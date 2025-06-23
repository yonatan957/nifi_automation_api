from dotenv import load_dotenv
### i have to load the env before importing the rest of the modules.
load_dotenv()
from nifi.nifi_connector import check_nifi_connection


print(check_nifi_connection())