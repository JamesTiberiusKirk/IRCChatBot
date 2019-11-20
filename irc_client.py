
import sys
import time
import socket

class IRC_client:
    
    def __init__(self,server, port, bot_nick, channel):
        self.server = server
        self.port = port
        self.bot_nick = bot_nick
        self.channel = channel
        self.hostname = bot_nick
        self.real_name = bot_nick
        self.join_server()
        self.set_nick(self.bot_nick)
        self.join_channel(self.channel)


    def join_server(self):
        print("Joining Server: "+self.server)

        self.isock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.iscok.connect(self.server, self.port)
        self.isock.setblocking(False)
        time.sleep(1)
        
        msg = "USER "+self.bot_nick+" "+ self.hostname+" " + servername+ " " + real_name

        print("Setting user: "+msg)
        self.isock.send(msg.encode());



    def set_nick(self, nick):
        msg = "NICK " + nick
        print("Setting nick: "+msg)
        self.isock.send(msg.encode())
        
    def join_channel(self, channel):
        msg = "JOIN " + channel 
        print("Joining channel "+ msg)
        self.isock.send(msg.encode())

    def msg(self,message):
        pring(message)

    def msg(self, user, message):
        print(user+" "+message)


    def ping_back(self, server):
        msg = "PONG "+ server
        #print()
        self.isocket.send(msg.encode())






