import click


@click.group()
def cli():
    pass


@cli.command()
def aiohttp_simple():
    from aiohttp_vs_fastapi.aiohttp.simple_response import run

    run()


if __name__ == "__main__":
    cli()
