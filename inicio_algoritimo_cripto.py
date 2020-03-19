#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 14:39:06 2019

@author: Felipe Soares
"""
#Importando Bibliotecas usadas
import requests           #Para fazer solicitações http para binance
import json               #Para analisar o que a binance envia de volta
import pandas as pd       #Para armazenar e manipular os dados que recebemos de volta
import datetime as dt     #Para lidar com os tempos


#Esolhe a Criptomoedas e valores de negociação
criptomoeda = input('Criptomoeda listada na Binance:')
valor_negociado = input('Valor negociado em Bitcoin:')
print('A criptomoeda informada foi: %s, e o valor negociado foi: %s' %(criptomoeda, valor_negociado))



#Cria URL da API Binance
root_url = 'https://api.binance.com/api/v1/klines'

symbol = criptomoeda

interval = '1h'

url = root_url + '?symbol=' + symbol + '&interval=' + interval
print(url)



#Monta URL e o Gráfico 
def get_bars(symbol, interval = '1h'):
   url = root_url + '?symbol=' + symbol + '&interval=' + interval
   data = json.loads(requests.get(url).text)
   df = pd.DataFrame(data)
   df.columns = ['open_time',
                 'o', 'h', 'l', 'c', 'v',
                 'close_time', 'qav', 'num_trades',
                 'taker_base_vol', 'taker_quote_vol', 'ignore']
   df.index = [dt.datetime.fromtimestamp(x/1000.0) for x in df.close_time]
   return df

criptomoeda = get_bars(criptomoeda)

criptomoeda = criptomoeda['c'].astype('float') 

criptomoeda.plot(figsize = (10,5))

#Faz a previsão do capital investido de acordo com o valor informado
