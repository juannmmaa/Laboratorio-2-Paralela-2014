from __future__ import division 
__author__ = 'jonathan'

import numpy as np
from PIL import Image,ImageOps
import time

def convertirImgMatrixRGB(img):
    return np.array(img.convert("RGB"))

#Genera un valor entre 0 y 1 a partir de un pixel en escala de grises
#Mientras mas alto sea , el valor devuelto será mas cercano a 1 (opacidad maxima)
def obtenerAlfa(pixel):
    return pixel[0]/255

#Pega una imagen encima de un fondo, usando una mascara para generar las zonas transparentes de esta.
def componerImagen(fondo,img,mascara):
    arrFondo=convertirImgMatrixRGB(fondo)
    arrImg=convertirImgMatrixRGB(img)
    arrMascara=convertirImgMatrixRGB(mascara)
    for i in range(fondo.size[1]):
        for j in range(fondo.size[0]):
            alfa=obtenerAlfa(arrMascara[i][j])  #el alfa se usa para representar un nivel de transparencia de una imagen dada
            sumaPixel= (arrFondo[i][j]*(1-alfa))+(arrImg[i][j]*(alfa))#se suman los pixeles multiplicando la imagen por el alfa y el fondo por el complemento(ver informe)
            arrFondo[i][j]=sumaPixel
    imgCompuesta=Image.fromarray(arrFondo)
    return imgCompuesta

def main():
    elapsed_time=time.time()-starting_point
    fondo=Image.open("galaxia.jpg")
    img=Image.open("barco.jpg")
    mascara=Image.open("alfaBarco.jpg")
    imagenCompuesta=componerImagen(fondo,img,mascara)
    imagenCompuesta.save("output.png")
    print ""
    print "Serial Time [seconds]: " + str(elapsed_time)

main()
