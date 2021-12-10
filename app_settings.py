# importing libraries
from flask import Flask, request, Response, jsonify, flash, url_for, redirect, render_template
import json
from werkzeug.wrappers import response
import requests

# Set API endpoint URL
api_endpoint = "http://localhost:8080/api/vehicles"

# creating an instance of the flask app
app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

site_title = "Sir Cars-a-Lot"