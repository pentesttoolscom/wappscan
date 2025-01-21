"""Functions for CLI interaction"""

import json
from uuid import UUID

import typer
from rich import print_json

from wappscan.core import get_scan_info

app = typer.Typer(no_args_is_help=True)


@app.command()
def get(scan_id: UUID):
    """Get scan by ID"""
    scan_result = get_scan_info(scan_id)
    print_json(json.dumps(scan_result))


@app.command()
def scan(target: str):
    """Run a scan on a given target"""
    pass
