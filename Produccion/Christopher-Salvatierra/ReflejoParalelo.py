__author__ = 'Christopher Salvatierra L.'
# -*- coding: utf-8 -*-

import numpy as np
from StringIO import StringIO
import time
from mpi4py import MPI
from pylab import *
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

starting_point=time.time()

#Explicacion paralelo
#Para cada procesador ingresado por el terminal, ya sea "np"=4 o "np"=12 va a funcionar de la misma forma,
#la distribución para que los "np" procesadores, será dividir la cantidad total de datos
#por la cantidad de procesado, dejandolos de forma pareja. En el caso que sobren será asignado para
#el ultimo procesador. A continuación se describiran brevemente que realizarán cada función


comm = MPI.COMM_WORLD  # comunicador entre dos procesadores
rank = comm.rank     # id procesador actual
size = comm.size     # cantidad de procesadores a usar

# En esta funcion se mandara a cada procesador la cantidad de datos con la que trabajaran
# Si sobran datos para que sean parejos, se le asignara al ultimo procesador
def distribuirEnP(size,altura):
    if (rank == 0):
        cuoc = (altura) / (size-2) #c : cuociente
        rest = (altura) % (size-2) #r : resto
        conta = 0
        for p in range(size-2):
            if (p+1) != (size-2):
                conta = conta + cuoc
                comm.send(conta, dest = p+2)
            else:
                conta = conta+cuoc+rest
                comm.send(conta, dest = p+2)

# El procesador 0 recibirá las cantidad de datos con la que trabajará
# cada procesador para devolver los indice i y j hasta donde operará
def buscarRangoFinal(base,altura):
    if rank==2:
        p=2
        conta=0
        rangos_end=[]
        valor=0
        for i in range(altura):
            for j in range(base):
                if(valor==0):
                    valor=comm.recv(source=p)
                if conta==valor:
                    rangos_end = rangos_end + [i,j]
                    comm.send(rangos_end,dest=p)
                    rangos_end=[]
                    p = p + 1
                    conta = conta + 1
                    valor=0
                else:
                    conta = conta + 1

# convierte una imagen tipo Imagen (de la libreria PIL) en una matriz(ETD) con la informacion RGB de la imagen
def convertirImgMatrixRGB(img):
    return np.array(img.convert("RGB"))

def cortarImagen(x, y,base):
    #print "hol"
    im = Image.open('1.jpg')
    region = im.crop((0, x, base, y))
    region.save("cut"+str(rank)+".jpg")
    factor = 0.5
    #data= np.array(region.convert("RGB"))
    #mezclarRGB(region,r,g,b)
    #aplicarBrillo(im,factor)
    aplicarReflejo(im)

def rotar90(img):
    arrImg = convertirImgMatrixRGB(img)
    n = img.size[0]
    m = img.size[1]
    final = np.array(Image.new("RGB",(m,n)))
    for i in range(n): #fila
        for j in range(m): #columna
            final[i][j] = arrImg[::, ((i*-1)-1)][j]
    imgColor = Image.fromarray(final)
    return imgColor

def rotar180(img):
    return rotar90(rotar90(img)) #debido a que el algoritmo de cambio de posicion es el mism

def aplicarReflejo(img):
    inv = img #se hace una copia de la imagen
    inv = rotar180(inv) #se gira

    copiaInvertida = convertirImgMatrixRGB(inv) #se convierten en matrices ambas imagenes

    imgMatriz = convertirImgMatrixRGB(img)
    filas = img.size[1]
    columnas = img.size[0]

    #Es una idea

    #print "MATRIZ ORIGINAL"
    #print imgMatriz
    for i in range (0,filas):
        for j in range(0,columnas):
            aux = imgMatriz[i][j]
            copiaInvertida[filas-1][j] = aux
        filas=filas-1
    #print "MATRIZ MODIFICADA"
    #print copiaInvertida

    arreglo = np.vstack((imgMatriz,copiaInvertida))

    imgInvertida = Image.fromarray(arreglo)
    #return imgInvertida
    imgInvertida.save("end.jpg")


#-------------MAIN---------------------

# Se sobre entiende que los delimitadores son espacios
data = Image.open("1.jpg")
data=convertirImgMatrixRGB(data)
altura = data.shape[0]
base = data.shape[1]

# El procesador 0 estará a cargo de mandar la cantidad de datos
# para cada procesador
if rank == 0:
    print ""
    print "altura,base: ",altura,base
    distribuirEnP(size,altura)

if rank >= 2:
    # Recibe la cantidad de datos en cada procesador
    fin = comm.recv(source=0)
    #fin = fin - 1
    #envia los datos con que finalizan al siguiente procesador para que lo usen como inicio
    if size != 3:
        if rank == 2:
            ini = 0
            i = 1
            if size > 0:
                comm.send(fin, dest=3)
    else:
        ini=0
        comm.send(fin,dest=2)
    # Hasta los p procesadores
    if size != 3:
        if rank !=2:
            ini=comm.recv(source=rank-1)
            if (rank+1)<size:
                comm.send(fin,dest=rank+1)
    else:
        ini=comm.recv(source=2)
    print "rank ",rank,", ini,fin :",ini,",",fin

    #r,g,b componentes del color a mezclar en decimales
    # 255,0,0 rojo


    cortarImagen(ini,fin,base)

if rank ==2:
#    Calculo de tiempo
    elapsed_time=time.time()-starting_point
    elapsed_time_int = int(elapsed_time)
    print "Parallel Time [seconds]: " + str(elapsed_time)
    print ""
