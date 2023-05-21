
import csv
import serial
import time

portaSerial = 'COM5'   #variável com a porta Serial utilizada para comunicar com o Arduino
baudRate = 9600        #variável com o valor do Baud Rate da comunicação serial

f = open("Arquivo_com_dadosColetados.csv", "w") #variavel para abrir o arquivo csv com nome desejado
f.truncate()

ser = serial.Serial(portaSerial, baudRate) #objeto que terá a comunicação serial com o Arduino

#Parte do código para reiniciar o Arduino
ser.setDTR(False)
time.sleep(1)
ser.flushInput()
ser.setDTR(True)

samples = 6000    #números de amostras a coletar (número ficticio alto somente para o código rodar, 
                  #na realidade ao querermos encerrar nós damos 'stop' no código)


#Loop For que faz coleta dos dados da comunicação serial, decodifica, printa na tela e armazena no arquivo .csv
for k in range(samples):
    s_bytes = ser.readline()
    dados = s_bytes.decode("utf-8").strip('\r\n')
    print(dados)
    f.write(dados + "\n")
            
print("Coleta de dados finalizada") #imprime que a coleta dos dados foi finalizada
f.close()                           #fecha o arquivo csv
        
    
