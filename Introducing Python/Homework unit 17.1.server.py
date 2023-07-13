# 17.1 Use a plain socket to implement a current-time-service. When a client sends the
# string time to the server, return the current date and time as an ISO string.
# import socket
# from datetime import datetime
#
# address = ('localhost', 6789)
# max_size = 4096
# print('Starting the server at', datetime.now())
# print('Waiting for a client to call.')
# server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# server.bind(address)
# while True:
#    if server == b'time':
#        data, client = server.recvfrom(max_size)
#        print('Server sent', data)
#        server.sendto(data, client)
#    if server == b'close':
#        data, client = server.recvfrom(max_size)
#        print('Server sent', data)
#        server.sendto(data, client)
#        server.close()
#        break
from datetime import datetime
import socket

address = ('localhost', 6789)
max_size = 4096
print('Starting the server at', datetime.now())
print('Waiting for a client to call.')
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(address)
while True:
    print("wait for a message from a client")
    data, client_addr = server.recvfrom(max_size)
    print("received a message from a client")
    if data == b'time':
        print("request for time")
        now = str(datetime.utcnow())
        data = now.encode('utf-8')
        server.sendto(data, client_addr)
        print('Server sent', data)
        server.close()
