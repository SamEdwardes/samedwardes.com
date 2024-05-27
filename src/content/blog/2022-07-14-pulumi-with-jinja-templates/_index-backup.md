---
title: Using Jinja2 Templates with Pulumi
draft: false
authors: sedwardes
tags: [python, infrastructure]
toc_min_heading_level: 2
toc_max_heading_level: 3
image: ./imgs/code-snippet.png
---

import CodeBlock from '@theme/CodeBlock';
import MainPy from '!!raw-loader!./example_project/__main__.py';
import RequirementsTxt from '!!raw-loader!./example_project/requirements.txt';
import CreateKeyPair from '!!raw-loader!./example_project/create_keypair.py';
import TemplatesEnv from '!!raw-loader!./example_project/templates/template.env';
import EnvOut from '!!raw-loader!./.envout';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';


Over the last few months, I have spent a lot of time working on AWS. I often need to spin up EC2 instances, databases, or other assets for testing. Doing this by hand can become burdensome. You need to click through the AWS CLI and keep track of everything you have created. This sounds like a perfect use case for infrastructure as code. Enter [Pulumi](https://www.pulumi.com)!

<!--truncate-->

## Motivation

If you are familiar with python, the learning curve for Pulumi is relatively low. I quickly learned how to spin up and destroy infrastructure in a programmatic way. One topic that I always struggled with was configuration and template files. Pulumi has no obvious built-in way to create template files that contain the dynamic values generated from Pulumi. For example, I may want to pass the IP address of my EC2 instance into a *.env* file.

After many different experiments, I have finally landed on a pattern that allows me to write templates using [Jinja2](https://jinja.palletsprojects.com/en/3.0.x/). This approach will enable me to:

- Define and render templates using Jinja2.
- Automatically update the templates by hashing the template files.


## TL/DR

You can find all of the code on GitHub: <https://github.com/SamEdwardes/personal-blog/tree/main/blog/2022-07-14-pulumi-with-jinja-templates>. You can download the code as a zip file using this link from [DownGit](https://minhaskamal.github.io/DownGit/#/home?url=https://github.com/SamEdwardes/personal-blog/tree/main/blog/2022-07-14-pulumi-with-jinja-templates).

Run the code below to spin up the infrastructure for yourself!


```bash
# Set your AWS Environment Variables so that Pulumi can access AWS
export AWS_ACCESS_KEY_ID=<YOUR_ACCESS_KEY_ID>
export AWS_SECRET_ACCESS_KEY=<YOUR_SECRET_ACCESS_KEY>

# Create a new virtual environment
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip wheel setuptools
pip install -r requirements.txt

# Create a key pair
python create_keypair.py
chmod 400 key.pem

# Create a new pulumi stack
pulumi stack init dev

# Spin up the infrastructure
pulumi up

# SSH into the EC2 instance and verify that the .env file has been set
ssh -i key.pem -o StrictHostKeyChecking=no ubuntu@$(pulumi stack output server_public_dns)
cat .env
```

## Setup

To spin up AWS infrastructure, Pulumi needs to be able to log into your account. You can do this through `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY` and environment variables.

```bash
export AWS_ACCESS_KEY_ID=<YOUR_ACCESS_KEY_ID>
export AWS_SECRET_ACCESS_KEY=<YOUR_SECRET_ACCESS_KEY>
```

Next, create a virtual environment, and install the dependencies:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip wheel setuptools
pip install -r requirements.txt
```

Lets see what is inside the *requirements.txt*:

<CodeBlock title="requirements.txt">{RequirementsTxt}</CodeBlock>

There are several packages we installed in addition to the minimum requirements from Pulumi:

- [pulumi-command](https://www.pulumi.com/registry/packages/command/): Used to execute commands on the remote EC2 server.
- [Jinja2](https://jinja.palletsprojects.com/en/3.0.x/): Used to generate dynamic templates.
- [pycryptodome](https://www.pycryptodome.org): Used to hash our template files so that Pulumi automatically.

Next, we need to create a new public and private key that we will use to SSH into our EC2 instance. I made a Python script that can quickly generate a unique public/private key pair. Create a unique pair by running:


```bash
python create_keypair.py
chmod 400 key.pem
```

<details>
<summary>
Expand to see <i>create_keypair.py</i>
</summary>
<CodeBlock language="python" title="create_keypair.py">{CreateKeyPair}</CodeBlock>
</details>

Lastly, create a new pulumi stack. I will name my stack *dev*, but you can call it whatever you like.

```bash
pulumi stack init dev
```

## pulumi up


You are now ready to spin up your infrastructure. Just run:

```bash
pulumi up
```

## \__main__.py deep dive

Let us take a closer look at __main__.py and see what is happening.

<details>
<summary>
Expand to see <i>__main.py__</i>
</summary>
<CodeBlock language="python" title="__main__.py">{MainPy}</CodeBlock>
</details>

Below we will walk through some of the critical parts of the code.


### create_template(path: str)

```python
import jinja2

def create_template(path: str) -> jinja2.Template:
    with open(path, 'r') as f:
        template = jinja2.Template(f.read())
    return template
```

This is a helper function so we can quickly create a `jinja2.Template` object. We wrap this logic in a function so we can easily call it later inside of `pulumi_command.remote.Command`.

### hash_file(path: str)

```python
import hashlib

def hash_file(path: str) -> pulumi.Output:
    with open(path, mode="r") as f:
        text = f.read()
    hash_str = hashlib.sha224(bytes(text, encoding='utf-8')).hexdigest()
    return pulumi.Output.concat(hash_str)
```

This function will create a unique hash of our template files. Note that we return a `pulumi.Output` object.


### command_render_template

This code chunk is really the core of what we are doing:

```python
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
```

The basic approach is to run an `echo` command on the remote server that writes our rendered template to a file.

```bash
echo "TEMPLATE CONTENTS" > .env
```

The tricky part is getting our rendered template into `"TEMPLATE CONTENTS"`. To do this, we need to use `pulumi.Output.concat`. This function allows you to use the output of other `pulumi.Output` objects. Notice that we pass in all the values we want to access in our template.

```python
pulumi.Output.all(
    public_ip=server.public_ip,
    availability_zone=server.availability_zone,
    cpu_core_count=server.cpu_core_count
)
```

Then, we can use `pulumi.Output.concat().apply` to pass these values into another function. Here, we will create a `jinja2.Template` object with our `create_template` function and dynamically render the values.

```python
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
)
```

Note that the keyword arguments inside `create_template(local_file_path).render` should match the values in your template.

<CodeBlock title="templates/.env">{TemplatesEnv}</CodeBlock>

## See the results

Now that you have run `pulumi up` and created a dynamically rendered template let us check out the results. SSH into your EC2 instance:

```bash
ssh -i key.pem -o StrictHostKeyChecking=no ubuntu@$(pulumi stack output server_public_dns)
```

Once inside your EC2 instance, inspect the template that we generated.


```bash
cat .env
```

```
IP_ADDRESS=3.21.35.72
CPU_CORE_COUNT=1
AVAILABILITY_ZONE=us-east-2c
```

## Wrap up

With jinja2 and Pulumi we are now able to turn this:

<CodeBlock title="templates/template.env">{TemplatesEnv}</CodeBlock>

Into this!

<CodeBlock title="~/.env">{EnvOut}</CodeBlock>





