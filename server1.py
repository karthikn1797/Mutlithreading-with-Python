#Karthik Natarajan
#1001872904
import socket
import time
import pickle
import os, sys
import stat

HEADERSIZE = 10
#https://pythonprogramming.net/pickle-objects-sockets-tutorial-python-1/
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((socket.gethostname(), 3001))

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((socket.gethostname(),3000))
sock.listen(5)

flag=0
if len(sys.argv)>1:
    if sys.argv[1]=="-lock":
        flag=1
    if sys.argv[1]=="-unlock":
        flag=2



while True:
    # now our endpoint knows about the OTHER endpoint.
    clientsocket, address = sock.accept()
    print(f"Connection from {address} has been established.")
    path = (r"./directory_a")
    dirs = os.listdir(path)

    #https://pythonprogramming.net/pickle-objects-sockets-tutorial-python-3/
    msg = pickle.dumps(dirs)
    msg = bytes(f"{len(msg):<{HEADERSIZE}}", 'utf-8')+msg

    clientsocket.send(msg)

    dirs.sort()
    if flag==1:
        for index in range(len(dirs)):
            if str(index) in sys.argv[2]:
                filepath=path+"/"+dirs[index]
                print("Locking file at index",index," : ",filepath)
                os.chmod(filepath, stat.S_IRUSR)

    elif flag==2:
        for index in range(len(dirs)):
            if str(index) in sys.argv[2]:
                filepath=path+"/"+dirs[index]
                print("Unlocking file at index",index," : ",filepath)
                os.chmod(filepath, 0o777)


