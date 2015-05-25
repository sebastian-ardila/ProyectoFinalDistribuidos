# -*- coding: utf-8 -*-

#Version 0.1 del proyecto sistemas distribuidos
#Sebastian Ardila
#Cristian Ciro
#Esta parte del proyecto Sincronizara relojes y ofrecera servicios a multiples clientes.

import SocketServer
import threading
import time

#Esta clase contendra el menu y los llamados a los servicios para los clientes.
class MiTcpHandler(SocketServer.BaseRequestHandler):
    def handle(self):

        #opcion = ""
        while True:
            try:
                opcion = self.request.recv(1024)
                print opcion

                cadena = opcion.split(' ')
                print "cadena -> " + str(cadena)
                opcion = cadena[0]
                print opcion + str(type(opcion))

                del cadena[0]
                print "nueva cadena -> "+ str(cadena)

                #print "escogiste la opcion "+opcion

                #--------------------------------------------------
                #Factorial
                if opcion == '1':
                    mensaje = ''.join(cadena)
                    #print "mensaje "+mensaje
                    resultado = factorial_remoto(int(mensaje))
                    self.request.send(str(resultado))

                #--------------------------------------------------
                #Potencia
                if opcion == '2':
                    #print cadena
                    resultado = potencia_remoto(int(cadena[0]), int(cadena[1]))
                    self.request.send(str(resultado))

                #--------------------------------------------------
                #Invertir Matriz
                if opcion == '3':
                    lista = cadena
                    mensaje = ' '.join(cadena)
                    resultado = invertirMatriz_remoto(str(mensaje))
                    self.request.send(str(resultado))


                #--------------------------------------------------
                #ver hora del servidor
                if opcion == '4':
                    pass

            except:
               print "el cliente se desconecto o hubo un error"
               break
        return resultado

#Esta parte implementara el algoritmo de Berkeley
#Aqui pondria el codigo, ¡SI TAN SOLO TUVIERA UNO!

# Funcion que calcula el factorial de a
def factorial_remoto(a):
    aux = a-1
    limit = a
    count = 1
    while(count < (limit-1)):
        a = a*aux
        aux = aux-1
        count = count +1
    print a
    return a

#Funcion que calcula la pontencia de numero elevado a la potencia
def potencia_remoto(numero,potencia):
    return pow(numero,potencia)

#Funcion que invierte una matriz.
def invertirMatriz_remoto(lista):
    cadena = lista.split(' ')
    listaInvertida = []
    n = 1
    for i in cadena:
        listaInvertida.append(cadena[-n])
        n += 1
    print listaInvertida
    return str(listaInvertida)


#Ahora creamos lo que permitira que varios clientes se puedan conectar.
class ThreadServer(SocketServer.ThreadingMixIn, SocketServer.ForkingTCPServer):
	pass
#Ahora creamos la funcion que llamara a nuestro servidor.

def main():
    host="localhost"
    port= 9990
    server = ThreadServer((host,port),MiTcpHandler)
    server_thread = threading.Thread(target=server.serve_forever)
    server_thread.start()
    print "server corriendo..."

main()
