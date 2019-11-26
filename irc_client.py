
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

        self.isock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.join_server()
        self.set_nick(self.bot_nick)
        self.join_channel(self.channel)


    def join_server(self):
        print("[CLIENT] Joining Server: "+self.server)

        self.isock.connect((self.server, self.port))
        #self.isock.setblocking(0)
        time.sleep(0.5)
        
        msg = "USER "+self.bot_nick+" "
        msg += self.hostname+" " 
        msg += self.server+ " " 
        msg += self.real_name
        msg += ":Hi\r\n"

        print("[CLIENT] Setting user: "+msg)
        self.isock.send(msg.encode());
        time.sleep(0.5)

    def set_nick(self, nick):
        msg = "NICK " + nick + "\r\n"
        print("[CLIENT] Setting nick: "+msg)
        self.isock.send(msg.encode())
        time.sleep(0.5)
        
    def join_channel(self, channel):
        msg = "JOIN " + channel 
        msg += "\r\n"
        print("[CLIENT] Joining channel "+ msg)
        self.isock.send(msg.encode())
        time.sleep(0.5)

    def msg(self, dest, message):
        msg = "PRIVMSG {0} {1} \n".format(dest, message)

        print("[CLIENT] {}".format(msg) )
        self.isock.send(bytes(msg,"UTF-8"))
        time.sleep(0.5)



    def pong(self, server):
        msg = "PONG "+ server 
        msg += "\r\n"
        self.isock.send(msg.encode())
        time.sleep(1)






