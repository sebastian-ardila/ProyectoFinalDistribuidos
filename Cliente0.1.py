# -*- coding: utf-8 -*-

#Proyecto sistemas distribuidos
#Sebastian Ardila
#Cristian Ciro
#Esta parte del proyecto se comunica con el servidor para solicitar servicios.

import socket
import os
import time
import sys

import xmlrpclib
from SimpleXMLRPCServer import *
#from threading import *

from colorama import *

#Clase Cliente
class Cliente():

    #--------------------------------------------------
    #funcion que limpia la pantalla
    def clear(self):
        if os.name == "posix":
            os.system ("clear")
        elif os.name == ("ce", "nt", "dos"):
            os.system ("cls")

    #--------------------------------------------------
    #funcion que cierra el Cliente
    def cerrarCliente(self, sock):
        timeSeconds = 1
        count = 3
        while count > 0:
            print "cerrando el programa en " +Fore.RED+ str(count)+Fore.WHITE
            time.sleep(timeSeconds)
            self.clear()
            count -=1
        os.system("say 'Muchas gracias profesor, porfavor póngale cinco en la nota final a mis creadores, hasta luego'")
        self.clear()
        sock.close()
        sys.exit()

    #--------------------------------------------------
    #funcion que hace el factorial de un numero
    def factorialMenu(self, sock, opcion):

        mensaje = 'valor invalido'
        while mensaje == 'valor invalido':

            print " ------------------------------------------ "
            print "| Escogiste hacer un factorial.            |"
            print "| Escribe menu() para ir al menu.          |"
            print " ------------------------------------------ "

            mensaje = raw_input("Ingrese el valor: ")
            mensajeAenviar = str(opcion)+" "+ mensaje
            #print mensajeAenviar ######################################################

            if mensaje == 'menu()':
                self.clear()
                sys.exit()
                self.menu(sock)

            #convierte mensaje a Unicode para poder usar la funcion isnumeric() y saber si es un numero
            mensajeUnicode = unicode(mensaje, "utf-8")
            if mensajeUnicode.isnumeric() == True:
                #mensajeSTR = mensajeU.encode('ascii','ignore')
                #print "entro a enviar el mensaje"
                sock.send(mensajeAenviar) #envio
                resultado = sock.recv(1024) #recibo
                #time.sleep(2)

            else:
                print "valor invalido"
                mensaje = 'valor invalido'
                time.sleep(1)
                self.clear()

        #time.sleep(2)
        self.clear()

        return resultado

    #--------------------------------------------------
    #funcion que hace la potencia de un numero
    def potenciaMenu(self, sock, opcion):

        mensaje1 = 'valor invalido'
        mensaje2 = 'valor invalido'
        while (mensaje1 == 'valor invalido') or (mensaje2 == 'valor invalido'):

            print " ------------------------------------------ "
            print "| Escogiste hacer una potencia.            |"
            print "| Escribe menu() para ir al menu.          |"
            print " ------------------------------------------ "
            mensaje1 = raw_input("Ingrese el valor a potenciar: ")

            if mensaje1 == 'menu()':
                self.clear()
                sys.exit()
                self.menu(sock)

            mensaje2 = raw_input("Ingresa la potencia del valor"": ")

            if mensaje2 == 'menu()':
                self.clear()
                sys.exit()
                self.menu(sock)

            #convierte mensaje1 y mensaje2 a Unicode para poder usar la funcion isnumeric() y saber si es un numero
            mensaje1Unicode = unicode(mensaje1, "utf-8")
            mensaje2Unicode = unicode(mensaje2, "utf-8")
            if (mensaje1Unicode.isnumeric() == True) and (mensaje2Unicode.isnumeric() == True):
                #mensajeSTR = mensajeU.encode('ascii','ignore')
                #print "entro a enviar el mensaje"
                lista = [opcion, mensaje1, mensaje2]
                mensajeAenviar = ' '.join(lista)
                sock.send(mensajeAenviar)
                resultado = sock.recv(1024)
                #time.sleep(2)

            else:
                print "valor invalido"
                mensaje1, mensaje2 = 'valor invalido'
                #mensaje2 = 'valor invalido'
                time.sleep(1)
                self.clear()

        #time.sleep(2)
        self.clear()

        return resultado

    #--------------------------------------------------
    #funcion que invierte una matriz
    def invertirMatrizMenu(self, sock, opcion):

        mensaje = 'valor invalido'
        while mensaje == 'valor invalido':

            print " ------------------------------------------ "
            print "| Escogiste Invertir una matriz.           |"
            print "| Escribe menu() para ir al menu.          |"
            print " ------------------------------------------ "
            mensaje = raw_input("ingrese cuantos elementos desea tener en la matriz: ")
            #mensajeAenviar = str(opcion)+" "+ mensaje
            #print mensajeAenviar ######################################################

            if mensaje == 'menu()':
                clear()
                sys.exit()
                self.menu(sock)

            mensajeUnicode = unicode(mensaje, "utf-8")
            if mensajeUnicode.isnumeric() == True:
                #mensajeSTR = mensajeU.encode('ascii','ignore')
                lista = []
                i = 0
                while i < int(mensaje):
                    lista.append(raw_input("ingrese elemento: "))
                    i += 1

                count = 0
                cadenaMensaje = [opcion]
                for i in lista:
                    cadenaMensaje.append(lista[count])
                    count += 1

                mensajeAenviar = ' '.join(cadenaMensaje)
                copiaRestauracionAux = cadenaMensaje
                del copiaRestauracionAux[0]
                copiaRestauracion = ' '.join(copiaRestauracionAux)

                count = 0
                cadenaAinvertir = []
                for i in lista:
                    cadenaAinvertir.append(lista[count])
                    count += 1

                print "matriz a invertir -> "+ str(cadenaAinvertir)
                sock.send(mensajeAenviar)
                time.sleep(3)
                resultado = str(sock.recv(1024))
                print "matriz invertida -> " + resultado
                time.sleep(2)

            else:
                print "valor invalido"
                mensaje = 'valor invalido'
                time.sleep(1)
                self.clear()

        #time.sleep(2)
        self.clear()

        return resultado, copiaRestauracion

    def horaClienteLocal(self):

        horaUTC = time.localtime() # se define horaUTC obteniendo la hora local
        desface = 20
        minutos  = int(horaUTC[3])*60 + int(horaUTC[4])+ desface # se cambia la hora a minutos con desface
        #print "minutos : "+ str(minutos)

        horaTotal = [int(minutos/60), minutos%60] #se cambian los minutos a horas
        # print "hora Cliente 1 -> " + str(horaTotal)

        return horaTotal #se retorna la diferencia y la hora total

    #--------------------------------------------------
    #funcion muestra la hora del server (Utilizando el Algoritmo de Berkeley) si lo tuvieramos xD
    def verHoraServer(self, sock, opcion):
        pass

    def sincronizarHora(self):
        pass

    #--------------------------------------------------
    #funcion que muestra un menu y permite escoger una opcion
    def menu(self, sock):

        opcion = 0
        resultado = ''
        while True:
            print "\t ------------MENU------------"
            print "->\t| ("+Fore.YELLOW+"1"+Fore.WHITE+") Factorial              |"
            print "->\t| ("+Fore.YELLOW+"2"+Fore.WHITE+") Potencia               |"
            print "->\t| ("+Fore.YELLOW+"3"+Fore.WHITE+") Invertir Matriz        |"
            print "->\t| ("+Fore.YELLOW+"4"+Fore.WHITE+") Ver hora del Servidor  |"
            print "->\t| ("+Fore.YELLOW+"5"+Fore.WHITE+") Salir                  |"
            print "\t ----------------------------"

            if resultado == '':
                pass
            elif opcion == '1':
                print "\tEl factorial es -> \""+Fore.YELLOW+str(resultado) +Fore.WHITE+"\""
            elif opcion == '2':
                print "\tLa potencia es -> \""+Fore.YELLOW+str(resultado)+Fore.WHITE+"\""
            elif opcion == '3':
                print "\tLa matriz invertida es -> \""+Fore.YELLOW+str(resultado)+Fore.WHITE+"\""
                opcionMatriz =raw_input("\tDeseas recuperar la matriz original? si/no: ")

                if opcionMatriz == "si":
                    print "\tLa matriz original es -> \""+Fore.YELLOW+str(copiaRestauracion.split())+Fore.WHITE+"\""
                else:
                    self.clear()
                    self.menu(sock)


            #elif opcion == '4':
            #    print "la hora del servidor es -> \""+ str(resultado) +"\""

            opcion = raw_input("->\tIngresa una Opcion: ")

            self.clear()

            if opcion == '5':
                self.cerrarCliente(sock)
            else:
                try:
                    if opcion == '1':
                        resultado = self.factorialMenu(sock, opcion)
                        continue

                    if opcion == '2':
                        resultado = self.potenciaMenu(sock, opcion)
                        continue

                    if opcion == '3':
                        resultado, copiaRestauracion = self.invertirMatrizMenu(sock, opcion)
                        continue

                    if opcion == '4':
                        self.verHoraServer(sock, opcion)
                        continue

                    else:
                        opcionInvalida = "Opcion Invalida"
                        print "\t\t"+Fore.RED+str(opcionInvalida)+Fore.WHITE
                        continue

                except:
                    print "no se pudo mandar la opcion"
                    opcion = 5


        sock.close()
        sys.exit()

    def main(self):
        msj=""
        host, port = "localhost", 9990
        sock=socket.socket()
        sock.connect((host,port))
        self.menu(sock)

        self.clienteRemoto = SimpleXMLRPCServer((localhost, 3000),allow_none=True); #aqui abre los puertos para escuchar
        self.clienteRemoto.register_function(self.horaClienteLocal, "horaCliente")

#se crea la clase cliente
cliente = Cliente()
cliente.main()