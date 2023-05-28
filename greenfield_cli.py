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
    
@cli.command()
def command3():
    click.echo("Executing command 3")


@cli.command()
def command4():
    click.echo("Executing command 4")
    
@cli.command()
def command5():
    click.echo("Executing command 5")
    
@cli.command()
def command6():
    click.echo("Executing command 6")


    

if __name__ == "__main__":
    cli()
