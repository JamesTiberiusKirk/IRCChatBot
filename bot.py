#!/usr/bin/env python3

import errno
import time
import requests # Used to get random facts 
import json
import random
import calendar
import sys

from irc_client import IRC_client
from datetime import datetime
from socket import error 

def bot_log(txt):
    print("[BOT] {}".format(txt))

def get_rand_fact(num):
    # Using a numbers facts API
    url = "http://numbersapi.com/{}".format(num)
    headers = {"Content-Type":"application/json"}
    response_raw = requests.request("GET", url, headers=headers)
    response = response_raw.json()
    return response["text"]

def parse_priv_msg(msg, msg_sender):
    # Genecating a random number for get_rand_facts() and sending it
    bot.msg(msg_sender,
            get_rand_fact(random.randint(-100,1000)))

def parse_channel_msg(msg, channel):
    # If the message does not contain a command
    if msg[0] != "!":
        bot_log("No Command found, did nothing")
        return

    bot_log("Command "+msg+" on "+channel)
    
    # If the command is !day
    if msg.find("!day") != -1:
        day = calendar.day_name[datetime.today().weekday()]
        bot.msg(channel, day)
    
    # If the command is !time
    elif msg.find("!time") != -1:
        bot.msg(channel, datetime.now().strftime("%H:%M:%S"))
    
    # In case it is not a listed command
    else:
        bot.msg(channel, "No such command")

def proc_s_code(s_code):
    if s_code == "433":
        bot_log("Username already taken")
        bot_log("Exiting...") 
        bot.isock.close()
        exit(1)

# Default values for theconnection
server = "10.0.42.17"
# server = "localhost"
port = 6667
bot_nick = "pyBot"
channel = "#test"

# Parcing sys.argv 
try:
    # Help message
    if sys.argv[1] == "-h":
        print("[Usage] ./bot.py <server> <port> <bot_nick> <channel with no '#'>")
        exit(0)
    
    # Seeting other variables if they exist
    server = sys.argv[1]
    port = int(sys.argv[2])
    bot_nick = sys.argv[3]
    channel = "#{}".format(sys.argv[4])
except Exception:
    pass

print("[CONN] server:{0}:{1}".format(server,port))
print("[CONN] bot_nick:{}".format(bot_nick))
print("[CONN] channel:{}".format(channel))

# Init a client and its connection
bot = IRC_client(server,port,bot_nick,channel)
time.sleep(1)

# Greeting message
bot.msg(channel, "Bot ready")
bot_log("READY")

# Main loop 
while True:
    time.sleep(0.1)
    try:
        # Receiving messages
        byte_str = bot.isock.recv(512)
        f_msg = byte_str.decode()
        
        # Handling PINGs
        if f_msg.find("PING") != -1 :
            bot.pong(f_msg.split(" ")[1])
        else:
            print("[IRC] "+f_msg)
        
            try:
                # Splitting incoming messages
                s_code = f_msg.split(" ")[1] # status code
                proc_s_code(s_code) # proccess the status code

                msg_sender = f_msg.split(":")[1].split("!")[0] # gettimg message sender 
                p_command = f_msg.split(" ")[1] # getting protocol command
                msg_target = f_msg.split(" ")[2] # getting message target
                msg = f_msg.split(":")[-1].strip() # getting message itself

                # In case its a PRIVMSG command
                if p_command == "PRIVMSG":
                    # If it is a private message to the bot
                    if msg_target == bot_nick:
                        parse_priv_msg(msg, msg_sender)
                    
                    # If it is a message for the channel
                    elif msg_target == channel:
                        parse_channel_msg(msg, channel)
            except Exception:
                # Exception can occur when parsing/splitting breaks
                pass

    except error as serr:
        # Exception can occur when message recieving breaks
        pass

