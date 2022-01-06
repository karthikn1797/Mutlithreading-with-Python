#Karthik Natarajan
#1001872904
import socket
import fcntl
import pickle
import os, time
import sys
from stat import S_IREAD


HEADERSIZE = 10

#https://pythonprogramming.net/pickle-objects-sockets-tutorial-python-1/
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((socket.gethostname(), 3000))



while True:
    full_msg = b''
    new_msg = True
    while True:
        msg = sock.recv(16)
		#https://pythonprogramming.net/pickle-objects-sockets-tutorial-python-3/
        if new_msg:
            print("new msg len:",msg[:HEADERSIZE])
            msglen = int(msg[:HEADERSIZE])
            new_msg = False

        print(f"full message length: {msglen}")

        full_msg += msg

        print(len(full_msg))

        if len(full_msg)-HEADERSIZE == msglen:
            print("full msg recieved")
            print(full_msg[HEADERSIZE:])
            print("\n")
            #https://stackoverflow.com/questions/237079/how-to-get-file-creation-modification-date-times-in-python
            path = (r"./directory_a")
            dirs = os.listdir(path )
            dirs.sort()
            for each in dirs:
                mypath= "./directory_a/"+each
                (mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime) = os.stat( path = mypath )
                print("\n",dirs.index(each)," ",each,    f"{os.path.getsize(mypath)/float(1<<7):,.0f}Kb  ", "Modified@:",time.ctime(mtime), ", Locked = ", not(os.access(mypath, os.W_OK)))
            new_msg = True
            full_msg = b''


