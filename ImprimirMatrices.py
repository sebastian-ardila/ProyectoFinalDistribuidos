import fractions
import string
import sys

def x(M):
    """Devuelve el numero de filas j"""
    return M[1][0]

def y(M):
    """Devuelve el numero de columnas"""
    return M[1][1]

def fila(M, f):
    """Devuelve la fila f de la matriz M"""
    if f<=x(M) and f>=1:
        return M[0][(f-1)*y(M):((f-1)*y(M))+y(M)]

def imprime(M):
    """Imprime la matriz de forma ordenada"""
    string=""
    print("")
    for f in range(1, x(M)+1):
        for n in fila(M, f):
            if n<10:
                string=string+"   "+str(n)
            elif n<100:
                string=string+"  "+str(n)
            else:
                string=string+" "+str(n)
        print(string)
        string=""
    print("")