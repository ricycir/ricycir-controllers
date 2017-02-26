import serial
import socket
import sys

#Add port
ser = serial.Serial('', 9600)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('kerlin.tech', 5001)

sock.connect(server_address)

try:
  while True:
    data = sock.recv(1024)
    print(data)
    ser.write(byte(data, 'utf-8'))

finally:
  print('Closing client')
  sock.close()

