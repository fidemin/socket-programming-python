import socket
import sys


if __name__ == '__main__':
    host = sys.argv[1]
    port = int(sys.argv[2])
    num_of_backlog = int(sys.argv[3])

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.bind((host, port))
        s.listen(num_of_backlog)
        print(f'[INFO] listens to {host}:{port} with backlog {num_of_backlog}')
        while True:
            conn, addr = s.accept()
            with conn:
                print(f'[INFO] connected to {addr[0]}:{addr[1]}')
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    print(f'[INFO] received data: {data.decode("utf-8")}')

                    # echo to client
                    conn.sendall(data)
    finally:
        print('[INFO] socket closed')
        s.close()
