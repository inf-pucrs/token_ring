#!bin/bash/python
# -*- coding: utf-8 -*-

import socket
import time
import threading
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
        and a boolean to set whether it is the first computer on a network
        (defaults to false because this will only be used once)
        """
        self.ny_nickname = ny_nickname
        self.my_socket_address = my_socket_address
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind(self.my_socket_address)
        
        self.next_computer_address = next_computer_address
        self.packet_queue = deque()
        self.tokenizer = tokenizer
        self.lock = threading.Lock()
        self.threads = []


    def start(self):

        if self.tokenizer:
            self.pass_token()

        chat = threading.Thread(target=self.chat_thread())
        token = threading.Thread(target=self.token_thread())
        self.threads.append(chat)
        self.threads.append(token)
        token.start()
        chat.start()
        
        
    def token_thread(self):
        while True:
            print("iniciou a thread token")
            #iniciar thread para enviar receber token
            pckt = self.wait_connection().decode('utf-8').split(';')
            time.sleep(1)
            print(pckt)
            packet = Packet(*pckt)  # get packets from socket, cast to str, split(';')
            if not packet.is_token():
                if self.ny_nickname == packet.dest_nick:
                    # if I am the destination device of this packet
                    packet.read()  # mark packet as read "OK"
                    self.connect(packet.to_bytes())  # send packet to next computer on the network
                elif self.ny_nickname == packet.origin_nick:
                    # it means the packet I had sent to some computer on the network got back to me
                    if packet.has_been_read == 'OK':
                        print('Packet was read by destination machine.')
                        self.pass_token()
                    else:
                        print('Packet was NOT READ by destination.')
                        self.pass_token()
                else:
                    # Packet was not sent TO me nor sent BY me.
                    print(packet, 'entrou naquele lugar ;)')
                    self.connect(packet.to_bytes())
            elif packet.is_token():
                print("Recebi o token.")
                if len(self.packet_queue) > 0:
                    # if I want to send messages
                    self.connect(self.packet_queue.popleft().to_bytes())
                    # wait for packet to come back
                    continue
                else:
                    self.pass_token()
                    
        pass

    def chat_thread(self):
        while True:
            a = input('Digite o apelido dos computador de destino ou 0 para sair: ')
            
            text = input("Digite o texto a ser enviado: ")
            pkt = self.create_packet(a.strip(), text).to_bytes()
            self.packet_queue.append(pkt)
        
        
    def connect(self, text: bytes=b"teste"):
        self.sock.sendto(text, self.next_computer_address)

    def wait_connection(self):
        incoming = self.sock.recv(1024)
        return incoming

    def create_packet(self, dest_nick: str, text: str):
        return Packet('2345', '', self.ny_nickname, dest_nick, text)

    def pass_token(self):
        print("Passando token ao", str(self.next_computer_address))
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
openopen three ipython sessions and copypaste this
(must cd token_ring first)

from computer import Computer
pc = Computer('Gian', ('0.0.0.0', 5000), ('localhost', 6000))
pc.start()

from computer import Computer
pc = Computer('Nei', ('0.0.0.0', 6000), ('localhost', 5000))
pc.start()

from computer import Computer
pc = Computer('João', ('0.0.0.0', 7000), ('localhost', 5000))
pc.start()

"""
# if __name__ == "__main__":
    # setup = read_file("")
