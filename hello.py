from flask import Flask
from flask_restful import Resource, Api
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app) ## To allow direct AJAX calls

@app.route('/', methods=['GET'])
def home():
    r = requests.get('http://dummy.restapiexample.com/api/v1/employees', headers={"User-Agent": "XY"})
    return r.json()

if __name__ == '__main__':
   app.run(debug = True)
