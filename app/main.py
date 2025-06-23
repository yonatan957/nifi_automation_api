from dotenv import load_dotenv
load_dotenv()
from nifi.nifi_connector import check_nifi_connection


print(check_nifi_connection())