# importing libraries
from flask import Flask, request, Response, jsonify
from flask_sqlalchemy import SQLAlchemy
import urllib.parse
import os

# PHASE 2 - Docker passthrough environment variables
if "MY_USER" in os.environ:
    username = os.environ['MY_USER']
    password = os.environ['MY_PASS']
else:
    username = "NONE"
    password = "NONE"
print(f"Running with user: {username} with password: {password}")

# creating an instance of the flask app
app = Flask(__name__)
db_server = '10.28.28.30'
db_user = 'carlot'
db_password = urllib.parse.quote_plus("I@mR00t") # Fix for passwords with non-alphanumeric symbols
db_name = 'car_demo'

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
# Configure our Database
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://reader:Notr00t1@10.28.28.81:3306/car_demo'
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+mysqlconnector://{db_user}:{db_password}@{db_server}/{db_name}"
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False