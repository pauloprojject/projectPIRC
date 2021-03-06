
#pip install youtube-search

import socket
import http
from youtube_search import YoutubeSearch
import json

def youtube_retorno(a):
    results = YoutubeSearch(a, max_results=1).to_json()
    xablau = results.split('"')

    b = ''

    for i in range(len(xablau)):
        if "title" in xablau[i]:
            # print("=" * 20)
            b += "titulo: " + xablau[i+2] + '\n'
        if "/watch?" in xablau[i]:
            b += "url: https://www.youtube.com" + xablau[i] + '\n'
            # print("=" * 20)
            print("\n")
        if "duration" in xablau[i]:
            b += "duração: " + xablau[i+2] + '\n'
    return b


HOST = '0.0.0.0'  # Endereco IP do Servidor
PORT = 40000  # Porta que o Servidor está

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
orig = (HOST, PORT)
udp.bind(orig)

print('Servidor no ar...')
while True:
    msg, cliente = udp.recvfrom(1024)  # quantidade de bytes que espera receber
    a = youtube_retorno(msg.decode())
    print(a)
    if msg:
        udp.sendto(a.encode(), cliente)
    print('Recebi de ', cliente, msg.decode()) # decode = de bytes para string
udp.close()