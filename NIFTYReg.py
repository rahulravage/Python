#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 19 16:42:47 2018

@author: nehavishnoi
http://localhost:8000/predict?amnt=100000&years=2
gunicorn --bind 0.0.0.0:8000 NIFTYReg:app
sudo lsof -i :8000
sudo kill -9 pid
"""

import pandas as pd
import json
import requests
import sklearn
import math, datetime
import numpy as np
from sklearn import preprocessing, cross_validation
from sklearn.linear_model import LinearRegression
from flask import Flask
from flask import request

df = pd.read_csv('NIFTY.csv')
df = df.iloc[::-1]
df = df[['High', 'Low', 'Price', 'Open']]
x=df['High']
x=[float(y.replace(',','')) for y in x]
df['High']=x
x=df['Low']
x=[float(y.replace(',','')) for y in x]
df['Low']=x
x=df['Price']
x=[float(y.replace(',','')) for y in x]
df['Price']=x
x=df['Open']
x=[float(y.replace(',','')) for y in x]
df['Open']=x
del x
df['HL_PCT'] = (df['High'] - df['Low'])/df['Low'] * 100.0
df['PCT_change'] = (df['Price'] - df['Open']) /df['Open'] * 100.0
forecast_col = 'Price'
forecast_out = 60

df['label'] = df[forecast_col].shift(-forecast_out)

X = np.array(df.drop(['label'],1))
X = preprocessing.scale(X)
X_lately = X[-forecast_out:]
X = X[:-forecast_out]

df.dropna(inplace=True)
y=np.array(df['label'])



#X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, test_size = 0.1)

clf = LinearRegression(n_jobs=-1)
clf.fit(X, y)

forecast_set = clf.predict(X_lately)

app= Flask(__name__)
@app.route('/predict')

#
def predict():
    amnt = request.args.get('amnt')
    x = request.args.get('years')
    x=int(x)
    amnt=float(amnt)
    if x >=1:
        data=(forecast_set[-1]/forecast_set[0])/60*(x*12)*(amnt)
    else:
        data=amnt
#    header = {'Content-Type': 'application/json', \
#                  'Accept': 'application/json'}

#    data = df.to_json(orient='records')
#    resp = requests.post("http://0.0.0.0:8000/predict", \
#                    data = json.dumps(data),\
#                    headers= header)
    return str(data)