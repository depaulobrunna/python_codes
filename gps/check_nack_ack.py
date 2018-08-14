import serial #initialize serial connection
import sys

#SERIAL CONFIG
porta = "com13"#mudanca de porta



def serialwrite(data):
    ser = serial.Serial(porta, 9600, timeout=0.20)
    
    if ser.isOpen():
        print ('\n'+ 'serial working, port:' + ser.portstr + '\n')#confirma a porta usada
    while True:
        print('package:',data,'\n')
        print('data send to gps:',ser.write(data), '\n' )
        lido = ser.read(255)
        break
    return lido
#GPS CONFIG
        
def NullPayload(size):
    '''func para payload = 0'''
    temp = []
    for data in range(size):
        temp.append(0)
    return temp


def cks(buffer):
    '''calculo de checksum'''
    ck_a =0
    ck_b =0
    
    for data in buffer:
        ck_a = (ck_a + data)& 0xFF
        ck_b = (ck_b + ck_a)& 0xFF
    
    return [ck_a, ck_b]

def pckg(clas, id, length, payload):
    '''func para montar os pacotes e envialos para serial'''
    if payload == 0:
        payload = NullPayload(length)
        temp = [clas, id, length&0x00FF, (length&0xFF00)>>8]
        for data in payload:
            temp.append(data)
        [ck_a, ck_b] = cks(temp)
        Temp = [0xB5, 0x62]
        Temp.append(clas)
        Temp.append(id)
        Temp.append(length&0x00FF)
        Temp.append((length&0xFF00)>>8)
        for data in payload:
            Temp.append(data)
        Temp.append(ck_a)
        Temp.append(ck_b)
        
        print('\n Pacote montado:', Temp)
        print('\n', 'payload:', payload, '\n nulo \n')
        Vartemp =  Temp
        serialwrite(Vartemp)
        return serialwrite(Vartemp)
    else:
        temp = [clas, id, length&0x00FF, (length&0xFF00)>>8]
        for data in payload:
            temp.append(data)
        [ck_a, ck_b] = cks(temp)
        Temp = [0xB5, 0x62]
        Temp.append(clas)
        Temp.append(id)
        Temp.append(length&0x00FF)
        Temp.append((length&0xFF00)>>8)
        for data in payload:
            Temp.append(data)
        Temp.append(ck_a)
        Temp.append(ck_b)
        
        print('\n Pacote montado:', Temp)
        print('\n', 'payload:', payload, '\n nao nulo \n')
        Vartemp =  Temp
        serialwrite(Vartemp)
        

def checkpckg(clas, id, length, payload):
    
    
    package = pckg(clas, id, length, payload)
    print (package)
    sizepack = len(package)
    
    i=0
    while i < sizepack:#while para usar a funcao break
        check = package[i]
        if(package[0]==181):
            print ('header 1 is ok', package[0], '\n')
        else:
            print('error header 1 =', package[0], '\n')
            break
        
        if(package[1]==98):
            print ('header 2 is ok', package[1], '\n')
        else:
            print('error header 2 =', package[1], '\n')
            break
        
        if(package[2]==0x05):
            print ('ack-nack class\n')
        else:
            print('error ack-nack class\n')
            break
        
        if(package[3]==0x01):
            print ('ack\n')
            break
        else:
            print('nack\n')
            break
