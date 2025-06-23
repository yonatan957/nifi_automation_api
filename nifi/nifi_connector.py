import os
import requests
from typing import Dict

NIFI_API_BASE = os.getenv("NIFI_API_BASE", "https://localhost:8443/nifi-api")
USER_NAME = os.getenv("USER_NAME")
PASSWORD = os.getenv("PASSWORD")

def get_token() -> str:
    res = requests.post(f'{NIFI_API_BASE}/access/token', data={
        "username": USER_NAME,
        "password": PASSWORD
    }, verify=False)
    if res.status_code not in [200, 201]:
        raise Exception(f"Failed to get token: {res.status_code} {res.text}")
    return res.text.strip()

def check_nifi_connection() -> Dict[str, str]:
    try:
        token = get_token()
        ### a random request, just to check
        res = requests.get(f'{NIFI_API_BASE}/flow/about', headers={
            "Authorization": f"Bearer {token}"
        }, verify=False)
        res.raise_for_status()
        return {"status": "success"}
    except Exception as e:
        return {"status": "error", "message": str(e)}