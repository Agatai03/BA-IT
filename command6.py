import click

@click.command()
@click.option('--wallet_id', prompt='Enter your wallet ID', help='Wallet ID')
@click.option('--amount', prompt='Enter the amount to withdraw', type=float, help='Amount to withdraw')
def command5(wallet_id, amount):
    # Здесь будет логика для снятия денег со своего кошелька
    # Добавьте необходимые действия для снятия денег и обработки ошибок
    
    click.echo(f"Withdrawing {amount} from wallet {wallet_id}")
    click.echo("Withdrawal successful")

if __name__ == '__main__':
    command5()
