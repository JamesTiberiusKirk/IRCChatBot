#!/usr/bin/env python3

import sys
import time
import socket

server = "localhost"
botnick = "python_script"
channel = "%23test"

# Establish connection

irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
irc.connect((server, 6667))
irc.setblocking(False)
time.sleep(1)

message = "USER "+botnick+" "+botnick+" " + botnick+" :Hello! I am a test bot!\r\n"
irc.send(message.encode())

time.sleep(1)
message = "NICK pyBot\n" 
irc.send(message.encode())
time.sleep(1)
message = "JOIN #test\n"
irc.send(message.encode())


"""
while 1:
    time.sleep(0.1)
    text = ""
    try:
        text = irc.recv(2040)
        strtxt = text.decode()
        print(strtxt)
        print(strtxt.find("PING"))
        if strtxt.find("PING") != 0:
            message = "PONG "+strtxt.split()[1]+"\r\n"
            print("if: "+message)
            irc.send(message.encode())
        
        if strtxt.lower().find(":@hi") != -1:
            message = "PRIVMSG "+channel+" :Hello!\r\n"
            print(message)
            irc.send(message.encode())
            text = ""
    except Exception as e:
        print(e)
"""
input()
