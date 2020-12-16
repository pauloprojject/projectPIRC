
#pip install youtube-search

import socket
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


TAM_MSG = 1024 # Tamanho do bloco de mensagem
HOST = '0.0.0.0' # IP do Servidor
PORT = 40000 # Porta que o Servidor escuta
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
orig = (HOST, PORT)
udp.bind(orig)
print('servidor rodando...')


while True:
    msg, cliente = udp.recvfrom(TAM_MSG)
    if not msg: break
    msg = msg.decode().split()
    msg[0] = msg[0].upper()
    if msg[0] == 'LIST':
        a = f"""
        comandos da aplicação:
        PESQ: passa a música como parametro para o comando (EX: PESQ música)
        ALL: testo todo
        URL: url da música
        TITLE: titulo da música
        EXIT: terminar a aplicação
        """
        udp.sendto(a.encode(), cliente)
    elif msg[0] == 'PESQ':
        if msg[1:] != '':
            f = msg[1:]
            msc = youtube_retorno(str(f))
            print(msc)
            b = 'Música pesquisada, para ver o conteúdo use o comando ALL'
            udp.sendto(b.encode(), cliente)
        else:
            c = 'digite um argumento válido.'
            udp.sendto(c.encode(), cliente)
    elif msg[0] == 'ALL':
        if msc:
            udp.sendto(msc.encode(), cliente)
        else:
            c = 'Pesquise uma música antes desse comando.'
            udp.sendto(c.encode(), cliente)
    elif msg[0] == 'URL':
        if msc:
            d = msc
            d = d.split("\n")
            udp.sendto(d[2].encode(), cliente)
        else:
            c = 'Pesquise uma música antes desse comando.'
            udp.sendto(c.encode(), cliente)
    elif msg[0] == 'TITLE':
        if msc:
            e = msc
            e = msc.split('\n')
            udp.sendto(e[0].encode(), cliente)
        else:
            c = 'Pesquise uma música antes desse comando.'
            udp.sendto(c.encode(), cliente)
    elif msg[0] == 'EXIT':
        c = 'Saindo da aplicação...'
        udp.sendto(c.encode(), cliente)
    else:
        c = '-ERR Invalid command\n'
        udp.sendto(c.encode(), cliente)
udp.close()

