import socket
import psycopg2
import csv
from kmeans import *


# Main 
def Main():
    # Ipaddress of nodes
    host = '<ipaddresses-of-servers>'
    # Port to be connected
    port = 5000

    # binding TCP socket
    s = socket.socket()
    s.bind((host, port))

    # Open to request
    s.listen(2)
    # Accepting connection with the machine/server
    c, addr = s.accept()
    print("Connection from : " + str(addr))
    
    # Infinite loop for server to keep running
    while True:
        # save the data recived from the machinei
        data = c.recv(1024)

        # Checking whether the data is there or not
        if not data:
            break

        # Database code
        # String for connection
        conn_string = "host='localhost' dbname='postgres' user='postgres' password='server'"
        
        # connect to database using the connection string
        database = psycopg2.connect(conn_string) 

        cursor = database.cursor()
        cursor.execute("SELECT * from location")

        # retriving all the datas from database
        result = cursor.fetchall()

        # External function for Kmeans clustering
        val = calling(result)
        data = str(val)
        print("Sending " + str(data))
        # Sending data in the form of byte by encoding [python3 feature]
        c.send(data.encode())
    s.close()


# Main function call
if __name__ == '__main__':
    Main()