#!bin/bash/python
# -*- coding: utf-8 -*-

import socket
from typing import Tuple
from collections import deque


class Computer(object):
    """xd"""

    def __init__(self, my_socket_address: Tuple[str, int] = ('localhost', 5000), tokenizer: bool=True):
        self.address_to_host_server = my_socket_address
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind(self.address_to_host_server)
        self.packet_queue = deque()
        if tokenizer:
            self.create_token()

    def start(self):
        '''
        while True:
            # packet = sock.recv()  # get packets from socket, cast to str, split(';')
            if not is_token(packet):
                if packet[3] == packet.dest_nick:  # if I am the destination device of this packet
                    #  packet[1] mark packet as read "OK"
                    continue
                else:
                    # send the received Packet to the next computer
            elif is_token(packet)
                if len(self.queue) > 0:  # if I want to send messages
                    # send message and queue.pop()
                # pass token
        '''
        pass

    def connect(self, nickname, text=b"teste", next_computer_address: Tuple[str, int] = ('localhost', 6000)):
        self.sock.sendto(text, next_computer_address)

    def wait_connection(self):
        incoming = self.sock.recv(1024)
        print(incoming)
        return incoming

    @staticmethod
    def to_bytes(ass: Packet):
        return bytes(str(ass), 'utf-8')

    def create_token(self):
        return Packet(1234, '', '', '')


def is_token(packet):
    if packet[0] == 1234:
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

    def __init__(self, packet_type: int, origin_nick: str, dest_nick: str, text: str):
        self.packet_type = packet_type
        self.origin_nick = origin_nick
        self.dest_nick = dest_nick
        self.text = text
        self.has_been_read = False

    @staticmethod
    def is_token(packet):
        if packet[0] == 1234:
            return True
        elif packet[0] == 2345:
            return False

    def read(self):
        self.has_been_read = True

    def _pprint(self):
        return "{}\n{}\n{}\n{}\n{}".format(self.packet_type, self.read, self.dest_nick, self.dest_nick, self.text)

    def __str__(self) -> str:
        return "{}\n{}\n{}\n{}\n{}".format(
            self.packet_type, self.has_been_read, self.dest_nick, self.dest_nick, self.text)
        
        
if __name__ == "__main__":
    from computer import Computer
    pc1 = Computer(('localhost', 5000))
    pc1.wait_connection()

    pc2 = Computer(('localhost', 6000))
    pc2.connect('', b"teste", ('localhost', 5000))

    pc3 = Computer(('localhost', 7000))

    # setup = read_file("")
