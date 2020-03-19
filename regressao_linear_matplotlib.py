#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 15:47:15 2019

@author: Felipe Soares
"""


# Importando bibliotecas necessarias
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt 
import seaborn as sns
from sklearn import linear_model

# Lendo dados históricos BNBUSD 
binance = pd.read_csv('BNB-USD.csv')
binance.head()
print(binance)

x0 = binance['Open']
x1 = binance['High']
x2 = binance['Low']
x3 = binance['Volume']
x4 = binance['Date']

y = binance['Close']

# Construindo modelo de regressão LINEAR
figure = plt.figure(figsize=(15,8))
plt.scatter(x0, x1, x2, y)
plt.xlabel('Preço BinanceCoin')
plt.ylabel('Preço')



binance = linear_model.LinearRegression()
binance.fit([x0], [x1], [x2])
