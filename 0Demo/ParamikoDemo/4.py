#!-*-coding:utf8-*-
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

def SSHoutput(channel):
    while True:
        if channel.recv_ready():
            txt = channel.recv(10240)
            print txt
            if not txt:
                sys.stdout.flush()
                break
            sys.stdout.write(txt)
            sys.stdout.flush()


             
t = threading.Thread(target=SSHoutput, args=(chan,))
t.setDaemon(1)
t.start()
time.sleep(0.1)
while True:
    i = raw_input()
    chan.sendall(i + '\n')
    
#trans.close()

