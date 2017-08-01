import paramiko, threading, sys, time


host = '192.168.121.162'
port = 22
usr = 'root'
pwd = 'qCYnMr@QM6mF3Y7CY7m@'
timeout = 30
 
trans = paramiko.Transport((host, port))
trans.connect(username=usr, password=pwd)
 
chan = trans.open_session()
chan.get_pty()
chan.invoke_shell()
chan.sendall('vmstat 1 5' + '\n')
while True:
    txt = chan.recv_ready()
    if not txt:
        sys.stdout.flush()
        break
    sys.stdout.write(txt)
    sys.stdout.flush()

trans.close()