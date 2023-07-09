
#import serial
import csv
#ser = serial.Serial("COM5",9600)
import serial
import time
#import csv

f = open("data03_07_P50_I0-005_T80.csv", "w")
f.truncate()

ser = serial.Serial('COM5', 9600)

#reinicia o arduino
ser.setDTR(False)
time.sleep(1)
ser.flushInput()
ser.setDTR(True)

samples = 8000


for k in range(samples):
    s_bytes = ser.readline()
    dados = s_bytes.decode("utf-8").strip('\r\n')
    print(dados)
    f.write(dados + "\n")
    #time.sleep(0.5)
            
print("Coleta de dados finalizada")
f.close()
        
    
