import os
from dotenv import load_dotenv
load_dotenv()

NIFI_API_BASE = os.getenv("NIFI_API_BASE", "https://localhost:8443/nifi-api")
USER_NAME = os.getenv("USER_NAME")
PASSWORD = os.getenv("PASSWORD")
VERIFY = os.getenv("VERIFY", True).lower() == "true"