#!/usr/bin/python3
from flask import Flask, jsonify
from flask_cors import CORS
import models
from models import storage
import datetime
from .authentication import auth
from flask import request

from flask_jwt_extended import create_access_token
from flask_jwt_extended import JWTManager, get_jwt

app = Flask(__name__)

with app.app_context():
    from api.views import app_views


app.register_blueprint(app_views)
cors = CORS(app, resources={r"/*": {"origins": "*"}})
app.register_blueprint(auth)
app.config["JWT_SECRET_KEY"] = "erfij3ouRH4OUR4OR3ORN"
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = datetime.timedelta(hours=1)
jwt = JWTManager(app)

@app.after_request
def refresh_expiring_jwts(response):
    try:
        exp_timestamp = get_jwt()["exp"]
        now = datetime.now(timezone.utc)
        target_timestamp = datetime.timestamp(now + timedelta(minutes=30))
        if target_timestamp > exp_timestamp:
            access_token = create_access_token(identity=get_jwt_identity())
            set_access_cookies(response, access_token)
        return response
    except (RuntimeError, KeyError):
        # Case where there is not a valid JWT. Just return the original response
        return response

@app.errorhandler(404)
def handle_404(e):
    """ handles a 404 httpexception"""
    return jsonify({'error': "Not found"}), 404

@app.errorhandler(400)
def handle_400(e):
    """handles code 400 httpexception """
    message = e.description
    return jsonify({'error': message}), 400

@app.teardown_appcontext
def teardown_db(exception):
    """ closes off session with database"""
    models.storage.close()

if __name__ == "__main__":
    app.run(port=5000, host="0.0.0.0", threaded=True)
