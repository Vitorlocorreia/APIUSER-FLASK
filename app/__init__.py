from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import Config
from flasgger import Swagger

db = SQLAlchemy()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    db.init_app(app)

    Swagger(app)
    with app.app_context():
        from .models import user_model  
        db.create_all()

        from .routes.user_routes import user_bp  
        app.register_blueprint(user_bp)

    return app
