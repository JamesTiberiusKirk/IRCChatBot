import sys
import time
import socket

# Logging function
def log(txt):
        print("[CLIENT] {}".format(txt))

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
        log("Joining Server: {}".format(self.server))

        # Connecting socket
        self.isock.connect((self.server, self.port))
        time.sleep(0.5)
        
        # Composing message
        msg = "USER {0} {1} {2} {3}\r\n".format(
            self.bot_nick, 
            self.hostname, 
            self.server, 
            self.real_name)

        #print(msg.encode())
        # Setting nickname
        self.set_nick(self.bot_nick)

        log("Setting user: {}".format(msg.strip()))
        # Sending message and encoding it
        self.isock.send(msg.encode())
        time.sleep(0.5)

    def set_nick(self, nick):
        # Composing message
        msg = "NICK {}\r\n".format(nick)
        log("Setting nick: "+msg.strip())
        #print(msg.encode())

        # Sending message and encoding it
        self.isock.send(msg.encode())
        time.sleep(0.5)
        
    def join_channel(self, channel):
        # Composing message
        msg = "JOIN {}\r\n".format(channel)
        log("Joining channel {}".format(msg.strip()))
        #print(msg.encode())

        # Sending message and encoding it
        self.isock.send(msg.encode())
        time.sleep(0.5)

    def msg(self, dest, message):
        # Composing message
        msg = "PRIVMSG {0} :{1}\r\n".format(dest, message)
        #print(msg.encode())
        log(msg.strip())
        
        # Composing message
        self.isock.send(bytes(msg,"UTF-8"))
        time.sleep(0.5)



    def pong(self, server):
        # Composing message
        msg = "PONG {}".format(server)
        #print(msg.encode())

        # Composing message
        self.isock.send(msg.encode())
        log(msg.strip())
        time.sleep(1)






