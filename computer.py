#!bin/bash/python
# -*- coding: utf-8 -*-

import socket
from typing import Tuple
from collections import deque
from packet import Packet


class Computer(object):
    """xd"""

    def __init__(self, ny_nickname: str,
                 my_socket_address: Tuple[str, int] = ('localhost', 5000),
                 next_computer_address: Tuple[str, int] = ('localhost', 6000),
                 tokenizer: bool=False):
        """
        It gets a tuple to set where to host the server,
        another tuple to set where to send his packets
        and a boolean to set whether it is the first computer on a network (defaults to false because this will only be used once)
        """
        self.ny_nickname = ny_nickname
        self.my_socket_address = my_socket_address
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind(self.my_socket_address)
        
        self.next_computer_address = next_computer_address
        self.packet_queue = deque()
        self.tokenizer = tokenizer


    def start(self):

        if self.tokenizer:
            self.pass_token()

        while True:
            packet = Packet(*str(self.wait_connection()).split(';'))  # get packets from socket, cast to str, split(';')
            if not packet.is_token():
                if self.ny_nickname == packet.dest_nick:
                    # if I am the destination device of this packet
                    packet.read()  # mark packet as read "OK"
                    self.connect(packet.to_bytes())  # send packet to next computer on the network
                elif self.ny_nickname == packet.origin_nick:
                    # it means the packet I had sent to some computer on the network got back to me
                    if packet.has_been_read:
                        print('Packet was read by destination machine.')
                        # pass token
                    else:
                        print('Packet was NOT READ by destination.')
                else:
                    # Packet was not sent TO me nor sent BY me.
                    self.connect(packet.to_bytes())
            elif packet.is_token():
                print("Recebi token")
                if len(self.packet_queue) > 0:
                    # if I want to send messages
                    self.connect(self.packet_queue.popleft().to_bytes())
                    # wait for packet to come back
                    continue
                else:
                    print("passando token")
                    self.pass_token()

        pass

    def connect(self, text: bytes=b"teste"):
        self.sock.sendto(text, self.next_computer_address)

    def wait_connection(self):
        incoming = self.sock.recv(1024)
        return incoming

    def pass_token(self):
        self.connect(Packet('1234', '', '', '', '').to_bytes())


def read_file(file_path: str) -> list:
    '''
    <ip_destino_token>
    <apelido>
    <tempo_token>to
    '''
    with open(file_path) as setup_file:
        return list(setup_file)

"""
To run on a single machine,
openopen two ipython sessions and copypaste this
(must cd token_ring first)

from computer import Computer
pc1 = Computer('Gian', ('0.0.0.0', 5000), ('10.32.143.194', 5000))
print(pc1.wait_connection())

from computer import Computer
pc2 = Computer('nei', ('0.0.0.0', 5000), ('10.32.143.174', 5000))
pc2.connect(b"testão")

"""
# if __name__ == "__main__":
    # setup = read_file("")
