import requests
from nifi_services.dto import Request_Type, GenericDict
from utils.consts import NIFI_API_BASE, USER_NAME, PASSWORD, SHOULD_VERIFY_SSL
TOKEN = None

# I know that recursion is usually bad practice, but here I think it's readable and better.
def generic_request(method:Request_Type, url:str="", *, json:GenericDict=None, data:GenericDict=None, params:GenericDict=None, retry_count=1) -> requests.models.Response:
    """
    a generic function for create request to nifi_services, using the constants TOKEN, VERIFY (if we want
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
        verify=SHOULD_VERIFY_SSL,
        headers={
            "Authorization": f"Bearer {TOKEN}"
        },
        json=json,
        data=data,
        params=params
    )
    ### if the request is unauthorized, try again with new token, decrease the retry_count by one
    if response.status_code == 401 and retry_count > 0:
        TOKEN = get_token()
        return generic_request(method, url, json=json, data=data, params=params, retry_count=retry_count-1)
    return response


def get_token() -> str:
    response = requests.post(f'{NIFI_API_BASE}/access/token', data={
        "username": USER_NAME,
        "password": PASSWORD
    }, verify=SHOULD_VERIFY_SSL)
    if response.status_code not in [200, 201]:
        raise Exception(f"Failed to get token: {response.status_code} {response.text}")
    token = response.text.strip()
    return token