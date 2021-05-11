#!/usr/bin/env python3

import socket

HOST = '127.0.0.1'
PORT = 10000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    print(f'[INFO] connected to {HOST}:{PORT}')
    while True:
        print('>>', end=' ')
        input_data = input()
        s.sendall(input_data.encode(encoding='utf-8'))
        received_data = s.recv(1024)
        print(f'received data: {received_data.decode("utf-8")}')
