import logging
from nifi.dto import create_pg_payload, Request_Type, GenericDict, ConnectionResult, create_funnel_payload
from typing import Dict

from nifi.utils import generic_request, get_token

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