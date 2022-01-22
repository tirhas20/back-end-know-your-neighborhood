from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
from flask_migrate import Migrate
from dotenv import load_dotenv 
import os
from flask_cors import CORS

db = SQLAlchemy()
migrate = Migrate()
load_dotenv()

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("SQLALCHEMY_DATABASE_URI")
    
    # import models
    from app.models.business import Business
    
    # from app.models.ExampleModel import ExampleModel
    db.init_app(app)
    migrate.init_app(app, db)
    
    #register blueprints
    from .routes import businnes_bp
    app.register_blueprint(businnes_bp)
    
    
    
    CORS(app)
    return app