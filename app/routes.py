from flask import Blueprint, jsonify, abort, make_response, request
from app.models.question import Question
from app import db
import os
from random import sample 
# import requests 
# from dotenv import load_dotenv


# create blueprint
questions_bp = Blueprint("questions_bp", __name__, url_prefix="/questions")

# keep track of questions answered right
# global bc want to keep track accross multiple requests!
num_correct = 0


# validate model
def validate_model(cls, model_id):
    try:
        model_id = int(model_id)
    except:
        abort(make_response({"message":f"{cls.__name__} {model_id} invalid"}, 400))

    model = cls.query.get(model_id)
    
    if not model:
        abort(make_response(jsonify({"message":f"{cls.__name__} {model_id} not found"}), 404))
    
    return model


#create endpoints 
'''
GET all questions from db, select 25 random for game
'''
@questions_bp.route("", methods=["GET"])
def get_random_questions():
    # SQLAlchemy to query db for all instances of `Question` model
    questions = Question.query.all()
    print(f"Number of questions in database: {len(questions)}")
    
    # debugging 
    # use make_response when returning strings or dictionaries
    if len(questions) < 25:
        abort(make_response(jsonify({"message":"Not enough questions in the database"}), 400))
        
    # return 25 random questions from db
    random_questions = sample(questions, 25)
    
    # serializing model instance data to dict format (JSON) for frontend
    questions_response = [question.to_dict() for question in random_questions]
    
    # reset score and number of correct answers for each new game
    global num_correct
    num_correct = 0
    
    # list of 25 question dictionaries
    # pass into jsonfy() to turn it into a response object
    return jsonify(questions_response), 200



'''
HANDLE ANSWER SUBMISSION
POST user answer to server, update score and number of correct answers
'''
@questions_bp.route("/answer", methods=["POST"])
def check_user_answer():
    # extract JSON data from POST request
    # DESERIALIZE, convert from JSON to python dict
    data = request.get_json()
    # extract JSON data, reassign
    question_id = data["question_id"]
    user_answer = data["user_answer"]
    
    # get the correct answer for the question from database
    question = validate_model(Question, question_id)
    correct_answer = question.correct_answer
    
    # check if user's answer matches correct answer
    # update score and number of correct answers
    global num_correct
    if user_answer == correct_answer:
        num_correct += 1
    
    # don't return any data, just resetting score variables
    # 200 OK
    return jsonify({}), 200
    
    
    
'''
GET user's final score and number of correct answers
'''
@questions_bp.route("/score", methods=["GET"])
def get_user_score():
    global num_correct
    
    percentage_score = (num_correct / 25) * 100
    
    # create a dictionary to hold the score information
    response_data = {"num_correct": num_correct,  "percentage_score": percentage_score}

    return jsonify(response_data), 200




