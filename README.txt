

Language : Python(version3)

Execution steps :

1. Open 3 terminals , change directory to this folder (lab2_natarajan_kxn2904)

2. First terminal command : python3 server2.py and immediately do step 3 before any output in server2 

3. Second terminal command : python3 server1.py

4. Third terminal command : python3 client.py

5. Clear all terminals again and follow step 1 & 2.
   Next, in the second terminal window, type the command: python3 server1.py -lock -<index>
   Finally, in the third terminal, type the command: python3 client.py

6. Now, to unlock the file, we follow steps 1 and 2 again. 
   And then, in the second window, type the following command: python3 server1.py -unlock -<index>
   Now, finally type the folllowing command in the third window: python3 client.py

7. Finally, follow steps 1 through 3 to obtain the desired output 

Note: If " File "/Users/karthiknatarajan/De/sktop/distributed lab2/lab2_natarajan_kxn2904/server1.py",       line 15, in <module>.                      sock.bind((socket.gethostname(),3000))
OSError: [Errno 48] Address already in use, then restart all the three terminal windows and follow the steps again.
PS: you might have to do it twice if it doesn't work the first time.
Thank you.
