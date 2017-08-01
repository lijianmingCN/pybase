import SimpleXMLRPCServer
import os
import subprocess
class XMLServer:
    def cmd (self,s ) :
        st = subprocess.Popen (s,stdout=subprocess.PIPE, shell=True)
        return st.stdout.read()
xso = XMLServer ()
server = SimpleXMLRPCServer.SimpleXMLRPCServer(("",8888),allow_none=True)
server.register_instance (xso) 
print " Listening on port 8888"
server.serve_forever()
