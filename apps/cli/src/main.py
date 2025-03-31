import click
import subprocess
from pathlib import Path

@click.group()
def cli() -> None:
    pass

@cli.command()
def start() -> None:
    """Start the API backend server"""
    api_path = Path(__file__).parent.parent.parent / 'api' / 'src'
    try:
        subprocess.run(['uvicorn', 'apps.api.src.main:app', '--reload'], cwd=str(api_path))
    except KeyboardInterrupt:
        click.echo('\nStopping API server...')
    except Exception as e:
        click.echo(f'Error starting API server: {e}')


if __name__ == '__main__':
    cli()
