#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 03:06:52 2019

@author: Felipe Soares
"""

from qtpylib.algo import Algo
import requests           #Para fazer solicitações http para binance
import json               #Para analisar o que a binance envia de volta
import pandas as pd       #Para armazenar e manipular os dados que recebemos de volta
import datetime as dt     #Para lidar com os tempos
from qtpylib.algo import Algo


criptomoeda = input('Criptomoeda listada na Binance:')

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




#ESTRATEGIA MEDIAS MOVEIS
class CrossOver(Algo):

    def on_bar(self, instrument):

        #obter histórico de instrumentos
        bars = instrument.get_bars(window=20)

        # certifique-se de que temos pelo menos 20 bares para trabalhar
        if len(bars) < 20:
            return

        # calcular médias usando rolling_mean interno
        bars['short_ma'] = bars['close'].rolling_mean(window=10)
        bars['long_ma']  = bars['close'].rolling_mean(window=20)

        # obter dados da posição atual
        positions = instrument.get_positions()

        # lógica de negociação - sinal de entrada
        if bars['short_ma'].crossed_above(bars['long_ma'])[-1]:
            if not instrument.pending_orders and positions["position"] == 0:

                # enviar um sinal de compra
                instrument.buy(1)

                # registrar valores para análise futura
                self.record(ma_cross=1)

        # lógica de negociação - sinal de saída
        elif bars['short_ma'].crossed_below(bars['long_ma'])[-1]:
            if positions["position"] != 0:

                # sair / achatar posição
                instrument.exit()

                # registrar valores para análise futura
                self.record(ma_cross=-1)


if __name__ == "__main__":
    strategy = CrossOver(
        instruments = [ ('criptomoeda') ],
        resolution  = "1H"
    )

    strategy.run()