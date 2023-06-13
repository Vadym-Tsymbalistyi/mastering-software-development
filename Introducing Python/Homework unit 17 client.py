# 17.1 Use a plain socket to implement a current-time-service. When a client sends the
# string time to the server, return the current date and time as an ISO string.
import socket
from datetime import datetime

address = ('localhost', 6789)
max_size = 4096
print('Starting the client at', datetime.now())
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.sendto(b'time', address)
data, server = client.recvfrom(max_size)
print('Client read', data)
client.close()
# 17.2 Use ZeroMQ REQ and REP sockets to do the same thing.
import zmq
from datetime import datetime

host = '127.0.0.1'
port = 6789
context = zmq.Context()
socket = context.socket(zmq.REQ)
server.bind("tcp://%S%S" % (host, port))
print('Starting the server at', datetime.utcnow())
while True:
    request_string = socket.recv_string()
    response_bytes = request_string.encode('utf-8')
    client.sendto(response_bytes)
    reply_bytes = client.recv()
    reply_string = reply_bytes.decode('utf-8')
    print('Server read', data)
    client.close()

# 17.3 Try the same with XMLRPC.
import xmlrpc.client

proxi = xmlrpc.client.ServerProxy('http://localhost:6789/')
now = 5
result = proxi.double(now)
print(now, result)

# 17.4 You may have seen the classic I Love Lucy television episode in which Lucy and
# Ethel worked in a chocolate factory. The duo fell behind as the conveyor belt that
# supplied the confections for them to process began operating at an ever-faster rate.
# Write a simulation that pushes different types of chocolates to a Redis list, and Lucy is
# a client doing blocking pops of this list. She needs 0.5 seconds to handle a piece of
# chocolate. Print the time and type of each chocolate as Lucy gets it, and how many
# remain to be handled.
import redis
import time
import random

r = redis.Redis(host='localhost', port=6379, db=0)
print('Starting the client at', datetime.utcnow())

# 17.5 Use ZeroMQ to publish the poem from exercise 12.4 (from Example 12-1), one
# word at a time. Write a ZeroMQ consumer that prints every word that starts with a
# vowel, and another that prints every word that contains five letters. Ignore punctuation
# characters.
