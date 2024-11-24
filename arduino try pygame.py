import serial.tools.list_ports
import time
import cv2

ports = serial.tools.list_ports.comports()
serialInst = serial.Serial()

portsList = []
imagecaptured = 1

for onePort in ports:
    portsList.append(str(onePort))
    print(str(onePort))

serialInst.baudrate = 9600
serialInst.port = "/dev/cu.usbserial-14230"
serialInst.open()
#serialInst.write("2000000,2000000\n".encode('utf-8'))

readlocation = open("newlocation.txt", "r")
readinglines = readlocation.readlines()
preorder = []
for line in readinglines:
    valuea, valueb = line.strip().split(" ")
    preorder.append([int(valuea), int(valueb)])
    #print(int(value1)+int(value2))

#print(preorder)

def captureimage():
    global trials, imagecaptured
    trials = 0
    while trials < 4:
        cap = cv2.VideoCapture(trials)  # 0 for default camera, change if you have multiple cameras
        if not cap.isOpened():
            print("Error: Could not open video device.")
            continue
        ret, frame = cap.read()
        if not ret:
            print("Error: Could not read frame.")
            cap.release()
            continue
        cv2.imshow('Captured Frame', frame)
        cv2.waitKey(1)
        name = 'image' + str(imagecaptured) + str(trials) + '.jpg'
        cv2.imwrite('data/' + name, frame)
        cap.release()
        cv2.destroyAllWindows()
        trials = trials + 1
        print(trials)
    trials = 0
    imagecaptured = imagecaptured + 1

while True:
    '''if serialInst.in_waiting:
        packet = serialInst.readline()
        print("coords recieved : "+str(packet.decode('utf').rstrip('\n')))
        coords = packet.decode('utf').rstrip('\n')
        coordx, coordy, coordz = coords.split()'''
    for i in preorder:
        # ready = input("ready or not : ")
        input("ready : ")
        # values = input("x axis and y axis with space between : ")
        value1, value2 = ((i[0]/2)*10), (((254-i[1])/2)*10)
        if serialInst.in_waiting:
            packet = serialInst.readline()
            print("coords actuator now : " + str(packet.decode('utf').rstrip('\n')))
            coords = packet.decode('utf').rstrip('\n')
            coordx, coordy, coordz = coords.split()
        # print(int(coordx)+int(coordy))
        xtravel = int(value1) - int(coordx)
        ytravel = int(value2) - int(coordy)
        # xtravel = int(value1)
        # ytravel = int(value2)
        values = str(xtravel) + " " + str(ytravel)
        print("destination : " + str(value1) + " " + str(value2) + "\n")
        print("travel distance now : " + str(values))

        serialInst.write(values.encode('utf-8'))

        input("capture : ")
        captureimage()
    break

