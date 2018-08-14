import serial
import time

ser = serial.Serial("/dev/ttyAMA0", 9600, timeout=1.0)

#for count in range(4)
#count = 0
#while count <= 4 :
linhalida = ser.readline()#para receber dados da serial
print (linhalida)
print ('Porta:', ser.name)
#ser.write(linhaescrita)#para escrever dados
#    if count < 3: break
#codigo para receber os dados que o gps exibe
