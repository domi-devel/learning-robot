import click

# Absolute import in case the relative import fails
try:
    from .app import create_app
except ImportError:
    from app import create_app


@click.group()
def cli():
    pass


@click.command()
@click.option(
    "--env",
    default="development",
    help="Environment to use while running server",
    type=click.STRING,
)
@click.option(
    "--port", default=5000, help="Port to use while running server", type=click.STRING
)
def runserver(env, port):
    app = create_app(env)
    app.run(port=port)


# Add other commands here
# Eg.
# def initdb():
#    ''' Create the SQL DB '''
#    db.create_all()


cli.add_command(runserver)
# Register other commands here
# Eg.
# cli.add_command(initdb)

if __name__ == "__main__":
    cli()
