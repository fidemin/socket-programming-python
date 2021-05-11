import socket
import sys


if __name__ == '__main__':
    host = sys.argv[1]
    port = int(sys.argv[2])
    num_of_backlog = int(sys.argv[3])

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen(num_of_backlog)
        print(f'[INFO] listens to {host}:{port} with backlog {num_of_backlog}')
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
