# EE2405_Final_Project

(1) how to setup and run your program

1. Preparation
    1. Compile main.py in OpenMV
    2. Connecte OpenMV to B_L4S5I_IOT01A
    3. Compile B_L4S5I_IOT01A
    4. Put the car on a line
2. Demo
    1. line detection
        1. Use Xbee to send a commend:

                /xbee_start/run
            to BBcar

        2. After getting the RPC call, BBcar use Uart to send a command "line" to OpenMV
        3. After getting the command: OpenMV send a RPC call:

                /line_det/run x1 y1 x2 y2
            to BBcar
        4. BBcar execute line detection function

    2. Circle around two objects
        1. After BBcar stops line detection, ping send the distance to BBcar and BBcar use Xbee to send a command "circle" to Xbee connected to computer.
        2. Xbee connected computer send a RPC call:

                /circle/run
            to BBcar.
        3. BBcar circle around a object clockwise, then circle around another object counterclockwise.
        4. After finishing circle, BBcar use Xbee send a command "parking" to Xbee connected to the computer.
    3. Parking
        1. After Xbee connected to the computer gets a command "parking", it will go into a function get() to get my command: parking area, direction, D1, D2 by using the RPC call:
        
                /car/run area direction D1 D2
        2. BBcar will go into the parking space.
        3. BBcar parks correctly.
        4. BBcar send a command "calib" to OpenMV by using Uart.
        6. BBcar send a command "stop" to Xbee connected to the computer to stop Xbee_host.py.
    4. Apriltag
        1. After OpenMV get the command "calib", it will open its apriltag function and send a RPC call:

                /calib/run Disx Disy Disz Rx Ry Rz
            to the BBcar by using Uart.                
        2. BBcar get the information from OpenMV, then go to the region in front of Apriltag.
        
(2) what are the results

Video link:

    https://drive.google.com/drive/u/3/folders/1yYIzKmUaVb33P_wTyUtbAUQ06JZaiMAL
