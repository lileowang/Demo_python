"""
descripton:
- socket client code
- monitor with:
> Get-NetTCPConnection | ?{$_.LocalPort -in @('8001')} |
>> select local*, remote*, state, `
>> @{n='app'; e={(Get-Process -Id $_.owningprocess).ProcessName}}

"""

import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostbyname('localhost')
port = 8001
server.connect((host, port))
print('connected')
data = server.recv(1024)
data2 = bytes.decode(data)
print(f'from server: {data2}')

while True:
    data = input('to server: ')
    server.send(str.encode(data))
    data = server.recv(1024)
    data2 = bytes.decode(data)
    print(f'from server: {data2}')

    if data2 == 'exit':
        break

print('closing')
server.close()
