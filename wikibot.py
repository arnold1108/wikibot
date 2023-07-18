import click 
from mylib.bot import scrape

@click.command()
@click.option('--topic', prompt="Which topic do you need?")
@click.option('--sentences', default=1, prompt="How many sentences?")

def cli(topic, sentences):
    """Simple program to scrape the first n sentences of a wikipedia page"""
    result = scrape(topic, sentences)
    click.echo(click.style(f"{result}", fg='white'))

if __name__ == "__main__":
    cli()
