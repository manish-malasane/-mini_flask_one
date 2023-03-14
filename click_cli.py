"""
Command to run this script::->
1) "python click_cli.py --count 3 --name Manthan"
2) "python click_cli.py --count 3"
    and then enter your name
"""
# This is like argparse module
import click


@click.command()
@click.option("--count", default=1, help="Number of greetings.")
@click.option("--name", prompt="Your name", help="The person to greet.")
def hello(count, name):
    """Simple code that greets NAME for a total of COUNT times"""
    for x in range(count):
        click.echo(f"Hello {name}")


if __name__ == "__main__":
    hello()
