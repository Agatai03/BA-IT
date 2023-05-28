import click
import requests

def get_cryptocurrency_data(cryptocurrency):
    url = f"https://api.coingecko.com/api/v3/coins/{cryptocurrency}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        name = data['name']
        symbol = data['symbol']
        price = data['market_data']['current_price']['usd']
        price_change_percentage = data['market_data']['price_change_percentage_24h']
        
        click.echo(f"Name: {name}")
        click.echo(f"Symbol: {symbol}")
        click.echo(f"Price (USD): {price}")
        click.echo(f"Price Change (24h): {price_change_percentage}%")
    else:
        click.echo("Error: Unable to retrieve cryptocurrency information")

@click.command()
def command1():
    cryptocurrency = 'binancecoin'
    get_cryptocurrency_data(cryptocurrency)

if __name__ == "__main__":
    command1()
