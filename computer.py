#!bin/bash/python
#! coding = utf-8
import socket
from collections import deque


class Computer(object):
    """xd"""

    def __init__(self):
        self.queue = deque()
        self.udp_port = 5000
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


    def connect(self,nickname, next_computer_address="127.0.0.1",next_computer_port = 5000):
        self.sock.sendto(b"teste",(next_computer_address,next_computer_port))
        
        
    def wait_connection(self):
        print(self.sock.recv(1024))
        
    def create_token(self):
        return
        
'''
<ip_destino_token>
<apelido>
<tempo_token> ???
'''

class Packet(object):
    """Datagram."""
    
    def __init__(self, dest_ip: str, dest_nickname: str, time, text: str):
        self.dest_ip = dest_ip
        self.dest_nickname = dest_nickname
        self.time = time
        self.text = text


    def __str__(self) -> str:
        return "{}\n{}\n{}\n{}".format(self.dest_ip, self.dest_nickname, self.time, self.text)

        
