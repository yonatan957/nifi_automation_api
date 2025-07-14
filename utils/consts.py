import os
from dotenv import load_dotenv
load_dotenv()

NIFI_API_URL = os.getenv("NIFI_API_URL", "https://localhost:8443/nifi-api")
NIFI_USER_NAME = os.getenv("NIFI_USER_NAME")
NIFI_PASSWORD = os.getenv("NIFI_PASSWORD")
NIFI_REGISTRY_URL = os.getenv("NIFI_REGISTRY_URL")
# Whether to verify the SSL certificate when making HTTP requests.
# This should be True in production for security, and can be False in testing or when using self-signed certificates.
SHOULD_VERIFY_SSL = os.getenv("SHOULD_VERIFY_SSL", True).lower() == "true"