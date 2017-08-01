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
 
def func(channel, f):
     while True:
         txt = channel.recv(256)
         if not txt:
             f.flush()
             break
         f.write(txt)
         f.flush()
 
def cmd(cmd_str):
     chan.sendall(cmd_str + '\n')
     time.sleep(timeout)
     
t = threading.Thread(target=func, args=(chan, sys.stdout))
t.setDaemon(1)
t.start()
 
cmd('vmstat 1 2')
trans.close()
