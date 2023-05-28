import click

@click.group()
def cli():
    pass

@cli.command()
def command1():
    click.echo("Executing command 1")

@cli.command()
def command2():
    click.echo("Executing command 2")

if __name__ == "__main__":
    cli()
