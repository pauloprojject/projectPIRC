#!/usr/bin/env python3
import socket
import os
import threading

TAM_MSG = 1024 # Tamanho do bloco de mensagem
HOST = '0.0.0.0' # IP do Servidor
PORT = 40000 # Porta que o Servidor escuta

def processar_cliente(con, cliente):
    print('Cliente conectado', cliente)
    while True:
        msg = con.recv(TAM_MSG)
        if not msg: break
        msg = msg.decode().split()
        if msg[0].upper() == 'GET':
            nome_arq = " ".join(msg[1:])
            print('Arquivo solicitado:', nome_arq)
            try:
                status_arq = os.stat(nome_arq)
                con.send(str.encode('+OK {}\n'.format(status_arq.st_size)))
                arq = open(nome_arq, "rb")
                while True:
                    dados = arq.read(TAM_MSG)
                    if not dados: break
                    con.send(dados)
            except Exception as e:
                con.send(str.encode('-ERR {}\n'.format(e)))
        elif msg[0].upper() == 'LIST':
            lista_arq = os.listdir('.')
            con.send(str.encode('+OK {}\n'.format(len(lista_arq))))
            for nome_arq in lista_arq:
                if os.path.isfile(nome_arq):
                    status_arq = os.stat(nome_arq)
                    con.send(str.encode('arq: {} - {:.1f}KB\n'.format(nome_arq, status_arq.st_size/1024)))

                elif os.path.isdir(nome_arq):
                    con.send(str.encode('dir: {}\n'.format(nome_arq)))
                else:
                    con.send(str.encode('esp: {}\n'.format(nome_arq)))


        elif msg[0].upper() == 'CD':
            current = os.getcwd()
            currentSplit = current.split('/')
            if len(msg) != 0:
                newdir = ''
                dir = msg[1].split('/')
                for i in dir:
                    if i == '..':
                        current = current.replace(currentSplit[-1],'')
                        del(currentSplit[-1])
                    elif i == dir[-1]:
                        current = current + i
                    else:
                        current = newdir + i + '/'
                newdir = current
                try:
                    os.chdir(newdir)
                    con.send(str.encode('+OK\n'))
                except:
                    con.send(str.encode( newdir + '-ERR - Directory not found'))

        elif msg[0].upper() == 'PWD':
            con.send(str.encode(os.getcwd()))

        elif msg[0].upper() == 'QUIT':
            con.send(str.encode('+OK\n'))
            break
        else:
            con.send(str.encode('-ERR Invalid command\n'))
    con.close()
    print('Cliente desconectado', cliente)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv = (HOST, PORT)
sock.bind(serv)
sock.listen(50)
while True:
    try:
        con, cliente = sock.accept()
    except: break
    threading.Thread(target=processar_cliente, args=(con, cliente)).start()
    
sock.close()