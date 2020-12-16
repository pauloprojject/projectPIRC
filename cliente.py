import socket
import webbrowser

HOST = '127.0.0.1'
PORT = 40000

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
dest = (HOST, PORT)
msc = ''
while True:
     try:
          msg = input('> ')
     except:
          msg = 'EXIT'
     udp.sendto(msg.encode(), dest)
     msg2, cliente = udp.recvfrom(1024)
     msg = msg.split()
     msg[0] = msg[0].upper()
     if msg[0] != 'PESQ':
          print(msg2.decode())
     if msg[0] == 'LIST':
          msg2.decode()
     elif msg[0] == 'PESQ':
          msc = msg2.decode()
          print('Música pesquisada, para ver o conteúdo use o comando ALL')
     elif msg[0] == 'ALL':
          if msc:
               print(msc)
          else:
               print('Pesquise uma música antes desse comando.')
     elif msg[0] == 'URL':
          if msc:
               d = msc
               d = d.split("\n")
               print(d[2])
          if len(msg) > 1:
               if msg[1].upper() == 'OPEN':
                    d = msc
                    d = d.split("\n")
                    a = d[2].split(' ')
                    webbrowser.open(a[1])
          else:
               print(msc)
               print('Pesquise uma música antes desse comando.')
     elif msg[0] == 'TITLE':
          if msc:
               d = msc
               d = d.split("\n")
               print(d[0])
          else:
               print('Pesquise uma música antes desse comando.')
     elif msg[0] == 'EXIT':
          break
udp.close()
