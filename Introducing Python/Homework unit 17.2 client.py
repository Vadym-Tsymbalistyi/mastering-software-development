# 17.2 Use ZeroMQ REQ and REP sockets to do the same thing.
import zmq
from datetime import datetime
from time import sleep

host = '127.0.0.1'
port = 6789
context = zmq.Context()
client = context.socket(zmq.REQ)
client.connect("tcp://%s:%s" % (host, port))
print('Client started at', datetime.utcnow())

request = b'time'
client.send(request)
reply = client.recv()
print("Client received %s" % reply)
sleep(20)

request = b'close'
client.send(request)
reply = client.recv()
print("Client received %s" % reply)
