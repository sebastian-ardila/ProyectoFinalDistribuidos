# -*- coding: utf-8 -*-

#Version 0.1 del proyecto sistemas distribuidos
#Sebastian Ardila
#Cristian Ciro
#Esta parte del proyecto se comunica con el servidor para solicitar servicios.

import socket
import os
import time
import sys

#--------------------------------------------------
#funcion que limpia la pantalla
def clear():
    if os.name == "posix":
        os.system ("clear")
    elif os.name == ("ce", "nt", "dos"):
        os.system ("cls")

#--------------------------------------------------
#funcion que cierra el Cliente
def cerrarCliente(sock):
    timeSeconds = 1
    count = 3
    while count > 0:
        print "cerrando el programa en " + str(count)
        time.sleep(timeSeconds)
        clear()
        count -=1
    clear()
    sock.close()
    sys.exit()

#--------------------------------------------------
#funcion que hace el factorial de un numero
def factorialMenu(sock, opcion):

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
            clear()
            sys.exit()
            menu(sock)

        #convierte mensaje a Unicode para poder usar la funcion isnumeric() y saber si es un numero
        mensajeUnicode = unicode(mensaje, "utf-8")
        if mensajeUnicode.isnumeric() == True:
            #mensajeSTR = mensajeU.encode('ascii','ignore')
            #print "entro a enviar el mensaje"
            sock.send(mensajeAenviar)
            resultado = sock.recv(1024)
            #time.sleep(2)

        else:
            print "valor invalido"
            mensaje = 'valor invalido'
            time.sleep(1)
            clear()

    #time.sleep(2)
    clear()

    return resultado

#--------------------------------------------------
#funcion que hace la potencia de un numero
def potenciaMenu(sock, opcion):

    mensaje1 = 'valor invalido'
    mensaje2 = 'valor invalido'
    while (mensaje1 == 'valor invalido') or (mensaje2 == 'valor invalido'):

        print " ------------------------------------------ "
        print "| Escogiste hacer una potencia.            |"
        print "| Escribe menu() para ir al menu.          |"
        print " ------------------------------------------ "
        mensaje1 = raw_input("Ingrese el valor a potenciar: ")

        if mensaje1 == 'menu()':
            clear()
            sys.exit()
            menu(sock)

        mensaje2 = raw_input("Ingresa la potencia del valor"": ")

        if mensaje2 == 'menu()':
            clear()
            sys.exit()
            menu(sock)

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
            clear()

    #time.sleep(2)
    clear()

    return resultado

#--------------------------------------------------
#funcion que invierte una matriz
def invertirMatrizMenu(sock, opcion):

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
            menu(sock)

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
            clear()

    #time.sleep(2)
    clear()

    return resultado

#--------------------------------------------------
#funcion muestra la hora del server (Utilizando el Algoritmo de Berkeley) si lo tuvieramos xD
def verHoraServer(sock, opcion):
    pass

def sincronizarHora():
    pass

#--------------------------------------------------
#funcion que muestra un menu y permite escoger una opcion
def menu(sock):

    opcion = 0
    resultado = ''
    while True:
        print " -----------Menu-------------"
        print "| (1) Factorial              |"
        print "| (2) Potencia               |"
        print "| (3) Invertir Matriz        |"
        print "| (4) Ver hora del Servidor  |"
        print "| (5) Salir                  |"
        print " ----------------------------"

        if resultado == '':
            pass
        elif opcion == '1':
            print "El factorial es -> \""+ str(resultado) +"\""
        elif opcion == '2':
            print "La potencia es -> \""+ str(resultado) +"\""
        elif opcion == '3':
            print "La matriz invertida es -> \""+ str(resultado) +"\""
        #elif opcion == '4':
        #    print "la hora del servidor es -> \""+ str(resultado) +"\""

        opcion = raw_input("Ingresa una Opcion: ")

        clear()

        if opcion == '5':
            cerrarCliente(sock)
        else:
            try:
                if opcion == '1':
                    resultado = factorialMenu(sock, opcion)
                    continue

                if opcion == '2':
                    resultado = potenciaMenu(sock, opcion)
                    continue

                if opcion == '3':
                    resultado = invertirMatrizMenu(sock, opcion)
                    continue

                if opcion == '4':
                    verHoraServer(sock, opcion)
                    continue

                else:
                    print "opcion no valida"
                    continue

            except:
                print "no se pudo mandar la opcion"
                opcion = 5

    sock.close()
    sys.exit()

#funcion principal
def main():
    print "Hola soy el cliente"
    msj=""
    host, port = "localhost", 9990
    sock=socket.socket()
    sock.connect((host,port))
    menu(sock)

main()
