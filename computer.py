#!bin/bash/python
#! coding = utf-8
import socket
from collections import deque


class Computer(object):
    """xd"""

    def __init__(self):
        self.udp_port = 5000
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind(("0.0.0.0",5000))

        
    # def start(self):
    #     while True:
    #         # packet = sock.recv()  # get packets from socket, cast to str, split(';')
    #         if not is_token(packet):
    #             if packet[3] == packet.dest_nick:  # if I am the destination device of this packet
    #                 #  packet[1] mark packet as read "OK"
    #                 continue
    #             else:
    #                 # send the received Packet to the next computer
    #         elif is_token(packet)
    #             if len(self.queue) > 0:  # if I want to send messages
    #                 # send message and queue.pop()
    #             # pass token
    #         pass
        

    def connect(self, nickname, next_computer_address="127.0.0.1", next_computer_port=5000):
        self.sock.sendto(b"teste", (next_computer_address, next_computer_port))
        
        
    def wait_connection(self):

        print(self.sock.recv(1024))
        
    def create_token(self):
        return
        
def is_token(packet):
    if packet[0] == 1234
        return True
    elif packet[0] == 2345:
        return False
    

def read_file(file_path: str) -> list:
    '''
    <ip_destino_token>
    <apelido>
    <tempo_token>
    '''
    with open(file_path) as setup_file:
        return list(setup_file)


class Packet(object):
    """Datagram: 2345;naocopiado:Bob:Alice:Oi Mundo!"""
    """Datagram: iden;statuscopy;origin;destination;msg"""
    """          0   ;1         ;2     ;3;         ;4"""
    
    read = False
    
    def __init__(self, origin_nick: str, dest_nick: str, text: str):
        self.dest_nick = dest_nick
        self.dest_nick = dest_nick
        self.text = text
        
    def read():
        self.read = True

        
    def _pprint():
        return "2345\n{}\n{}\n{}\n{}".format(self.read, self.dest_nick, self.dest_nick, self.text)
        
        
    def __str__(self) -> str:
        return "2345;{};{};{};{}".format(self.read, self.dest_nick, self.dest_nick, self.text)
        
        
if __name__ == "__main__":
    setup = read_file("")
