import fractions
import string
import sys

def error(n):
    if n==2: sys.stderr.write("Inserte una matriz cuadrada")
    elif n==3:  sys.stderr.write("La matriz no tiene inversa")

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

def inversa(M):
    """Devuelve la matriz inversa a M"""
    if cuadrada(M):
        detm=det(M)
        if detm!=0:
            Madj=matrizAdjunta(M)
            return traspuesta(prodnr(Madj, (fractions.Fraction(1 , detm))))
        else:
            return error(3)
    else:
        return error(2), error(3)

def matrizAdjunta(M):
    """Calcula la matriz adjunta de M"""
    if not cuadrada(M):
        return None
    if x(M)==1:
        return M[:]
    if x(M)==2:
        A=[ [ M[0][3],-M[0][2],-M[0][1], M[0][0] ], [2, 2] ]
        return A
    A=Mnula(x(M), y(M))
    for i in range(1, x(M)+1):
        for j in range(1, y(M)+1):
            subM=submatriz(M, i, j)
            A[0][(i-1)*y(M)+j-1]=(-1)**(i+j)*det(subM)
    return A

def Mnula(x, y):
    """ Crea una matriz nula"""
    A=[0]*x*y
    return [A, [x, y]]

def submatriz(M, f, c):
    """Elimina la fila f y la columna c de una matriz (menor complementario)"""
    if x(M)<2:
        sys.stderr.write("Imposible eliminar la unica fila de una matriz al tratar de extraer una submatriz")
        return None
    if y(M)<2:
        sys.stderr.write("Imposible eliminar la unica columna de una matriz al tratar de extraer una submatriz")
    A=[M[0][:], M[1][:]]
    del A[0][(f-1)*y(A): f*y(A)]
    for i in range(len(A[0])-y(A)+c, 0,-y(A)):
        del A[0][i-1]
    A[1][0]=A[1][0]-1
    A[1][1]=A[1][1]-1
    return A

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

def prodnr(M, k):
    """Producto de un numero real por una matriz"""
    A=[]
    for i in range(y(M)*x(M)):
        A=A+[M[0][i]*k]
    return [A, [y(M), x(M)]]


def det(M):
    """Resuelve el determinante de la matriz M"""
    if cuadrada(M):
        if y(M)==1:
            return M[0][0]
        elif y(M)==2:
            return (M[0][0]*M[0][3])-(M[0][2]*M[0][1])
        elif y(M)==3:
            return ((M[0][0]*M[0][4]*M[0][8])+(M[0][2]*M[0][3]*M[0][7])+(M[0][1]*M[0][5]*M[0][6]))-((M[0][2]*M[0][4]*M[0][6])+(M[0][1]*M[0][3]*M[0][8])+(M[0][0]*M[0][5]*M[0][7]))
        else:
            f1=fila(M, 1)
            deter=0
            for n in range(y(M)):
                subM=[]
                for nfila in range(2, y(M)+1):
                    fi=fila(M, nfila)
                    del fi[n]
                    subM+=fi
                deter+=f1[n]*((-1)**n)*det([subM, [y(M)-1, y(M)-1]])
            return deter

def traspuesta(M):
    """Devuelve la matriz traspuesta a M"""
    A=[]
    for col in range(1, y(M)+1):
        A+=columna(M, col)
    return [A, [y(M), x(M)]]

def columna(M, c):
    """Devuelve la columna c de la matriz M"""
    if c<=y(M) and c>=1:
        A=[]
        for i in range(1, x(M)+1):
            l=fila(M, i)
            A=A+[l[c-1]]
        return A

def cuadrada(M):
    """Verifica que se trata de una matriz cuadrada"""
    if x(M)==y(M):
        return True
    else:
        return False

