#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 11:51:45 2017

@author: laurent
"""

import socket

TCP_IP = '10.0.133.226'
TCP_PORT = 5000
BUFFER_SIZE = 1024
MESSAGE = "Hello, World!"


#TCP server connection
def connection(IP, PORT):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((IP, PORT))
    
    #Receiving the server message
    data = s.recv(BUFFER_SIZE)
    print("received data:", data)
    #Pseudo entry
    pseudo = input()
    s.sendall(bytes(pseudo, 'utf8'))
    
    #infinite loop to enter messages continuously
    while 1:
        #Message entry
        msg = input(pseudo + ' : ')
        #Message send
        s.sendall(bytes(msg, 'utf8'))
    
    #Close Connection   
    s.close()
    

connection(TCP_IP, TCP_PORT)