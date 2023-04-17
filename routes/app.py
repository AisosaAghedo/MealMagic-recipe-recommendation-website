#!/usr/bin/python3
"""
module to hold the Flask object
"""
from models import storage
import datetime
from .authentication import auth
from flask import Flask
from flask import jsonify
from flask import request

from flask_jwt_extended import create_access_token
from flask_jwt_extended import JWTManager, get_jwt

app = Flask(__name__)
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

@app.teardown_appcontext
def teardown_db(exception):
    """ closes off session with database"""
    storage.close()

if __name__ == "__main__":
    app.run(port=5002)
