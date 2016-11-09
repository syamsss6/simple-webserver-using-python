#!/usr/bin/python
import socket,os,sys

ROOT = os.getcwd()

listen_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
listen_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
listen_socket.bind(('localhost',8000))
listen_socket.listen(1)

print("listening on port 8000")

def create_child():
 while True:
  try:
   res = os.waitpid(-1,os.WNOHANG)
   if not result[0]:
     break
  except:
    break

while True:
	clientsock,clientaddr = listen_socket.accept()
	create_child()
	
        pid = os.fork()
	if pid:
	  clientsock.close()
 	  continue
 	else:
           listen_socket.close()
  	   request = clientsock.recv(5120)
           print request.split("\n")[0]

           buff = request.split()[1]
           PATH = ROOT + buff

           try:
 
              fp = open(PATH,'r')
              data = fp.read()
              
              clientsock.sendall(data)
              fp.close()
           except:
                  pass


           clientsock.close()
           sys.exit(0) 

  
