import serial

#Add port
ser = serial.Serial('', 9600)

#Test input
ser.write(b'5')
