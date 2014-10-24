__author__ = 'francisco'
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  8 14:31:26 2014

@author: paralela
"""
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
def distribuirEnP(size,base,altura):
    if (rank==0):
        cuoc= (base*altura)/size #c : cuociente
        rest= (base*altura)%size #r : resto
        conta=0
        for p in range (size):
            if (p+1)!=size:
                conta=conta+cuoc
                comm.send (conta, dest = p)
            else:
                conta=conta+cuoc+rest
                comm.send (conta, dest = p)

# El procesador 0 recibirá las cantidad de datos con la que trabajará
# cada procesador para devolver los indice i y j hasta donde operará
def buscarRangoFinal(size,base,altura):
    if rank==0:
        p=0
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

#-------------MAIN---------------------

# Se sobre entiende que los delimitadores son espacios
data = Image.open("0,3 megapixeles 1.jpg")
data=convertirImgMatrixRGB(data)
altura = data.shape[0]
base = data.shape[1]
if rank ==0:
    print "altura,base: ",altura,base
    #print data
# El procesador 0 estará a cargo de mandar la cantidad de datos
# para cada procesador
if rank == 0:
    distribuirEnP(size,base,altura)

# Recibe la cantidad de datos en cada procesador
rango = comm.recv(source=0)
rango = rango-1
comm.send(rango, dest=0)
#print "rank ",rank,", cantidad :",rango

# Con la cantidad de datos se buscara el rango donde terminara de procesar en la matriz
if rank == 0:
    buscarRangoFinal(size, base, altura)

# Con la posición de termino se mandarán como punto de inicio para los procesadores siguientes
# Primero se inicia el procesador 1
fin = comm.recv(source=0)
#print "rank ",rank,", fin : ",fin
if size != 1:
    if rank==0:
        ini=[0,0]
        i=1
        if size>0:
            comm.send(fin,dest=1)
else:
    ini=[0,0]
    comm.send(fin,dest=0)

# Hasta los p procesadores
if size != 1:
    if rank !=0:
        ini=comm.recv(source=rank-1)
        if (rank+1)<size:
            comm.send(fin,dest=rank+1)
else:
    ini=comm.recv(source=0)
print "rank ",rank,", rango :",ini,fin

if rank ==0:
#    Calculo de tiempo
    elapsed_time=time.time()-starting_point
    elapsed_time_int = int(elapsed_time)
    print ""
    print "Parallel Time [seconds]: " + str(elapsed_time)
#    elapsed_time_minutes = elapsed_time_int/60
#    elapsed_time_seconds = elapsed_time_int%60
#    print "Time [min:sec]: "+ str(elapsed_time_minutes) + ":" + str(elapsed_time_seconds)

