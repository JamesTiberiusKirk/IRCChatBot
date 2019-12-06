import sys
import time
import socket

# Logging function
def log(txt):
        print("[CLIENT] "+txt)

class IRC_client:

    def __init__(self,server, port, bot_nick, channel):
        # Setting some globa variables
        self.server = server
        self.port = port
        self.bot_nick = bot_nick
        self.channel = channel
        self.hostname = bot_nick
        self.real_name = bot_nick

        # Socket Init
        self.isock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Joning server
        self.join_server()

        # Joining channel
        self.join_channel(self.channel)


    def join_server(self):
        log("Joining Server: "+self.server)

        # Connecting socket
        self.isock.connect((self.server, self.port))
        time.sleep(0.5)
        
        # Composing message
        msg = "USER "+self.bot_nick+" "
        msg += self.hostname+" " 
        msg += self.server+ " " 
        msg += self.real_name
        msg += "\r\n"

        # Setting nickname
        self.set_nick(self.bot_nick)

        log("Setting user: "+msg.strip())
        # Sending message and encoding it
        self.isock.send(msg.encode());
        time.sleep(0.5)

    def set_nick(self, nick):
        # Composing message
        msg = "NICK " + nick + "\r\n"
        log("Setting nick: "+msg.strip())
        
        # Sending message and encoding it
        self.isock.send(msg.encode())
        time.sleep(0.5)
        
    def join_channel(self, channel):
        # Composing message
        msg = "JOIN " + channel 
        msg += "\r\n"
        log("Joining channel "+ msg.strip())

        # Sending message and encoding it
        self.isock.send(msg.encode())
        time.sleep(0.5)

    def msg(self, dest, message):
        # Composing message
        msg = "PRIVMSG {0} :{1} \r\n".format(dest, message)

        log(msg.strip())
        
        # Composing message
        self.isock.send(bytes(msg,"UTF-8"))
        time.sleep(0.5)



    def pong(self, server):
        # Composing message
        msg = "PONG "+ server 
        msg += "\r\n"

        # Composing message
        self.isock.send(msg.encode())
        log(msg.strip())
        time.sleep(1)






