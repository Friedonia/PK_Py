import serial

# Functions
def print_commands():
   """Verfügbare befehle"""
   print("Available commands:")
   print("  l - Linke Blende Bewegen /-Links/0Aus/-Rechts")
   print("  r - Rechte Blende Bewegen /-Links/0Aus/-Rechts")
   print("  m - platform Bewegen /-Links/0Aus/-Rechts")
   print("  s - Start Bewegen /anzahl an Offfenen Blenden")
   print("  c - Beenden")


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
   elif command == "c":  # exit program
      print("Exiting program.")
      exit()
   else:  # unknown command
      print("Unknown command '" + command + "'.")
      print_commands()