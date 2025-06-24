import os
from dotenv import load_dotenv
load_dotenv()

NIFI_API_URL = os.getenv("NIFI_API_URL", "https://localhost:8443/nifi-api")
USER_NAME = os.getenv("USER_NAME")
PASSWORD = os.getenv("PASSWORD")
# Whether to verify the SSL certificate when making HTTP requests.
# This should be True in production for security, and can be False in testing or when using self-signed certificates.
SHOULD_VERIFY_SSL = os.getenv("SHOULD_VERIFY_SSL", True).lower() == "true"