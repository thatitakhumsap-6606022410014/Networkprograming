import socket

HOST = ''
PORT = 50007
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind (HOST, PORT)
    s.listen(1)
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.rrecv(1024)
            if not data: break
            conn.sendall(data)

import socket
HOST = 'daring.cwi.nl'
PORT = 50007
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect (HOST, PORT)
    s.sendall(b'Hello world')
    data = s.recv(1024)
print('Received', repr(data))