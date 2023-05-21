import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 


def divide(x): #função que irá dividir os valores de tempo, uma vez que foram transmitidos em mseg e queremos em seg
    return x/1000


headers = ['Temperatura', 'Tempo', 'Referencia'] #dando nomes para as 'headers'
df = pd.read_csv('data08_05_LigadoAteDesligar_2.csv', names=headers) #transferindo dados do arquivo para um dataframe
df['Tempo'] = df['Tempo'].map(divide) #dividindo valores da coluna de tempo para termos eles em segundos e não ms


#código para plot do grafico
plt.grid()          #cria nova grade de gráfico
plt.plot(df['Tempo'],df['Temperatura'], '-b', label = 'Resposta em MA da Planta') #plot da temperatura em azul
plt.plot(df['Tempo'],df['Referencia'],'-y', label = 'Temperatura de Referência (degrau)') #plot da referencia em amarelo
#colocando legenda nos eixos
plt.xlabel('Tempo (s)') 
plt.ylabel('Temperatura (°C)')
#adicionando legenda das curvas
plt.legend()
#mostrando a figura em nova aba
plt.show()






