from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate 
# import os
# from flask_cors import CORS
# from dotenv import load_dotenv

# creates new instance of SQLAlchemy class
db = SQLAlchemy()
migrate = Migrate()
# load_dotenv()

# create the object of Flask
def create_app(test_config=None):
    # app.debug = True
    app = Flask(__name__)
    
    # config Flask app w/ MySQL database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:P3r!winkle@localhost/question'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # Import models to create tables
    from app.models.question import Question
    
    # associate SQLAlchemy instance w/ flask app
    db.init_app(app)
    # initialize it w/ app
    migrate.init_app(app, db)
    
    # import questions_data after initializing db and Question
    # can't put at the top 
    from app.questions import questions_data
    
    with app.app_context():
    # iterate through the questions_data list and add each question to the database
        for question_data in questions_data:
            question = Question(prompt=question_data['prompt'], 
                                choice_1=question_data['choices']['1'],
                                choice_2=question_data['choices']['2'],
                                choice_3=question_data['choices']['3'],
                                choice_4=question_data['choices']['4'],
                                correct_answer=question_data['correct_answer'])
            db.session.add(question)
        db.session.commit()

    # create tables if they don't exist yet
    # with app.app_context():
    #     db.create_all()
        
    # register blueprint
    from app.routes import questions_bp
    app.register_blueprint(questions_bp)
    
    return app

