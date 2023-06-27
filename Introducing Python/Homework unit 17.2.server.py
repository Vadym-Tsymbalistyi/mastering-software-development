# 17.2 Use ZeroMQ REQ and REP sockets to do the same thing.
import zmq
from datetime import datetime

host = '127.0.0.1'
port = 6789
context = zmq.Context()
server = context.socket(zmq.REP)
server.bind("tcp://%s:%s" % (host, port))
print('Server started at', datetime.utcnow())
while True:
    print("wait for a message from a client")
    message = server.recv()
    print("received a message from a client")
    if message == b'time':
        print("request for time")
        now = datetime.utcnow()
        reply = str(now)
        server.send(bytes(reply, 'utf-8'))
        print('Server sent', reply)
    if message == b'close':
        print("request for closing")
        reply = "OK"
        server.send(bytes(reply, 'utf-8'))
        server.close()
        print('Server is closed')
        break
