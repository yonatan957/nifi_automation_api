import os
import requests
from dto import create_pg_payload
from typing import Dict

NIFI_API_BASE = os.getenv("NIFI_API_BASE", "https://localhost:8443/nifi-api")
USER_NAME = os.getenv("USER_NAME")
PASSWORD = os.getenv("PASSWORD")
VERIFY = os.getenv("VERIFY", True)
TOKEN = None

# I know that recursion is usually bad practice, but here I think it's readable and better.
def generic_request(method:str, url:str,*, json=None, data=None, params=None, retry_count=1) -> requests.models.Response:
    global TOKEN
    response = requests.request(
        url=f"{NIFI_API_BASE}{url}",
        method=method,
        verify=VERIFY,
        headers={
            "Authorization": f"Bearer {TOKEN}"
        },
        json=json,
        data=data,
        params=params
    )
    if response.status_code == 401 and retry_count > 0:
        ### if it doesn't work, try again with new token, decrease the retry_count in one
        TOKEN = get_token()
        return generic_request(method, url, json=json, data=data, params=params, retry_count=retry_count-1)
    return response

def get_token() -> str:
    res = requests.post(f'{NIFI_API_BASE}/access/token', data={
        "username": USER_NAME,
        "password": PASSWORD
    }, verify=VERIFY)
    if res.status_code not in [200, 201]:
        raise Exception(f"Failed to get token: {res.status_code} {res.text}")
    return res.text.strip()

def check_nifi_connection() -> Dict[str, str]:
    try:
        ### a random request, just to check
        response = generic_request("GET", "/flow/about")
        response.raise_for_status()
        return {"status": "success"}
    except Exception as e:
        return {"status": "error", "message": str(e)}

def get_root_id() -> str:
    response = generic_request("GET", "/flow/process-groups/root")
    if response.status_code != 200:
        raise Exception(f"failed to get root id: {res.status_code} {res.text}")
    root_pg = response.json()
    return root_pg["processGroupFlow"]["id"]
def create_first_process_group(name:str) -> str:
    try:
        root_pg_id = get_root_id()
        response = generic_request(
            "POST",
            f"/process-groups/{root_pg_id}/process-groups",
            json=create_pg_payload(name)
        )
        if response.status_code != 200:
            raise Exception("failed to create process-group")
    except Exception as e:
        return str(e)

