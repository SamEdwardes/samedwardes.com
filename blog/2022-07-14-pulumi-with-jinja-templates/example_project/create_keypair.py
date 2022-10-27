import os

from Crypto.PublicKey import RSA


def main():
    """Create a new keypair."""
    key = RSA.generate(2048)
    private_key = key.exportKey("PEM")
    public_key = key.publickey().exportKey("OpenSSH")

    with open("key.pem", "w") as f:
        f.write(private_key.decode())
   
    with open("key.pub", "w") as f:
        f.write(public_key.decode())

    return public_key, private_key


if __name__ == '__main__':
    main()
