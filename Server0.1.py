# -*- coding: utf-8 -*-

#Version 0.1 del proyecto sistemas distribuidos
#Sebastian Ardila
#Cristian Ciro
#Esta parte del proyecto Sincronizara relojes y ofrecera servicios a multiples clientes.

import SocketServer
import threading

#Esta clase contendra el menu y los llamados a los servicios para los clientes.
class MiTcpHandler(SocketServer.BaseRequestHandler):
	def Handle(self):
#creamos el menu
		sock.send("Selecciona el numero de la opcion que desees: \n")
		print "1) Factorial \n", "2) Potencia \n", "3) Invertir Matriz \n" "4) Ver hora del servidor \n", "5) Salir \n"
		
		data ="" #Creamos una variable vacia.
#Iniciaos las opciones.
		if data == "1": #Factorial
			print "Ingrese el numero por favor: \n"
			numero1 = int(self.request.recv(1024))
			numero2 = factorial(numero1)
			print "el factorial de %s es: %s" % numero1, numero2
		if data=="2": #Potencia
			print "ingrese el numero base por favor: \n"
			numero1= int(self.request.recv(1024))
			print "ingrese el numero a elevar: \n"
			nuemro2= int(self.request.recv(1024))
			numero3= potencia(numero1,numero2)
			print "%s elevado a la %s es: %s" % numero1, numero2, numero3
		if data =="3": #Invertir matriz
			print "Ingrese la matriz por favor: \n"

		if data =="4":
			print "Hora del servidor HH:MM"

#Esta parte implementara el algoritmo de Berkeley
#Aqui pondria el codigo, ¡SI TAN SOLO TUBIERA UNO!

# Funcion que calcula el factorial de a
def factorial(a):
	aux = a-1
	limit = a
	count = 1
	while(count < (limit-1)):
		a = a*aux
		aux = aux-1
		count = count +1
		return a

#Funcion que calcula la pontencia de numero elevado a la potencia
def potencia(numero,potencia):
	return pow(numero,potencia)
#Funcion que invierte una matriz.
def invertirMatriz_remoto(lista):
	listaInvertida = []
	n = 1
	for i in lista:
		listaInvertida.append(lista[-n])
		n += 1
		return listaInvertida

#Ahora creamos lo que permitira que varios clientes se puedan conectar.
class ThreadServer(SocketServer.ThreadingMixIn, SocketServer.ForkingTCPServer):
	pass
#Ahora creamos la funcion que llamara a nuestro servidor.
def main():
	host="localhost"
	port= 9990
	server = ThreadServer((host,port),MiTcpHandler)
	server_Thread = threading.Thread(target=server.serve_forever)
	server_Thread.start()
	print "server corriendo... \n"
main()
