from nifi_services.nifi_service import NifiService
from utils.logger import logger
from utils.consts import NIFI_API_URL, NIFI_USER_NAME, SHOULD_VERIFY_SSL, NIFI_PASSWORD

if __name__ == '__main__':
    try:
        nifi_service = NifiService(NIFI_API_URL, NIFI_USER_NAME, NIFI_PASSWORD, SHOULD_VERIFY_SSL)

    except Exception as e:
        logging.error(e)