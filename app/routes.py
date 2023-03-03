from flask_sqlalchemy import SQLAlchemy
from flask import Blueprint, jsonify, abort, make_response, request
# from app.models.task import Task
# from app.models.goal import Goal
# from app import db
# from sqlalchemy import asc, desc
# import datetime, requests, os
# from dotenv import load_dotenv

# load_dotenv()


# create blueprint
questions_bp = Blueprint("questions", __name__, url_prefix="/questions")

# create endpoints 
@questions_bp.route("", methods=["GET"])
def get_questions():

    
    
    # returns list of question dictionaries, pass into jsonfy()
    # to turn it into a response object
    return jsonify(questions_response)

    # use make_response when returning strings or dictionaries