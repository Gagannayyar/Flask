# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 13:09:02 2021

@author: Gagam

Starting an API for the random forest classifier
"""

import pickle
import numpy as np
import pandas as pd
from flask import Flask, request
from flasgger import Swagger

with open(r"C:\Users\hp\Documents\Practice\Flask\rf.pkl", "rb") as model_file:
    model = pickle.load(model_file)


app = Flask(__name__)

swagger = Swagger(app)

@app.route('/predict_file', methods=['POST'] )
def predict_iris():
    """Example file endpoint returning a prediction of predict_iris
    This is using docstring for specifications.
    ---
    parameters:
      - name: input_file
        in: formData
        type: file
        required: true
        responses:
        200:

     """
    input_data = pd.read_csv(request.files.get("input_file"), header = None)

    prediction = model.predict(input_data)


    return str(list(prediction))

if __name__ == '__main__':
    app.run()
