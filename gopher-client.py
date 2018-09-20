import socket
import sys

gopher_port = 70

host = sys.argv[1]
file_name = sys.argv[2]

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect((host,gopher_port))
sock.sendall(file_name+"\r\n")

while True:
    buffer = sock.recv(2048)
    if not len(buffer):
        break
    sys.stdout.write(buffer)