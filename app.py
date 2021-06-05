from flask import Flask, render_template, request
import jsonify
import requests
import flasgger
from flasgger import Swagger
import pandas as pd
import numpy as np
import pickle

app = Flask(__name__)
Swagger(app)
model = pickle.load(open('banknote.pkl','rb'))

@app.route('/',methods=['GET'])
def Welcome():
    return "Welcome to BankNoteAuthenticator!"

@app.route('/predict',methods=['GET'])
def predict():
    """Please Enter the Details to Authenticate a BankNote
    This is using docstrings for specifications.
    ---
    parameters:
      - name: variance
        in: query
        type: number
        required: true
      - name: skewness
        in: query
        type: number
        required: true
      - name: curtosis
        in: query
        type: number
        required: true
      - name: entropy
        in: query
        type: number
        required: true
    responses:
        200:
            description: The output values
    """
    variance = request.args.get('variance')
    skewness = request.args.get('skewness')
    curtosis = request.args.get('curtosis')
    entropy = request.args.get('entropy')

    prediction = model.predict([[variance,skewness,curtosis,entropy]])
    if prediction[0]==0:
        return "This is a Fake BankNote!"
    else:
        return "This is an Authentic BankNote!"

if __name__=='__main__':
    app.run(host="0.0.0.0",port=5000)
