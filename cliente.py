import socket
import webbrowser


HOST = '127.0.0.1'
PORT = 40000

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
dest = (HOST, PORT)

while True:
     try:
          msg = input('> ')
     except:
          msg = 'EXIT'
     udp.sendto(msg.encode(), dest)
     msg2, cliente = udp.recvfrom(1024)
     print(msg2.decode())
     msg = msg.split()
     if msg[0] == 'LIST':
          msg2.decode()
     elif msg[0] == 'PESQ':
          msg2.decode()
     elif msg[0] == 'ALL':
          msg2.decode()
     elif msg[0] == 'URL':
          msg2.decode()
          if msg[1].upper() == 'OPEN':
               a = msg2.decode().split(' ')
               webbrowser.open(a[1])
     elif msg[0] == 'TITLE':
          msg2.decode()
     elif msg[0] == 'EXIT':
          break
udp.close()
