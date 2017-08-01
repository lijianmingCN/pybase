import xmlrpclib
server = xmlrpclib.ServerProxy ("http://127.0.0.1:8888")
cmdOut = server.cmd ("date")
print cmdOut
