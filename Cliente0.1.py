# -*- coding: utf-8 -*-

#Version 0.1 del proyecto sistemas distribuidos
#Sebastian Ardila
#Cristian Ciro
#Esta parte del proyecto se comunica con el servidor para solicitar servicios.

import socket

def main():
	print "Hola soy el cliente"
	msj=""
	host, port = "localhost", 9990

	sock=socket.socket()
	sock.connect((host,port))
	
	while msj != "salir":
		msj = raw_input("> ")
		sock.send(msj)
	sock,close()

main()
