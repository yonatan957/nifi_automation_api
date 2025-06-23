from dotenv import load_dotenv
### i have to load the env before importing the rest of the modules.
load_dotenv()
import logging
from nifi.nifi_connector import check_nifi_connection


if __name__ == '__main__':
    logging.info(check_nifi_connection())