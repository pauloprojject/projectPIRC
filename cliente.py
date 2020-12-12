import socket


HOST = '127.0.0.1'
PORT = 40000

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
dest = (HOST, PORT)

while True:
     try:
          msg = input('BTP> ')
     except:
          msg = 'QUIT'
     udp.sendto(msg.encode(), dest)
     msg2, cliente = udp.recvfrom(1024)
     print(msg2.decode())
     msg = msg.split()
     if msg[0] == 'LIST':
          print(msg2.decode())
     elif msg[0] == 'PESQ':
          a = str(msg[1])    
          print(msg2.decode())
          udp.sendto(a.encode(), dest)
          print(msg2.decode())
udp.close()
