import click
import random
import string

def generate_wallet():
    wallet_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
    private_key = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=20))
    public_key = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=20))
    
    return wallet_id, private_key, public_key

@click.command()
def command5():
    wallet_id, private_key, public_key = generate_wallet()
    
    click.echo("Wallet created successfully!")
    click.echo(f"Wallet ID: {wallet_id}")
    click.echo(f"Private Key: {private_key}")
    click.echo(f"Public Key: {public_key}")

if __name__ == "__main__":
    command5()
