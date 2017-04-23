import socket


for port in range(1,1024):
   try:
      s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
      socket.settimeout(1000)
      socket.connect(('127.0.0.1',port))
      print('[+] Open Port: ') + port
      socket.close
   except: continue
