"""Functions for CLI interaction"""

from uuid import UUID

import typer
from rich import print as rich_print

from wappscan.core import get_scan_info

app = typer.Typer(no_args_is_help=True)


@app.command()
def get(scan_id: UUID):
    """Get scan by ID"""
    rich_print(get_scan_info(scan_id))


@app.command()
def scan(target: str):
    """Run a scan on a given target"""
    pass
