import pandas as pd
import numpy as np
import control
import matplotlib.pyplot as plt 


#função que irá dividir o tempo que está em mseg para seg
def divide(x):
    return x/1000

#coletando dados do arquivo csv, alocando no dataframe e dividindo os valores do tempo para ter tudo em segundos
headers = ['Temperatura', 'Tempo', 'Referencia']
df = pd.read_csv('data08_05_LigadoAteDesligar_2.csv', names=headers)
df['Tempo'] = df['Tempo'].map(divide)


#Cálculo da Planta conforme descrito no artigo
# K = 70.5 / (100-25.69) 70.5 o deltaY; 100 é a ref final, 25.69 a inicial
#250 é a cte de tempo do sistema e o 1 representa o + 1 
# como se tivessemos o sistema abaixo
# (K/(250s + 1))* retardo de transporte

#Atraso de transporte (para o gráfico) será composto de duas parcelas:
#18 de atraso do sistema + 8 seg até acionar o comando do relé (degrau ter sido dado)

#Agora, utilizaremos do módulo control para fazer os cálculos com funções de transferências, a partir
#dos valores listados acima.

#O método .pade() simula uma determinada função de transferência de ordem a escolher que trará um atraso de transporte
#especificado, por exemplo especificamos o 26.

#o método .tf() gera uma função de transferência a partir do numerador e denominador passados para ele
# funciona com control.tf(num,den) em que num é uma lista e den é outra lista com os coeficientes dos mesmos.

num,den = control.pade(26,3,-2) #utilizamos o comando pade para otermos uma FT que aproxima o atraso de transporte
                                #26 de 26seg de atraso, grau 3 no denominador e grau 1 no numerador.
delay = control.tf(num,den)     #formamos a FT do delay com o numerador e denominador recebido pelo pade
G = control.tf([70.5/(100.0-25.69)],[250,1]) #formamos a FT do sistema normal conforme explicitado acima e no artigo

Gdelay = G*delay #formamos a FT final de simulação multiplicando a FT do sistema pela do delay


#obtemos a resposta ao degrau e armazenamos valores de t e y nas respectivas variaveis
t,y = control.step_response(Gdelay,np.linspace(0,404.53,202)) #passamos o sistema a simular e um vetor de tempo
                                                              #que é composto por um array de 0 a 404.53(ultimo t dos dados coletados)
                                                              #com 202 pontos


#código para plot do grafico
#para o plot da resposta ao degrau deve ser multiplicada e somada do valor inicial
#pq os valores que a simulação retorna partem de 0 e vão para o degrau de valor 1
plt.grid()
plt.plot(t,(y*100)+25.69, '-r', label = 'Resposta ao degrau da FT obtida') #plot da resposta simulada
plt.plot(df['Tempo'],df['Temperatura'], '-b', label = 'Resposta em MA da Planta') #plot dos dados coletados
plt.plot(df['Tempo'],df['Referencia'],'-y', label = 'Temperatura de Referência (degrau)') #plot da referencia
plt.xlabel('Tempo (s)') #legenda do eixo X
plt.ylabel('Temperatura (°C)') #legenda do eixo Y
plt.legend() #legenda o gráfico com o nome de cada curva
plt.show() #mostra o gráfico