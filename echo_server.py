

import socket
from io import BytesIO

HOST = '127.0.0.1'
PORT = 10000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(2)
    print(f'[INFO] listens to {HOST}:{PORT}')
    conn, addr = s.accept()
    with conn:
        print(f'[INFO] connected to {addr}')
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print(f'[INFO] received data: {data.decode("utf-8")}')

            # echo to client
            conn.sendall(data)
