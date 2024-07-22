import typer
import subprocess
import InquirerPy
from rich import print as rprint
import socket

app = typer.Typer()


@app.command("hi")
def sample_func():
    rprint("[red bold]Hi[/red bold] [yellow]World[yello]")

@app.command("hello")
def sample_func():
    rprint("[red bold]Hello[/red bold] [yellow]World[yello]")



if __name__ == "__main__":
    app()   