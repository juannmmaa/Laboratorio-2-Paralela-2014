from __future__ import division 
__author__ = 'jonathan'
# -*- coding: utf-8 -*-

import numpy as np
from PIL import Image,ImageOps
import time

def convertirImgMatrixRGB(img):
    return np.array(img.convert("RGB"))

#Genera un valor entre 0 y 1 a partir de un pixel en escala de grises
#Mientras mas alto sea , el valor devuelto sera mas cercano a 1 (opacidad maxima)
def obtenerAlfa(pixel):
    return pixel[0]/255

#Pega una imagen encima de un fondo, usando una mascara para generar las zonas transparentes de esta.
def componerImagen(fpFondo,fpImg,fpMascara):

    fondo=Image.open(fpFondo)  #el fondo manda, no lo tocamos por nada
    img=Image.open(fpImg).resize(fondo.size)#redimensionamos la imagen que pegaremos
    mascara=Image.open(fpMascara).resize(fondo.size)# y la respectiva mascara.
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
    starting_point=time.time()
    imagenCompuesta=componerImagen("galaxia.jpg","barco.jpg","alfaBarco.jpg")
    imagenCompuesta.save("output.png")
    elapsed_time=time.time()-starting_point
    print ""
    print "Serial Time [seconds]: " + str(elapsed_time)

main()
