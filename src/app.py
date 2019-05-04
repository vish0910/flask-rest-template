from flask import Flask, request

from api.v1.routes import blueprint as blueprint_v1, api as api_v1
from settings.main import DEBUG_MODE

app = Flask(__name__)
app.url_map.strict_slashes = False
app.register_blueprint(blueprint_v1, url_prefix='/v1')

# You can customise the host, port number, whether you want debuggin on or not and much more.
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=DEBUG_MODE)
