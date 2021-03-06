import os
import paramiko
from scp import SCPClient

def createSSHClient(server, port, user, password):
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(server, port, user, password)
    return client

cwd = os.getcwd()#get filepath the script is running from

ssh = createSSHClient('192.168.1.110', 22, 'server', 'password')#createSSHClient(server, port, user, password)
scp = SCPClient(ssh.get_transport())

scp.get("/home/server/Documents/test_file.txt" , cwd)#scp(server file path, current working directory)
