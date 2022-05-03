import socket


class Irc:
    def __init__(self, host : str, port : int, channel : str, nickname : str):
        self.irc_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = host
        self.port = port
        self.channel = channel
        self.nickname = nickname

    def connect(self):
        self.irc_socket.connect((self.host, self.port))
        self.irc_socket.send(str.encode((f"USER {self.nickname} {self.nickname} {self.nickname} {self.nickname}\n")))
        self.irc_socket.send(str.encode((f"NICK {self.nickname}\n")))

    def leave(self):
        self.irc_socket.send(str.encode("QUIT\n"))

    def join_channel(self, channel : str):
        self.irc_socket.send(str.encode(f"JOIN {channel}\n"))

    def receive_message(self):
        message = self.irc_socket.recv(2048).decode("UTF-8")
        return message.strip("\n\r")

    def send_message(self, username : str, message : str):
        self.irc_socket.send(str.encode(f"PRIVMSG {username} : {message}\n"))

    def read_private_message(self, message : str):
        if self.is_private_message(message):
            message = message.split(':', 2)[2]
            return message

    def is_private_message(self, message : str):
        return message.find("PRIVMSG") != -1