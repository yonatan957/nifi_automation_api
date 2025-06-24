import logging
import os
import requests
from nifi.dto import create_pg_payload, Request_Type, GenericDict, ConnectionResult, create_funnel_payload
from typing import Dict

NIFI_API_BASE = os.getenv("NIFI_API_BASE", "https://localhost:8443/nifi-api")
USER_NAME = os.getenv("USER_NAME")
PASSWORD = os.getenv("PASSWORD")
VERIFY = os.getenv("VERIFY", True).lower() == "true"
TOKEN = None

# I know that recursion is usually bad practice, but here I think it's readable and better.
def generic_request(method:Request_Type, url:str="", *, json:GenericDict=None, data:GenericDict=None, params:GenericDict=None, retry_count=1) -> requests.models.Response:
    """
    a generic function for create request to nifi, using the constants TOKEN, VERIFY (if we want
    secure requests or not, locally not), and trying again if you were unauthorized with another
    token, recursively, as many times as you want, with field "retry_count"
    :param method: the method for the request, of type :class:`Request_Type`
    :param url: the end of the url to use initial empty
    :param json: if you want to send json in body - An object of type Parameter_Type with unlimited (arbitrary) keys.
    :param data: if you want to send file in body - An object of type Parameter_Type with unlimited (arbitrary) keys.
    :param params: if you want to send with query params - An object of type Parameter_Type with unlimited (arbitrary) keys.
    :param retry_count: how many times you want the function will try again with another token in
    case of authentication failed, initially 1
    :return: the response from the server
    """
    global TOKEN
    response = requests.request(
        url=f"{NIFI_API_BASE}{url}",
        method=method.value,
        verify=VERIFY,
        headers={
            "Authorization": f"Bearer {TOKEN}"
        },
        json=json,
        data=data,
        params=params
    )
    # if the request is unauthorized, try again with new token, decrease the retry_count by one
    if response.status_code == 401 and retry_count > 0:
        TOKEN = get_token()
        return generic_request(method, url, json=json, data=data, params=params, retry_count=retry_count-1)
    return response

def get_token() -> str:
    response = requests.post(f'{NIFI_API_BASE}/access/token', data={
        "username": USER_NAME,
        "password": PASSWORD
    }, verify=VERIFY)
    if response.status_code not in [200, 201]:
        raise Exception(f"Failed to get token: {response.status_code} {response.text}")
    token = response.text.strip()
    return token

def is_connection_good() -> ConnectionResult:
    """
    :return: :class:`ConnectionResult`
    """
    try:
        ### a random request, just to check
        response = generic_request(Request_Type.GET, "/flow/about")
        response.raise_for_status()
        return {"succeeded": True, "message":"Connection is good"}
    except Exception as e:
        return {"succeeded": False, "message":str(e)}

def get_root_id() -> str:
    response = generic_request(Request_Type.GET, "/flow/process-groups/root")
    if response.status_code != 200:
        raise Exception(f"failed to get root id: {response.status_code} {response.text}")
    root_pg = response.json()
    return root_pg["processGroupFlow"]["id"]

def create_process_group(name:str, father_id:str) -> str:
    try:
        response = generic_request(
            Request_Type.POST,
            f"/process-groups/{father_id}/process-groups",
            json=create_pg_payload(name)
        )
        if response.status_code not in (200, 201):
            raise Exception(f"failed to create process-group{response.text}")

        new_process_group = response.json()
        return new_process_group["id"]
    except Exception as e:
        logging.error(e)
        raise e

def create_funnel(process_group_id: str) -> str:
    response = generic_request(
        Request_Type.POST,
        f"/process-groups/{process_group_id}/funnels",
        json=create_funnel_payload()
    )
    if response.status_code not in (200, 201):
        raise Exception(f"failed to create funnel - {response.text}")

    new_funnel = response.json()
    return new_funnel["id"]

