import socket
import http

HOST = '127.0.0.1'
PORT = 40000

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
dest = (HOST, PORT)

print('Para sair digite CTRL+X\n')
msg = input('informe o artista e música que queira pesquisar: ')

# while msg != '\x18':
udp.sendto(msg.encode(), dest)


msg2, cliente = udp.recvfrom(1024)
print(msg2.decode())
# msg = input('informe o artista e música que queira pesquisar: ')
udp.close()