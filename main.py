#!/usr/bin/env python3

import time
from irc_client import *

import errno
from socket import error as socket_error


bot = IRC_client("localhost",6667, "pyBot" ,"#test")
time.sleep(1)

bot.msg("#test", "hello")

while True:
    time.sleep(0.1)
    try:
        byte_str = bot.isock.recv(1024)
        msg = byte_str.decode()
        sender_uname = msg.split(":")[1].split("!")[0]
        print(msg)

        if msg.find("PING") != -1 :
            bot.pong(msg.split(" ")[1])
            #print("pong")

        if msg.find(":@hi") != -1 :
            bot.msg(sender_uname,"hello")

    except socket_error as serr:
        if serr.errno != errno.ECONNREFUSED:
            # Not the error we are looking for, re-raise
            raise serr
        # connection refused
        # handle here
