#!/usr/bin/env python3

import errno
import time
import requests
import json
import random
import calendar

from irc_client import *
from datetime import datetime
from socket import error 

def bot_log(txt):
    print("[Bot] {}".format(txt))

server = "localhost"
port = 6667
bot_nick = "manj-gnome"
channel = "#test"

def get_rand_fact(num):
    # Using a random facts API
    url = "http://numbersapi.com/{}".format(num)
    headers = {"Content-Type":"application/json"}
    response_raw = requests.request("GET", url, headers=headers)
    response = response_raw.json()
    return response["text"]

def parse_priv_msg(msg, msg_sender):
    bot.msg(msg_sender,
            get_rand_fact(random.randint(-100,1000)))

def parse_channel_msg(msg, channel):
    if msg[0] != "!":
        bot_log("No Command found, did nothing")
        return

    bot_log("Command "+msg+" on "+channel)
    
    if msg.find("!day") != -1:
        day = calendar.day_name[datetime.today().weekday()]
        bot.msg(channel, day)
    elif msg.find("!time") != -1:
        bot.msg(channel, datetime.now().strftime("%H:%M:%S"))
    else:
        bot.msg(channel, "No such command")

def proc_s_code(s_code):
    if s_code == "433":
        bot_log("Username already taken")
        bot_nick = "{}_".format(bot_nick)
        bot_log("Trying again with {}".format(bot_nick))

        bot.set_nick(bot_nick)
        #exit(1)

bot = IRC_client(server,port,bot_nick,channel)
time.sleep(1)

bot.msg(channel, "Bot ready")
bot_log("READY")

while True:
    time.sleep(0.1)
    try:
        byte_str = bot.isock.recv(512)
        f_msg = byte_str.decode()
        
        if f_msg.find("PING") != -1 :
            bot.pong(f_msg.split(" ")[1])
        else:
            print("[IRC] "+f_msg)
        
            try:
                s_code = f_msg.split(" ")[1]
                proc_s_code(s_code)

                msg_sender = f_msg.split(":")[1].split("!")[0]
                p_command = f_msg.split(" ")[1] #protocol command
                msg_target = f_msg.split(" ")[2] 
                msg = f_msg.split(":")[-1].strip()

                if p_command == "PRIVMSG":
                    if msg_target == bot_nick:
                        parse_priv_msg(msg, msg_sender)
                    elif msg_target == channel:
                        parse_channel_msg(msg, channel)
            except Exception:
                pass

    except error as serr:
        print(len(f_msg))
        if serr.errno != errno.ECONNREFUSED:
            # Not the error we are looking for, re-raise
            raise serr
        # connection refused
        # handle here

