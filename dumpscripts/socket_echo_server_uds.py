#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import socket
import sys
import os

server_address = './uds_socket'

# Ci si assicura che il socket non esista
try:
    os.unlink(server_address)
except OSError:
    if os.path.exists(server_address):
        raise

# Crea un socket UDS
sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)



# Collega il socket alla porta
print >>sys.stderr, 'in avvio su %s ' % server_address
sock.bind(server_address)

# In ascolto per una connessione in entrata
sock.listen(1)

while True:
    # Attende una connessione
    print >>sys.stderr, 'in attesa di una connessione'
    connection, client_address = sock.accept()
    try:
        print >>sys.stderr, 'connessione da', client_address
    
        # Riceve i dati in piccoli segmenti e li ritrasmette
        while True:
            data = connection.recv(16)
            print >>sys.stderr, 'ricevuto "%s"' % data
            if data:
                print >>sys.stderr, 'reinvio dei dati al client'
                connection.sendall(data)
            else:
                print >>sys.stderr, 'non ci sono più dati da', client_address
                break
            
    finally:
        # Pulisce la connessione
        connection.close()    