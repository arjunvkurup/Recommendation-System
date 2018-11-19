import socket
import ast

def Server1():
    host = '192.168.43.214'
    port = 5001

    s = socket.socket()
    s.connect((host, port))

    message = 'trigger'

    s.send(message.encode())
    data = s.recv(1024).decode('utf-8')
    print(type(data))
    print('Received from Server ' + str(data))
    x = ast.literal_eval(data)
    print(x)
    s.close()
    return x


if __name__ == '__main__':
    data = Server1()