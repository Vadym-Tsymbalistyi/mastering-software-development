# 17.1 Use a plain socket to implement a current-time-service. When a client sends the
# string time to the server, return the current date and time as an ISO string.
import socket
from datetime import datetime

address = ('localhost', 6789)
max_size = 4096
print('Starting the server at', datetime.now())
print('Waiting for a client to call.')
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(address)
data, client = server.recvfrom(max_size)
print('Server sent', data)
server.sendto(data, client)
server.close()
