# -*- coding: utf-8 -*-
"""
An simple Random forest classifier for predicting the iris dataset
"""

#Importing neccessary libraries

import pandas as pd
import numpy as np
import sklearn
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


#loading dataset
iris = load_iris()
X = iris.data
y = iris.target

#Split data in train and test set
X_train, X_test, y_train, y_test = train_test_split(X,y, random_state=42, test_size=0.5)

#Building Model
clf = RandomForestClassifier(n_estimators=10)

#Train the classifier
clf.fit(X_train, y_train)

#Predictions
predicted = clf.predict(X_test)

#Accuracy
print(accuracy_score(predicted, y_test))

#Pickling the file
import pickle
with open("C:/Users/hp/Documents/Practice/Flask/rf.pkl", "wb") as model_pkl:
    pickle.dump(clf,model_pkl)

