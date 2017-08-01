import paramiko

class SSHTool:
    def __init__(self,hostname,username,password):
        self.hostname = hostname
        self.username = username
        self.password = password
    def setLog(self,logPath):
        if(logPath):
            paramiko.util.log_to_file(logPath)
    def runCmd(self,cmd):
        self.client = paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.client.connect(hostname=self.hostname,username=self.username,password=self.password)
        stdin,stdout,stderr = self.client.exec_command(cmd)
        return stdin,stdout,stderr
    def runAlways(self,cmd):
        post=22
        trans = paramiko.Transport((host, port))
        trans.connect(username=usr, password=pwd)
         
        chan = trans.open_session()
        chan.get_pty()
        chan.invoke_shell()        
        
        
    def close(self):
        self.client.close()
        
ssh = SSHTool('192.168.121.162','root','qCYnMr@QM6mF3Y7CY7m@')
ssh.setLog('sys.log')
stdin,stdout,stderr = ssh.run('free -m')
print stdout.read()
ssh.close()



