from nifi_services.nifi_connector import (
    is_nifi_connection_alive,
    get_root_id,
    create_process_group,
    create_funnel,
    get_process_group)
from utils.logger import logger

if __name__ == '__main__':
    connection_status = is_nifi_connection_alive()

    try:
        root_id = get_root_id()
        process_group_id = create_process_group("my-pg", root_id)
        process_group = get_process_group(process_group_id)
        logger.info(f'successfully create new process-group with id - {process_group.id}, named {process_group.component.name}')
        funnel_id = create_funnel(process_group_id)
        logger.info(f'successfully create new funnel with id - {funnel_id}')
    except Exception as e:
        logging.error(e)