"""
descripton:
- socket server code
- monitor with:
> Get-NetTCPConnection | ?{$_.LocalPort -in @('8001')} |
>> select local*, remote*, state, `
>> @{n='app'; e={(Get-Process -Id $_.owningprocess).ProcessName}}

"""

import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = ''
port = 8001
server.bind((host, port))
print('listening')
server.listen(5)
client, adr = server.accept()
print(f'client: {adr}')
client.send(str.encode('welcome'))

while True:
    data = client.recv(1024)
    client.send(data)
    data2 = bytes.decode(data)
    print(f'from client: {data2}')

    if data2 == 'exit':
        break

print('closing')
client.close()
