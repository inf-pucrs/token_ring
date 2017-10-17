#!bin/bash/python
#! coding = utf-8
import socket
from collections import deque


class Computer(object):
    """xd"""

    def __init__(self, nickname, next_computer_address="127.0.0.1"):
        self.queue = deque()
        self.nickname = nickname
        self.udp_ip = next_computer_address
        self.udp_port = 5000
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def start(self):
        self.sock.bind((self.udp_ip, self.udp_port))
        while True:
            # get packets from socket
            if packet is token:
                if nickname == packet.dest_nickname:  # if I am the destination device of this packet
                    #  mark packet as read
                    continue
                else:
                    # take my IP off of packet
                    #  write the IP of the next computer in the network
                    #  send it
            # elif packet is token
                if len(self.queue) > 0:  # if I want to send messages
                    # send message and delete from queue (.pop())
                # pass token


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
