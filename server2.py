#Karthik Natarajan
#1001872904
import socket
import time
import pickle
import os, sys
import shutil
import fcntl
from os.path import exists


HEADERSIZE = 10


#https://pythonprogramming.net/pickle-objects-sockets-tutorial-python-1/
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((socket.gethostname(),3001))
sock.listen(5)
while True:
    # now our endpoint knows about the OTHER endpoint.
    clientsocket, address = sock.accept()
    print(f"Connection from {address} has been established.")
    #https://stackoverflow.com/questions/12831865/python-script-to-get-files-from-one-server-into-another-and-store-them-in-separa
    path = ("./directory_b")
    dirs = os.listdir( path )
    print(dirs)
    dirs.sort()
    for f in dirs:
        fa="./directory_a/"+f
        file_exists = exists(fa)
        if not file_exists :
            fnew="./directory_b/"+f
            #https://www.geeksforgeeks.org/python-move-or-copy-files-and-directories/
            shutil.copy(fnew, './directory_a/')
        else :
            #if locked - dont replace with new file...simply continue loop
            if not(os.access(fa, os.W_OK)):
                flag1="lock"

            # if not locked - replace with directory b
            print("\nFound files with same name '",f,"' in both directories..\nDeleting the older date version....\n")

            fnew="./directory_b/"+f
            modTimeA=os.path.getmtime(fa)
            modTimeB=os.path.getmtime(fnew)
            if modTimeA < modTimeB:
                os.remove(fa)
                shutil.copy(fnew, './directory_a/')


    #https://pythonprogramming.net/pickle-objects-sockets-tutorial-python-3/
    msg1 = pickle.dumps(dirs)
    msg1 = bytes(f"{len(msg1):<{HEADERSIZE}}", 'utf-8')+msg1
    print("going from server2 to server1 after copying files from directory b to a",msg1)
    clientsocket.send(msg1)