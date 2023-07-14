# 17.3 Try the same with XMLRPC.
from xmlrpc.server import SimpleXMLRPCServer


def now():
    from datetime import datetime
    data = str(datetime.utcnow())
    print('Server sent', data)
    return data


server = SimpleXMLRPCServer(("localhost", 6789))
server.register_function(now, "now")
server.serve_forever()
