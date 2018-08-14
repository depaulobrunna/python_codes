import serial
#initialize serial connection 
ser = serial.Serial("com3", 9600, timeout=0.100)

if ser.isOpen():
    print ('serial comunicando, porta usada:' + ser.portstr)#confirma a porta usada

ser.write(b'cabrinhas')
lido = ser.read(255)#
print(lido)