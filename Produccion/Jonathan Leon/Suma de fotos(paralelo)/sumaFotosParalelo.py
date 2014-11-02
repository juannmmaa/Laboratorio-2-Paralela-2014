__author__ = 'jonathan'
# -*- coding: utf-8 -*-

from mpi4py import MPI
import numpy as np
import time
from PIL import Image

ALFA=0.5
comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.rank

def convertirImgMatrixRGB(img):
    return np.array(img.convert("RGB"))

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

def cortarImagen(img,nombre,x, y):

    region = img.crop((0, x, img.size[0], y))
    region.save(nombre+"-"+str(rank)+".jpg")
    data= np.array(region.convert("RGB"))

def unirImagen():
    #cargo los cortes sumados y los junto con np.stack, no tiene mayor ciencia...
    im1 = Image.open('sum'+str(rank)+'.jpg')
    im1 = np.array(im1.convert("RGB"))
    for i in range(3, size):
        im2 = Image.open('sum'+str(i)+'.jpg')
        im2 = np.array(im2.convert("RGB"))
        im1=np.vstack((im1, im2))
    im1=Image.fromarray(im1)
    im1.save("resultado.jpg")

def sumarCortes():

    #cargo los cortes respectivos de ambas imagenes
    img1=Image.open("img1-"+str(rank)+".jpg")
    img2=Image.open("img2-"+str(rank)+".jpg")

    #las paso a array y las trabajo igual que el script en secuencial...
    arrImg1=convertirImgMatrixRGB(img1)
    arrImg2=convertirImgMatrixRGB(img2)
    for i in range(img1.size[1]):
        for j in range(img1.size[0]):
            sumaPixel= (arrImg1[i][j]*(1-ALFA))+(arrImg2[i][j]*(ALFA))
            arrImg1[i][j]=sumaPixel
    imgSuma=Image.fromarray(arrImg1)
    imgSuma.save("sum"+str(rank)+".jpg") #guardo la suma de 2 cortes como una nueva imagen.


def main():
    starting_point=time.time()
    img1=Image.open("flor.jpg")
    img2=Image.open("calle.jpg").resize(img1.size)
    arrImg1=convertirImgMatrixRGB(img1)
    arrImg2=convertirImgMatrixRGB(img2)

    altura=arrImg1.shape[0]
    base=arrImg1.shape[1]

    if rank==0: # el nodo 0 distribuye los rangos de trabajo (rango de filas)
        print ""
        print "altura,base",altura,base
        distribuirEnP(size,altura)

    if rank >=2:   #se que esta parte de codigo hace algo importante, pero de momento
        fin=comm.recv(source=0) #funciona para distribuir los rangos equitativamente, asi que funca y punto xD
        if size!=3:
            if rank==2:
                ini=0
                i=1
                if size>0:
                    comm.send(fin,dest=3)
        else:
            ini=0
            comm.send(fin,dest=2)
        if size!=3:
            if rank!=2:
                ini=comm.recv(source=rank-1)
                if(rank+1)<size:
                    comm.send(fin,dest=rank+1)
        else:
            ini=comm.recv(source=2)
        #cada nodo imprime sus rangos por consola,ademas corta las imagenes
        #en su rango correspondiente y guarda una imagen para ambas imagenes.
        #vale decir que cada nodo tiene una copia de las imagenes

        print "rank ",rank,", ini,fin :",ini,",",fin
        cortarImagen(img1,"img1",ini,fin)#corta imagen 1
        cortarImagen(img2,"img2",ini,fin)#corta imagen 2
        sumarCortes() #ahora se suman los cortes sumados


    if rank==2:
        #intentaremos unir las imagenes, se usa una secuencia try catch porque puede suceder que intentemos
        #unir imagenes que aun no esten listas, para que el programa no se caiga, lo volvemos a intentar
        #hasta que salga bien
        exito=0
        while exito==0:
            try:
                unirImagen()
                exito=1
            except:
                print "imagenes aun no listas, reintentando..."


    elapsed_time=time.time()-starting_point
    print ""
    print "Tiempo Paralelo [seconds]: " + str(elapsed_time)

main()
