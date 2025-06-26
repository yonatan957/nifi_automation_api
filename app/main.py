from nifi_services.nifi_service import NifiService
from flask import Flask
from utils.logger import logger
from utils.consts import NIFI_API_URL, NIFI_USER_NAME, SHOULD_VERIFY_SSL, NIFI_PASSWORD
from error.error_handler import register_error_handlers
from controllers.process_group import process_group_bp
from controllers.funnel import funnel_bp
from controllers.port import port_bp
app = Flask(__name__)
register_error_handlers(app)
app.config["nifi_service"] = NifiService(NIFI_API_URL, NIFI_USER_NAME, NIFI_PASSWORD, SHOULD_VERIFY_SSL)

app.register_blueprint(process_group_bp)
app.register_blueprint(funnel_bp)
app.register_blueprint(port_bp)

if __name__ == '__main__':
    app.run(debug=True)