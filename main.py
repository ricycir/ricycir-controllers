import serial
import socket
import sys

#Add port
#ser = serial.Serial('', 9600)

#Test write
#ser.write(b'5')

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('kerlin.tech', 5001)

sock.connect(server_address)

try:
  while True:
    data = sock.recv(1024)
    print(data)
    #ser.write(data)

finally:
  print('Closing client')
  sock.close()
