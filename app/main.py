from nifi_services.nifi_service import NifiService
from nifi_services.nifi_registry_service import NifiRegistryService
from flask import Flask
from utils.logger import logger
from utils.consts import NIFI_API_URL, NIFI_USER_NAME, SHOULD_VERIFY_SSL, NIFI_PASSWORD, NIFI_REGISTRY_URL
from error.error_handler import register_error_handlers
from controllers.process_group import process_group_bp
from controllers.parameter_context import parameter_context_bp
from controllers.funnel import funnel_bp
from controllers.port import port_bp
from controllers.connection import connection_bp

app = Flask(__name__)
register_error_handlers(app)

app.config["nifi_service"] = NifiService(NIFI_API_URL, NIFI_USER_NAME, NIFI_PASSWORD, SHOULD_VERIFY_SSL)
app.config["nifi_registry_service"] = NifiRegistryService(NIFI_REGISTRY_URL)
app.register_blueprint(process_group_bp)
app.register_blueprint(funnel_bp)
app.register_blueprint(port_bp)
app.register_blueprint(connection_bp)
app.register_blueprint(parameter_context_bp)

if __name__ == '__main__':
    app.run(debug=True)