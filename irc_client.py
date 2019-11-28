
import sys
import time
import socket

def log(txt):
        print("[CLIENT] "+txt)

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
        self.join_channel(self.channel)


    def join_server(self):
        log("Joining Server: "+self.server)

        self.isock.connect((self.server, self.port))
        #self.isock.setblocking(0)
        time.sleep(0.5)
        
        msg = "USER "+self.bot_nick+" "
        msg += self.hostname+" " 
        msg += self.server+ " " 
        msg += self.real_name
        msg += ":Hi\r\n"

        self.set_nick(self.bot_nick)

        log("Setting user: "+msg.strip())
        self.isock.send(msg.encode());
        time.sleep(0.5)

    def set_nick(self, nick):
        msg = "NICK " + nick + "\r\n"
        log("Setting nick: "+msg.strip())
        self.isock.send(msg.encode())
        time.sleep(0.5)
        
    def join_channel(self, channel):
        msg = "JOIN " + channel 
        msg += "\r\n"
        log("Joining channel "+ msg.strip())
        self.isock.send(msg.encode())
        time.sleep(0.5)

    def msg(self, dest, message):
        msg = "PRIVMSG {0} :{1} \r\n".format(dest, message)

        log(msg.strip())
        self.isock.send(bytes(msg,"UTF-8"))
        time.sleep(0.5)



    def pong(self, server):
        msg = "PONG "+ server 
        msg += "\r\n"
        self.isock.send(msg.encode())
        log(msg.strip())
        time.sleep(1)






