import serial
#initialize serial connection 

def cks(buffer):
    ck_a =0
    ck_b =0
    
    for data in buffer:
        ck_a = (ck_a + data)& 0xFF
        ck_b = (ck_b + ck_a)& 0xFF
    
    return [ck_a, ck_b]

def pckg(clas, id, length, payload):
    
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
    
    return Temp

def NullPayload(length):
    temp = []
    for data in range(length):
        temp.append(0)
    return temp
#def serialinit(pack):
pack = pckg(0x06, 0x01, 3, [240, 0, 0])
pack_2 = pckg(0x06, 0x17, 4, NullPayload(4))

ser = serial.Serial("/dev/ttyAMA0", 9600, timeout=0.250)

if ser.isOpen():
    print ('serial comunicando, porta usada:' + ser.portstr + '\n')#confirma a porta usada

ser.write(pack)
lido = ser.read(255)
print('package:',pack,'\n')
print('data send to gps:',ser.write(pack), '\n' )
print('data recived from gps:', lido, '\n')
    
