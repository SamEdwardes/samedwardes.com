"""An AWS Python Pulumi program"""

import hashlib
from pathlib import Path

import jinja2
import pulumi
from pulumi_aws import ec2
from pulumi_command import remote

# ------------------------------------------------------------------------------
# Helper functions
# ------------------------------------------------------------------------------    

def create_template(path: str) -> jinja2.Template:
    with open(path, 'r') as f:
        template = jinja2.Template(f.read())
    return template


def hash_file(path: str) -> pulumi.Output:
    with open(path, mode="r") as f:
        text = f.read()
    hash_str = hashlib.sha224(bytes(text, encoding='utf-8')).hexdigest()
    return pulumi.Output.concat(hash_str)


# ------------------------------------------------------------------------------
# Infrastructure
# ------------------------------------------------------------------------------

def main():
    # Customize these with your own tags!
    tags = {
        "rs:environment": "development",
        "rs:owner": "name@email.com",
        "rs:project": "solutions",
    }

    key_pair = ec2.KeyPair(
        "ec2 key pair",
        key_name=f"keypair-for-pulumi",
        public_key=Path("key.pub").read_text(),
        tags=tags | {"Name": "keypair-for-pulumi"},
    )
    
    # Make security groups
    security_group = ec2.SecurityGroup(
        "security group",
        description="Security group for my blog post",
        ingress=[{"protocol": "TCP", "from_port": 22, "to_port": 22, 'cidr_blocks': ['0.0.0.0/0'], "description": "SSH"}],
        egress=[{"protocol": "All", "from_port": -1, "to_port": -1, 'cidr_blocks': ['0.0.0.0/0'], "description": "Allow all outbound traffic"}],
        tags=tags
    )
    
    # Create a new ec2 instance
    server = ec2.Instance(
        "EC2 instance",
        instance_type="t3.medium",
        vpc_security_group_ids=[security_group.id],
        ami="ami-0fb653ca2d3203ac1",  # Ubuntu Server 20.04 LTS (HVM), SSD Volume Type
        tags=tags,
        key_name=key_pair.key_name
    )

    pulumi.export('server_public_dns', server.public_dns)

    # Create a connection that will be used to SSH into the ec2 instance
    connection = remote.ConnectionArgs(
        host=server.public_dns, 
        user="ubuntu", 
        private_key=Path("key.pem").read_text()
    )

    # Render a template on the ec2 instance
    local_file_path = "templates/template.env"
    remote_file_path = "~/.env"
    
    command_render_template = remote.Command(
        "copy .env",
        create=pulumi.Output.concat(
            'echo "',
            pulumi.Output.all(
                public_ip=server.public_ip,
                availability_zone=server.availability_zone,
                cpu_core_count=server.cpu_core_count
            ).apply(
                lambda args: create_template(local_file_path).render(
                    ip_address=args['public_ip'],
                    availability_zone=args['availability_zone'],
                    cpu_core_count=args['cpu_core_count']
                )
            ), 
            f'" > {remote_file_path}'
        ),
        connection=connection, 
        opts=pulumi.ResourceOptions(depends_on=[server]),
        triggers=[hash_file(local_file_path)]
    )


main()
