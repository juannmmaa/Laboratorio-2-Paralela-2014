__author__ = 'Christopher Salvatierra L.'



from mpi4py import MPI
import numpy as np
from PIL import Image,ImageChops
import StringIO

comm = MPI.COMM_WORLD  # comunicador entre dos procesadores #

rank = comm.rank     # id procesador actual #
size = comm.size     # tamano procesador #


def convertirImgMatrixRGB(img):
    return np.array(img.convert("RGB"))

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

def aplicarReflejo(arreglo):
    img = Image.fromarray(arreglo)
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

    #arreglo = np.vstack((imgMatriz,copiaInvertida))
    arreglo = copiaInvertida

    #imgInvertida = Image.fromarray(arreglo)
    return arreglo

#funcion que recibe la ruta de imagen y distribuye los trozos horizontales a cada procesador excepto el cero
def divisionTareaImagen(ruta):
    img=Image.open(ruta)
    imgSize=img.size
    largo=imgSize[1]
    ancho=imgSize[0]
    tamanoParte=largo/(size-1)  #(size-1) es para no incluir el procesador cero
    xInicio=0
    yInicio=0
    tamPar=tamanoParte
    for i in range(1,size):
        parteImgEnvio=img.crop((xInicio,yInicio,ancho,tamPar))
        tamPar=tamPar+tamanoParte
        yInicio=yInicio+tamanoParte
        rutaSalida="photoCut"+str(i)+".png"
        parteImgEnvio.save(rutaSalida)
        arrImg=convertirImgMatrixRGB(parteImgEnvio)
        comm.send(arrImg,dest=i)

def main():
    if rank==0:
        ruta="imagenMuestra.jpg"
        divisionTareaImagen(ruta)
    if rank!=0:
        arrTrabajo=comm.recv(source=0)    #cada procesador recibe un arreglo RGB que contiene un trozo horizontal de la imagen
        arrImgSalida=aplicarReflejo(arrTrabajo)    #enviar el arreglo RGB a transformarlo en arreglo negativo de la imagen
        comm.send(arrImgSalida,dest=0)
    if rank==0 :       #recibe los arreglos y los junta uno abajo del otro
        for i in range(1,size):
            if i > 1:
                construcImg = np.concatenate((comm.recv(source=i),construcImg))


            if i == 1:
                construcImg = comm.recv(source=i)

        img = Image.open("imagenMuestra.jpg")
        imgOriginal = convertirImgMatrixRGB(img)
        arreglo = np.vstack((imgOriginal,construcImg))
        imgContrucFinal=Image.fromarray(arreglo)
        imgContrucFinal.save("resultado.jpg")



import time #Libreria
starting_point=time.time() #Donde quiere empezar a calcular el tiempo
main()
elapsed_time=time.time()-starting_point #calculo
print ""
print "Time [seconds]: " + str(elapsed_time) #segundos
