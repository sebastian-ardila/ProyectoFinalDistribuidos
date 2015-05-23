# -*- coding: utf-8 -*-

#Version 0.1 del proyecto sistemas distribuidos
#Sebastian Ardila
#Cristian Ciro
#Esta parte del proyecto se comunica con el servidor para solicitar servicios.

import socket

#--------------------------------------------------
#funcion que limpia la pantalla
def clear():
		if os.name == "posix":
			os.system ("clear")
		elif os.name == ("ce", "nt", "dos"):
			os.system ("cls")

#--------------------------------------------------
#funcion que cierra el Cliente
def cerrarCliente():
    timeSeconds = 1
    count = 3
    while count > 0:
        print "cerrando el programa en" + count
        time.sleep(timeSeconds)
        count -=1
    clear()
    sock.close()
    exit()

#--------------------------------------------------
#funcion que hace el factorial de un numero
def factorialMenu(opcion):
    print " ------------------------------------------ "
    print "| Escogiste Factorial.                     |"
    print "| Escribe menu() para ir al menu.          |"
    print "| Escribe salir() para salir del programa. |"
    print " ------------------------------------------ "


    mensaje = 'valor invalido'
    while mensaje == 'valor invalido':
        mensaje = raw_input("Ingrese el valor: ")
        mensajeAenviar = str(opcion) + mensaje
        print mensajeAenviar ######################################################

        if mensaje == 'menu()':
            clear()
            continue

        if mensaje == 'salir()':
            cerrarCliente()

        #convierte mensaje a Unicode para poder usar la funcion isnumeric() y saber si es un numero
        mensajeUnicode = unicode(mensaje, "utf-8")
        if mensajeUnicode.isnumeric() == True:
            #mensajeSTR = mensajeU.encode('ascii','ignore')
            sock.send(mensajeAenviar)

        else:
            print "valor invalido"
            time.sleep(1)
            clear()

#--------------------------------------------------
#funcion que hace la potencia de un numero
def potenciaMenu(opcion):
    print " ------------------------------------------ "
    print "| Escogiste Potencia.                      |"
    print "| Escribe menu() para ir al menu.          |"
    print "| Escribe salir() para salir del programa. |"
    print " ------------------------------------------ "

    mensaje = 'valor invalido'

    while mensaje == 'valor invalido':
        mensaje = raw_input("Ingrese el valor: ")
        mensajeAenviar = str(opcion) + mensaje
        print mensajeAenviar ######################################################

        if mensaje == 'menu()':
            clear()
            continue

        if mensaje == 'salir()':
            cerrarCliente()

        #convierte mensaje a Unicode para poder usar la funcion isnumeric() y saber si es un numero
        mensajeUnicode = unicode(mensaje, "utf-8")
        if mensajeUnicode.isnumeric() == True:
            #mensajeSTR = mensajeU.encode('ascii','ignore')
            sock.send(mensajeAenviar)

        else:
            print "valor invalido"
            mensaje = 'valor invalido'
            time.sleep(1)
            clear()

#--------------------------------------------------
#funcion que invierte una matriz
def InvertirMatrizMenu(opcion):

    print " ------------------------------------------ "
    print "| Escogiste Invertir una matriz.           |"
    print "| Escribe menu() para ir al menu.          |"
    print "| Escribe salir() para salir del programa. |"
    print " ------------------------------------------ "

    while True:
        mensaje = raw_input("Ingrese el valor: ")
        mensajeAenviar = str(opcion) + mensaje
        print mensajeAenviar ######################################################

        if mensaje == 'menu()':
            clear()
            continue

        if mensaje == 'salir()':
            cerrarCliente()

        else:
            sock.send(mensajeAenviar)
            break


#--------------------------------------------------
#funcion muestra la hora del server (Utilizando el Algoritmo de Berkeley) si lo tuvieramos xD
def verHoraServer(opcion):
    pass

#--------------------------------------------------
#funcion que muestra un menu y permite escoger una opcion
def menu():

    opcion = 0
    while True:
        print " -----------Menu------------"
        print "| 1) Factorial              |"
        print "| 2) Potencia               |"
        print "| 3) Invertir Matriz        |"
        print "| 4) Ver hora del Servidor  |"
        print "| 5) Salir                  |"
        print " ---------------------------"

        opcion = raw_input("Ingresa una Opcion: ")
        clear()

        if opcion == 5:
            cerrarCliente()
        else:
            try:
                if opcion == 1:
                    factorialMenu(opcion)

                if opcion == 2:
                    potenciaMenu(opcion)

                if opcion == 3:
                    InvertirMatrizMenu(opcion)

                if opcion == 4:
                    verHoraServer(opcion)

                else:
                    print "opcion no valida"

            except:
                print "no se pudo mandar la opcion"
                opcion = 5

    sock.close()
    exit()

#funcion principal
def main():
	print "Hola soy el cliente"
	msj=""
	host, port = "localhost", 9990
    sock=socket.socket()
    sock.connect((host,port))
    menu()

main()
