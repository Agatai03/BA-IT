import click
import requests

def get_currency_rate(base_currency, target_currency):
    url = f"https://api.exchangerate-api.com/v4/latest/{base_currency}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        rate = data['rates'][target_currency]
        click.echo(f"1 {base_currency} = {rate} {target_currency}")
    else:
        click.echo("Error: Unable to retrieve currency rates")

@click.command()
@click.option('--base', prompt='Enter base currency', help='Base currency')
@click.option('--target', prompt='Enter target currency', help='Target currency')
def command4(base, target):
    get_currency_rate(base, target)

if __name__ == "__main__":
    command4()
