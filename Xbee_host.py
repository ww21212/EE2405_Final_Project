import serial
import time
import sys,tty,termios

# XBee setting
serdev = '/dev/ttyUSB0'
s = serial.Serial(serdev, 9600, timeout=3)

class _Getch:
    def __call__(self):
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

def get():
    inkey = _Getch()
    while(1):
        k=inkey()
        if k!='':break
    if k=='\x1b':
        k2 = inkey()
        k3 = inkey()
        if k3=='A':
            print ("up")
            s.write("/CT/run 100 \n".encode())
        if k3=='B':
            print ("down")
            s.write("/CT/run -100 \n".encode())
        if k3=='C':
            print ("right")
            s.write("/turn/run 100 -0.1 \n".encode())
        if k3=='D':
            print ("left")
            s.write("/turn/run 100 0.1 \n".encode())
        time.sleep(1)
        s.write("/stop/run \n".encode())
    elif k=='1':
        print ("parking area: 1")         # parking area 1
        k4 = input()
        if k4 == 'N':   # North
            print("direction: N")
            k5 = input()
            d1 = float(k5)
            k6 = input()
            d2 = float(k6)
            print_args = ("/car/run 1 0", d1, d2)
            s.write(("%s %f %f \n" % print_args).encode())
        elif k4 == 'NE':    # NorthEast
            print("direction: NE")
            k5 = input()
            d1 = float(k5)
            k6 = input()
            d2 = float(k6)
            print_args = ("/car/run 1 1", d1, d2)
            s.write(("%s %f %f \n" % print_args).encode())
        elif k4 == 'E':     # East
            print("direction: E")
            k5 = input()
            d1 = float(k5)
            k6 = input()
            d2 = float(k6)
            print_args = ("/car/run 1 2", d1, d2)
            s.write(("%s %f %f \n" % print_args).encode())
        elif k4 == 'SE':    # SouthEast
            print("direction: SE")
            k5 = input()
            d1 = float(k5)
            k6 = input()
            d2 = float(k6)
            print_args = ("/car/run 1 3", d1, d2)
            s.write(("%s %f %f \n" % print_args).encode())
        elif k4 == 'S':     # South
            print("direction: S")
            k5 = input()
            d1 = float(k5)
            k6 = input()
            d2 = float(k6)
            print_args = ("/car/run 1 4", d1, d2)
            s.write(("%s %f %f \n" % print_args).encode())
        elif k4 == 'SW':    # SouthWest
            print("direction: SW")
            k5 = input()
            d1 = float(k5)
            k6 = input()
            d2 = float(k6)
            print_args = ("/car/run 1 5", d1, d2)
            s.write(("%s %f %f \n" % print_args).encode())
        elif k4 == 'W':     # West
            print("direction: W")
            k5 = input()
            d1 = float(k5)
            k6 = input()
            d2 = float(k6)
            print_args = ("/car/run 1 6", d1, d2)
            s.write(("%s %f %f \n" % print_args).encode())
        elif k4 == 'NW':    # NorthWest
            print("direction: NW")
            k5 = input()
            d1 = float(k5)
            k6 = input()
            d2 = float(k6)
            print_args = ("/car/run 1 7", d1, d2)
            s.write(("%s %f %f \n" % print_args).encode())
    elif k=='2':
        print ("parking area: 2")
        k4 = input()
        if k4 == 'N':
            print("direction: N")
            k5 = input()
            d1 = float(k5)
            k6 = input()
            d2 = float(k6)
            print_args = ("/car/run 2 0", d1, d2)
            s.write(("%s %f %f \n" % print_args).encode())
        elif k4 == 'NE':
            print("direction: NE")
            k5 = input()
            d1 = float(k5)
            k6 = input()
            d2 = float(k6)
            print_args = ("/car/run 2 1", d1, d2)
            s.write(("%s %f %f \n" % print_args).encode())
        elif k4 == 'E':
            print("direction: E")
            k5 = input()
            d1 = float(k5)
            k6 = input()
            d2 = float(k6)
            print_args = ("/car/run 2 2", d1, d2)
            s.write(("%s %f %f \n" % print_args).encode())
        elif k4 == 'SE':
            print("direction: SE")
            k5 = input()
            d1 = float(k5)
            k6 = input()
            d2 = float(k6)
            print_args = ("/car/run 2 3", d1, d2)
            s.write(("%s %f %f \n" % print_args).encode())
        elif k4 == 'S':
            print("direction: S")
            k5 = input()
            d1 = float(k5)
            k6 = input()
            d2 = float(k6)
            print_args = ("/car/run 2 4", d1, d2)
            s.write(("%s %f %f \n" % print_args).encode())
        elif k4 == 'SW':
            print("direction: SW")
            k5 = input()
            d1 = float(k5)
            k6 = input()
            d2 = float(k6)
            print_args = ("/car/run 2 5", d1, d2)
            s.write(("%s %f %f \n" % print_args).encode())
        elif k4 == 'W':
            print("direction: W")
            k5 = input()
            d1 = float(k5)
            k6 = input()
            d2 = float(k6)
            print_args = ("/car/run 2 6", d1, d2)
            s.write(("%s %f %f \n" % print_args).encode())
        elif k4 == 'NW':
            print("direction: NW")
            k5 = input()
            d1 = float(k5)
            k6 = input()
            d2 = float(k6)
            print_args = ("/car/run 2 7", d1, d2)
            s.write(("%s %f %f \n" % print_args).encode())
    elif k=='q':
        print ("quit")
        return 0
    else:
        print ("not an arrow key!")
    return 1

print('Start Communication, sending RPC')
send = 'start'
print(send)
s.write("/xbee_start/run\n".encode())

while send!='stop':
    #print('Sent RPC')
    send = s.readline()
    print(send)
    if (send == b'circle'):
        # send to remote
        s.write("/circle/run\n".encode())
    elif (send == b'parking'):
        # send to remote
        while get():
            i = 0
        s.write("/parking/run 5 5 west\n".encode())
s.close()