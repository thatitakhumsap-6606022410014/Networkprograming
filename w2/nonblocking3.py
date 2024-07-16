import socket
import select
import errno

sock = socket.socket(socket.AF_INET, socket.SOCK_STREM)
sock.connect(('localhost', 1234))
sock.setblocking(0)

data = 'foobar\n' * 1024 * 1024 
data_size = len(data)
print('Bytes to send: ', len(data))

total_sent = 0
while len(data):
    try:
        sent = sock.send(data.encode())
        total_sent += sent
        data = data[sent:]
        print('Sending data')
    except socket.error as e:
        if e.errno != errno.EAGAIN:
            raise e
        print('Blocking with', len(data), 'remaiing')
        select.select([], [sock], []) # This blocks until

assert total_sent == data_size # True