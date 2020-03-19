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
from sklearn.linear_model import LinearRegression

# Lendo dados históricos BNBUSD 
advert = pd.read_csv('BNB-USD.csv')
advert.head()

# Construindo modelo de regressão LINEAR
predictors = ['High', 'Low']
X = advert[predictors]
y = advert['Close']

# Inicialização e modelo de ajuste
lm = LinearRegression()
model = lm.fit(X, y)

# model.intercept para retornar valor de ALPHA e model.coef_ para uma matriz com nossos coeficientes BETA1 e BETA2
print ( f ' alpha = { model.intercept_ }' )
print ( f ' betas = { model.coef_ } ' )

# Possivel previssão do preço de fechamento
model.predict (X)