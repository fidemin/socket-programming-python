import socket
import sys


if __name__ == '__main__':
    host = sys.argv[1]
    port = int(sys.argv[2])

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        print(f'[INFO] connected to {host}:{port}')
        while True:
            # make prompts
            print('>>', end=' ')

            # send input data to server
            input_data = input()
            s.sendall(input_data.encode(encoding='utf-8'))

            # receive data from server
            received_data = s.recv(1024)
            print(f'[INFO] received data: {received_data.decode("utf-8")}')
