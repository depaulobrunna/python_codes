import serial #initialize serial connection
import sys

#SERIAL CONFIG
porta = "com14"#mudanca de porta

def serialwrite(data):
    ser = serial.Serial(porta, 9600, timeout=0.20)
    
    if ser.isOpen():
        print ('\n'+ 'serial working, port:' + ser.portstr + '\n')#confirma a porta usada
    while True:
        print('package:',data,'\n')
        print('data send to gps:',ser.write(data), '\n' )
        lido = ser.read(255)
        print(lido)
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

def payloadconstr(size, content):
    payload = []
    for data in range(size):
        payload.append(0)
    for i in range(size-1):
        payload[i] = content[i]
    return payload

def pckg(clas, id, length, payload,serial):
    '''func para montar os pacotes e envialos para serial'''
    payload = payloadconstr(length, payload)
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
    print('\n', 'payload:', payload)
    if serial == 1:
        Vartemp =  Temp
        lido = serialwrite(Vartemp)
    return lido

#define rate como zero
gga = pckg(0x06, 0x01, 3, (0xF0, 0x00, 0), 1)#GGA
ggl = pckg(0x06, 0x01, 3, (0xF0, 0x01, 0), 1)#GGL
gsa = pckg(0x06, 0x01, 3, (0xF0, 0x02, 0), 1)#GSA
gsv = pckg(0x06, 0x01, 3, (0xF0, 0x03, 0), 1)#GSV
rmc = pckg(0x06, 0x01, 3, (0xF0, 0x04, 0), 1)#RMC
txt = pckg(0x06, 0x01, 3, (0xF0, 0x05, 0), 1)#TXT
vtg = pckg(0x06, 0x01, 3, (0xF0, 0x41, 0), 1)#VTG

#pckg(0x06, 0x09, 0x0C,(0,0,0,0,2,0,0,0,0,0,0,0), 1)
#serialwrite([0xB5, 0x62, 0x06, 0x09, 0x0D, 0x00, 0x00, 0x00, 0x00, 0x00, 0x02, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x20, 0xCD])
#pckg(0x06, 0x09, 12,(0,0,8), 1)
#serialwrite([0xB5, 0x62, 0x06, 0x09, 0x0D, 0x00, 0x00, 0x00, 0x00, 0x00, 0xFF, 0xFF, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x03, 0x1D, 0xAB])
s = pckg(0x06, 0x04, 4,(0,0,0x08),1)
sm = pckg(0x09, 0x14, 4,(0,0,0,0), 1)
