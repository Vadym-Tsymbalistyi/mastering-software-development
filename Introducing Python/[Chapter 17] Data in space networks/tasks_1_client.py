# 17.1 Use a plain socket to implement a current-time-service. When a client sends the
# string time to the server, return the current date and time as an ISO string.
import socket
from datetime import datetime
from time import sleep

address = ('localhost', 6789)
max_size = 4096
print('Starting the client at', datetime.now())
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

client.sendto(b'time', address)
data, server_addr = client.recvfrom(max_size)
print('Client read', data)

sleep(20)

client.sendto(b'close', address)
data, server_address = client.recvfrom(max_size)
print('Client read', data)
