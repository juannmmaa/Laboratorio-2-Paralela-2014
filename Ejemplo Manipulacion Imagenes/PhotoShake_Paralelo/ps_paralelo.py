__author__ = 'diogoalfa'



from mpi4py import MPI
import numpy as np
from PIL import Image,ImageChops
import StringIO

comm = MPI.COMM_WORLD  # comunicador entre dos procesadores #

rank = comm.rank     # id procesador actual #
size = comm.size     # tamano procesador #


# largo=imgSize[1]
# ancho=imgSize[0]
# print "largo :",largo
# print "Ancho :",ancho



def convertirImgMatrixRGB(img):
    return np.array(img.convert("RGB"))

#recibe un arreglo RGB de la imagen,lo convierte en negativo y retorna el arreglo negativo
def convertirImgNegativo(arrImg):
    for i in range(len(arrImg)): #largo
        for j in range(len(arrImg[0])):  #ancho
            arrImg[i][j] = 255-arrImg[i][j]
    return arrImg


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
        ruta="ViendoFacebook.png"
        divisionTareaImagen(ruta)
    if rank!=0:
        arrTrabajo=comm.recv(source=0)    #cada procesador recibe un arreglo RGB que contiene un trozo horizontal de la imagen
        arrImgSalida=convertirImgNegativo(arrTrabajo)    #enviar el arreglo RGB a transformarlo en arreglo negativo de la imagen
        comm.send(arrImgSalida,dest=0)
    if rank==0 :       #recibe los arreglos y los junta uno abajo del otro
        for i in range(1,size):
            if i > 1:
                construcImg = np.concatenate((construcImg,comm.recv(source=i)))
            if i == 1:
                construcImg = comm.recv(source=i)
        imgContrucFinal=Image.fromarray(construcImg)
        imgContrucFinal.save("IMAGENFINAL.png")



main()
