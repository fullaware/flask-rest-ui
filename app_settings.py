# importing libraries
from flask import Flask, request, Response, jsonify, flash, url_for, redirect, render_template
import json
from werkzeug.wrappers import response
import requests
import os

# Set API endpoint URL
if "API_HOSTNAME" in os.environ and "API_PORT" in os.environ:
    api_endpoint = f"http://{os.environ['API_HOSTNAME']}:{os.environ['API_PORT']}/api/vehicles"
    
    print(f"\nConnecting to host : {os.environ['API_HOSTNAME']} on port: {os.environ['API_PORT']}\n")
else:
    print(f"\n INFO : Missing environment variables:\n")
    print(f"\n API_HOSTNAME\nAPI_PORT\n")
    print(f"\n Using default: http://host.docker.internal:8088\n")
    api_endpoint = "http://host.docker.internal:8088/api/vehicles"


# creating an instance of the flask app
app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'