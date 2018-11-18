import socket
import ast


def Server2():
    host = '192.168.0.104'
    port = 5002

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
    return data


if __name__ == '__main__':
    data = Server2()