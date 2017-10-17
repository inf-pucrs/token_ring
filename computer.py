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
        self.sock.bind((udp_ip, udp_port))
        while True:
            if has_token():
                if len(queue) > 0:  # if I want to send messages
                    # send message
                else:
                    # pass token
            else:
                # get_packet
                if nickname == packet.dest_nickname:  # if I am the destination device of this packet
                    #  mark packet as read
                    continue
                else:
                    #  take my IP off of packet
                    #  write the IP of the next computer in the network
                    #  send it
                
                    

    def has_token():
        pass


'''
<ip_destino_token>
<apelido>
<tempo_token>
'''
     
class Token(object):
    """lol"""
    def __init__(self):
        # something that identifies on which computer am I

class Packet(object):
    """Datagram."""
    def __init__(self, dest_ip, dest_nickname, text):
        self.dest_ip = dest_ip
        self.dest_nickname = dest_nickname
        self.text = text
