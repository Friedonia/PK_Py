#last change 17.6.2023 by Frieder Schmidt
import serial
import time
from START import *;

sleepTim = 10
blendeInfo = 0
lastState = False
count = 0

# Functions
def print_commands():
    """Verfügbare befehle"""
    print("Available commands:")
    print("  l - Linke Blende Bewegen /-Links/0Aus/-Rechts")
    print("  r - Rechte Blende Bewegen /-Links/0Aus/-Rechts")
    print("  m - platform Bewegen /-Links/0Aus/-Rechts")
    print("  s - Start Bewegen /anzahl an Offfenen Blenden")
    print("  c - Beenden")

def restPlatform():
    while(open("platformGrad.txt", "r") != "0"):
        usb.write(b'm-')
        time.sleep(sleepTim)
        line = usb.readline()  # read input from Arduino
        line = line.decode()  # convert type from bytes to string
        line = line.strip()
        lineArray = line.split("/")
        f = open("platformGrad.txt", "w")
        f.write(lineArray[1])
        f.close()
# Main

# Connect to USB serial port at 9600 baud
try:
    usb = serial.Serial(USB_PORT, 9600, timeout=2)
except:
    print("ERROR - Could not open USB serial port.  Please check your port name and permissions.")
    print("Exiting program.")
    exit()

# Send commands to Arduino
print("Enter a command from the keyboard to send to the Arduino.")
print_commands()
while True:
    command = input("Enter command: ")
   
    if command[0] == "l":  # linke blende
        send = ''+command[0] + command[1]
        usb.write(b''+send+'')  # send command to Arduino
        
    elif command == "r":  # rechte blende
        send = ''+command[0] + command[1]
        usb.write(b''+send+'')  # send command to Arduino
    elif command == "m":  # dreht die mitte
        send = ''+command[0] + command[1]
        usb.write(b''+send+'')  # send command to Arduino
    elif command == "s":  # Start der seq
       send = ''+command[0] + command[1]
       usb.write(b''+send+'')  # send command to Arduino
    elif isRuning():
        #Reset motor
        if(blendeInfo != getBlende()):
            if(getBlende() < blendeInfo):
                usb.write(b'l+')
                time.sleep(sleepTim)
                usb.write(b'r-')
            elif(getBlende() > blendeInfo):
                usb.write(b'l+')
                time.sleep(sleepTim)
                usb.write(b'r-')
        # start Motor
    elif command == "c":  # exit program
        print("Exiting program.")
        exit()
    else:  # unknown command
        print("Unknown command '" + command + "'.")
        print_commands()



    # command from website 
    line = usb.readline()  # read input from Arduino
    line = line.decode()  # convert type from bytes to string
    line = line.strip()

    lineArray = line.split("/")

    f = open("platformGrad.txt", "w")
    f.write(lineArray[1])
    f.close()

    if(lastState and isRuning()):
        if(open("platformGrad.txt", "r") != "360"):
            usb.write(b'm+')
            time.sleep(sleepTim)

        f = open("ultraschallsensor.txt", "a")
        f.write(""+ count +", "+lineArray[0]+"\n")
        f.close()
        count +=1
    elif((not lastState) and (isRuning())):
        
        restPlatform()

        f = open("ultraschallsensor.txt", "w")
        f.write(""+ count +", "+lineArray[0]+"\n")
        f.close()
        count = 0
        setRuning()

    
    lastState = isRuning()
    

