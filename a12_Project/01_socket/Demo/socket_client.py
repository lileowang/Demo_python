# Author:      Li Leo Wang
# Start Date:  2019-06-21
# Description:
#      - socket client
# Notes:
#      - monitor with: netstat -an | find -5151
#
# Change history:
#      - Refer to GitHub comments related to each source file.
#

import sys
import socket

def Run():
    
    print('in client')

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = socket.gethostbyname('localhost')
    port = 5151
    server.connect((host, port))
    print('connected')
    data = server.recv(1024)
    data2 = bytes.decode(data)
    print('from server:', data2)

    while True:
        data = input('to server: ')
        server.send(str.encode(data))
        data = server.recv(1024)
        data2 = bytes.decode(data)
        print('from server:', data2)

        if 'exit' == data2:
            break

    print('closing')
    server.close()
    