import socket


def Server3():
    host = '192.168.0.106'
    port = 5003

    s = socket.socket()
    s.connect((host, port))

    message = 'trigger'

    s.send(message.encode())
    data = s.recv(1024).decode('utf-8')
    print(type(data))
    print('Received from Server ' + str(data[0]))
    s.close()
    return data


if __name__ == '__main__':
    data = Server3()