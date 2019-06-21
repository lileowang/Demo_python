# Author:      Li Leo Wang
# Start Date:  2019-06-21
# Description:
#      - socket server
# Notes:
#      - monitor with: netstat -an | find -5151
#
# Change history:
#      - Refer to GitHub comments related to each source file.
#

import sys
import socket

def Run():
    
    print('in server')

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = ''
    port = 5151
    server.bind((host, port))
    print('listening')
    server.listen(5)
    client, adr = server.accept()
    print('client:', adr)
    client.send(str.encode('welcome'))

    while True:
        data = client.recv(1024)
        data2 = bytes.decode(data)
        print('from client:', data2)
        client.send(data)

        if 'exit' == data2:
            break

    print('closing')
    client.close()
    