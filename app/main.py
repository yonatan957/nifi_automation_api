from nifi_services.nifi_service import NifiService
from utils.logger import logger
from utils.consts import NIFI_API_URL, NIFI_USER_NAME, SHOULD_VERIFY_SSL, NIFI_PASSWORD

if __name__ == '__main__':
    try:
        nifi_service = NifiService(NIFI_API_URL, NIFI_USER_NAME, NIFI_PASSWORD, SHOULD_VERIFY_SSL)
        root_id = nifi_service.get_root_id()
        process_group = nifi_service.create_process_group("new_process_group", root_id)
        funnel_id = nifi_service.create_funnel(process_group.id)
    except Exception as e:
        logger.error(e)