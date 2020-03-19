#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 15:47:15 2019

@author: Felipe Soares
"""
# USAR EM JUPYTER NOTEBOOK

# Regressão LINEAR com SCKIT-LEARN

# Importando bibliotecas necessarias
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt 
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score




# Lendo dados históricos BNBUSD 
binance = pd.read_csv('BNB-USD.csv')
binance.head()
print(binance)

x0 = binance['Open'].values.reshape(-1,1)
x1 = binance['High'].values.reshape(-1,1)
x2 = binance['Low'].values.reshape(-1,1)
x3 = binance['Volume'].values.reshape(-1,1)
x4 = binance['Date']

y = binance['Close'].values.reshape(-1,1)

# Construindo modelo de regressão LINEAR
figure = plt.figure(figsize=(15,8))
plt.scatter(x0, x1, x2, y)
plt.xlabel('Preço BinanceCoin')
plt.ylabel('Preço')

x_train = x0[:-20]
x_test = x0[-20:]

y_train = y[:-20]
y_test = y[-20:]

binance = linear_model.LinearRegression()
binance.fit(x_train, y_train)
binance_y_pred = binance.predict(x_test)

print('Coefficients: \n', binance.coef_)
print("Mean squared error: %.2f"
      % mean_squared_error(y_test, binance_y_pred))

plt.plot(binance_y_pred)

print(binance_y_pred)