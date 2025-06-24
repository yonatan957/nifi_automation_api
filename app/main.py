from dotenv import load_dotenv
### I have to load the env before importing the rest of the modules.
load_dotenv()
import logging
from nifi.nifi_connector import (
    is_connection_good,
    get_root_id,
    create_process_group,
    create_funnel,
    get_process_group)
logging.basicConfig(level=logging.INFO)


if __name__ == '__main__':
    connection_status = is_connection_good()
    if connection_status["succeeded"] is not True:
        logging.error(connection_status["message"])
        raise Exception(connection_status["message"])

    try:
        root_id = get_root_id()
        process_group_id = create_process_group("my-pg", root_id)
        process_group = get_process_group(process_group_id)
        logging.info(f'successfully create new process-group with id - {process_group.id}, named {process_group.component.name}')
        funnel_id = create_funnel(process_group_id)
        logging.info(f'successfully create new funnel with id - {funnel_id}')
    except Exception as e:
        logging.error(e)