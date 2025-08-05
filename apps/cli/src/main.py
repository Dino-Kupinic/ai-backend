import os
import signal
import sys

import click
import subprocess
from pathlib import Path


@click.group()
def cli() -> None:
    pass


PID_FILE = Path("server.pid")
"""File to store if the server is running."""


@cli.command()
def start() -> None:
    """Start the API backend server"""
    api_path = Path(__file__).parent.parent.parent / "api" / "src"
    try:
        api_process = subprocess.Popen(
            ["fastapi", "run", "main.py"],
            cwd=str(api_path),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        pid = api_process.pid

        with open(PID_FILE, "w") as f:
            f.write(str(pid))

        click.echo(f"\nStarted API server with {pid}")

        for line in iter(api_process.stdout.readline, ""):
            sys.stdout.write(line)
            sys.stdout.flush()
    except Exception as e:
        click.echo(f"Error starting API server: {e}")


@cli.command()
def stop() -> None:
    """Stop the API backend server"""
    if not PID_FILE.exists():
        click.echo("API server is not running.")
        return

    try:
        with open(PID_FILE, "r") as f:
            pid = int(f.read().strip())

        os.kill(pid, signal.SIGTERM)

        PID_FILE.unlink()
        click.echo(f"API server with PID {pid} stopped.")
    except Exception as e:
        click.echo(f"Error stopping API server: {e}")


if __name__ == "__main__":
    cli()
