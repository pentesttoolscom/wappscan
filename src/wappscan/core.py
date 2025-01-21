"""Core logic"""

from uuid import UUID

import requests


def get_scan_info(scan_id: UUID) -> dict:
    """Get scan by ID"""
    res = requests.get(f"https://api.wappscan.io/scans/{scan_id}")
    return res.json()
