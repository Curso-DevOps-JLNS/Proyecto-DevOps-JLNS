import os
import newrelic.agent

from flask import Flask
from .models import db
from .routes import register_routes

def create_app(config_class=None):
    app = Flask(__name__)

    if config_class:
        app.config.from_object(config_class)
    else:
        app.config.from_pyfile("../config.py")

    db.init_app(app)

    from flask_restful import Api
    api = Api(app)
    
    # Instrumentar la aplicación Flask
    try:
        app.wsgi_app = newrelic.agent.WSGIApplicationWrapper(app.wsgi_app)
        print("✅ Flask app instrumented with New Relic")
    except Exception as e:
        print(f"❌ Failed to instrument Flask app: {e}")
    
    register_routes(api)
    return app