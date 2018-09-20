import socket
import sys

gopher_port = 70

host = sys.argv[1]
file_name = sys.argv[2]

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect((host,gopher_port))

message = file_name + "\r\n"
message = message.encode()  # add line for python3

sock.sendall(message)

while True:
    #buff = sock.recv(2048)                  #python2
    buffer = sock.recv(2048).decode('utf-8') #python3
    if not len(buffer):
        break
    sys.stdout.write(buffer)