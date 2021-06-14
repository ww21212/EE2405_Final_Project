import serial
import time
import sys,tty,termios

# XBee setting
serdev = '/dev/ttyUSB0'
s = serial.Serial(serdev, 9600, timeout=3)

print('Start Communication, sending RPC')
send = 'start'
s.write("/xbee_start/run\n".encode())
while send!='stop':
    print('Sent RPC')
    send = s.readline()
    if (send =='circle'):
        # send to remote
        s.write("/circle/run\n".encode())
        '''
        line = s.read(20)
        
        if len(line) < 20:
            print('No response')
        else:
            print(line.decode())
        print('')
        ''' 
    elif (send == 'parking'):
        # send to remote
        s.write("/parking/run 5 5 west\n".encode())


s.close()