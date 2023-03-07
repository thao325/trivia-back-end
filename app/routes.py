from flask import Blueprint, jsonify, abort, make_response, request
from app.models.question import Question
from app import db
import os
from random import sample 
# import requests 
# from dotenv import load_dotenv


# create blueprint
questions_bp = Blueprint("questions_bp", __name__, url_prefix="/questions")

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
    
    # list of question dictionaries, pass into jsonfy()
    # to turn it into a response object 
    # (serializing model instance data to dict format (JSON) for frontend) 
    questions_response = [question.to_dict() for question in random_questions]
    return jsonify(questions_response), 200


    
    


# '''
# HANDLE SCORE
# '''

# @app.route('/submit-answers', methods=['POST'])
# def submit_answers():
#     data = request.get_json()
#     # `data` = list of dictionaries, where each dict represents a question
#     # Each dictionary contains the user's answer for that question

#     # keep track of # of correct answers
#     num_correct = 0

#     # Loop through each Q, check if user's answer is correct
#     for question_data in data:
#         question_id = question_data['id']
#         user_answer = question_data['answer']
#         question = Question.query.get(question_id)

#         # Check if the user's answer is correct
#         if user_answer == question.correct_answer:
#             num_correct += 1

#     # Calculate the user's score based on the number of correct answers
#     score = num_correct * 10  # assuming each correct answer is worth 10 points

#     # Return the number of correct answers and the score as a JSON response
#     return jsonify({'num_correct': num_correct, 'score': score})









# ====== RANDOM LOGIC???? ========== ##

# @app.route('/questions/<int:id>/answer', methods=['POST'])
# def answer_question(id):
#     req_body = request.get_json()
#     question = Question.query.get(id)

#     if question.correct_answer == req_body['answer']:
#         question.score += 1
#         db.session.commit()

#     return jsonify(question.to_dict())


# # Get the current question
# question = Question.query.get(question_id)

# # Check if the user's answer is correct
# if user_answer == question.correct_answer:
#     # Increment the user's score
#     question.score += 1
#     db.session.commit()

# # Get the number of correct answers
# num_correct = Question.query.filter(Question.score == 1).count()

# # Calculate the final score as a percentage
# final_score = (num_correct / 25) * 100