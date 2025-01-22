"""
Client for the WappScan.io REST API.

API Reference: https://wappscan.io/api-reference
"""

from uuid import UUID

import requests

from wappscan.exceptions import StartScanException


def get_scan_info(scan_id: UUID) -> dict:
    """Get scan by ID"""
    res = requests.get(f"https://api.wappscan.io/scans/{scan_id}", timeout=3)
    return res.json()


def run_scan(target: str) -> dict:
    """Run a scan on a given target"""

    parsed_target = target.strip()
    if not parsed_target.startswith("http://") and not parsed_target.startswith(
        "https://"
    ):
        parsed_target = f"https://{parsed_target}"
    if not parsed_target.endswith("/"):
        parsed_target = f"{parsed_target}/"

    res = requests.post(
        "https://api.wappscan.io/scans",
        timeout=3,
        json={"target": parsed_target},
    )

    if not res.ok:
        error_msg = res.json()["detail"][0]["msg"]
        raise StartScanException(res.status_code, error_msg)

    return res.json()
