# importing libraries
from flask import Flask, request, Response, jsonify
from flask_sqlalchemy import SQLAlchemy


# creating an instance of the flask app
app = Flask(__name__)

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
# Configure our Database
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://reader:Notr00t1@10.28.28.81:3306/ContainerDemo'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://{user}:{password}@{server}/{database}'.format(user='reader', password='Notr00t1', server='10.28.28.81', database='ContainerDemo')
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Set API endpoint URL
api_endpoint = "http://localhost:8080/api/vehicles"