__author__ = 'francisco'

import numpy as np
from StringIO import StringIO
import time
from mpi4py import MPI
from pylab import *
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

def cortarImagen( x, y):
    im = Image.open('output.png')
    data= np.array(im.convert("RGB"))
    region = im.crop((0, 0, 632, 94))
    region.save("new1", "PNG")
    region = im.crop((0, 94, 632, 188))
    region.save("new2", "PNG")
    region = im.crop((0, 188, 632, 282))
    region.save("new3", "PNG")
    region = im.crop((0, 282, 632, 376))
    region.save("new4", "PNG")
    region = im.crop((0, 376, 632, 474))
    region.save("new5", "PNG")


# convierte una imagen tipo Imagen (de la libreria PIL) en una matriz(ETD) con la informacion RGB de la imagen
def convertirImgMatrixRGB(img):
    return np.array(img.convert("RGB"))


# procedimiento : Suma los componentes R, G, B del pixel de la imagen con el color que se quiere
# y cada suma se divide en dos, obteniendo un promedio
def mezclarRGB(img,r,g,b):
    arrImg=convertirImgMatrixRGB(img)
    for i in range(img.size[1]/2):
        for j in range(img.size[0]):
            arrImg[i][j][0] = (arrImg[i][j][0]+r)/2
            arrImg[i][j][1] = (arrImg[i][j][1]+g)/2
            arrImg[i][j][2] = (arrImg[i][j][2]+b)/2
    imgRGB=Image.fromarray(arrImg)
    return imgRGB

def main():
    starting_point=time.time()
    img=Image.open("1.jpg")

    #r,g,b componentes del color a mezclar en decimales
    # 255,0,0 rojo
    r=255
    g=0
    b=0
    imgRGB=mezclarRGB(img,r,g,b)
    imgRGB.save("output.png")    #guarda la imagen RGB
    elapsed_time=time.time()-starting_point
    print ""
    print "Serial Time [seconds]: " + str(elapsed_time)

main()
#ruta='/home/francisco/Documentos/Laboratorio-2-Paralela-2014/Produccion/Francisco Ramirez/Estrategia Paralelo/'
#cortarImagen(ruta,0,236)
cortarImagen(0,236)


