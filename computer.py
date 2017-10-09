#!bin/bash/python
#! coding = utf-8
import socket
from collections import deque


class computer(object):
    """xd"""
    def __init__(self, nickname, next_computer_address="127.0.0.1"):
        self.queue = deque()
        self.nickname = nickname
        self.udp_ip = next_computer_address
        self.udp_port = 5000
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
        
    def start(self):
        self.sock.bind((udp_ip, udp_port))
        while True:
            if has_token():
                
                
                
    '''            
    def parse(packet):
        if eu sou a máquina que o pacote quer
            marcar que eu list
    '''

    
'''
<ip_destino_token>
<apelido>
<tempo_token>
'''
     
class token(object):
    """lol"""
    def __init__():
        