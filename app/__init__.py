from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate 
# import os
# from dotenv import load_dotenv

db = SQLAlchemy()
migrate = Migrate()
# load_dotenv()

# create the object of Flask
def create_app(test_config=None):
    app = Flask(__name__)
    
    # SQLAlchemy db config w/ MySQL
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:P3r!winkle@localhost/question'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    db.init_app(app)
    migrate.init_app(app, db)


    # register blueprint
    from .routes import questions_bp
    app.register_blueprint(questions_bp)
    
    return app