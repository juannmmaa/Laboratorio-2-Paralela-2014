#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'cpina'

'''
versión 1.0 de hdr

	falta optimizar el proceso de difuminación de pixeles y la superposición de capas
'''

import numpy as np
from PIL import Image
from PIL import ImageEnhance
import sys

#Nivel de transparencia de imagen 1, para que queden igualmete mezcladas se debe usar un alfa=0.5
oscuro=0.4
claro=2.5

def convertirImgMatrixRGB(img):
    return np.array(img.convert("RGB"))

#aplicar brillo con libreria PIL
def aplicarBrillo(img,factor):
    imagen = ImageEnhance.Brightness(img)
    imConBrillo = imagen.enhance(factor) #si el factor esta entre 0.0 y 1.0 la imagen se opacara, de ahi en mas aumentara 
    return imConBrillo					 #el brillo, y si el valor es menor que 0 la imagen queda completamente negra


#resta los niveles de luminosidad de cada imagen para lograr el efecto hdr.
def restabrillo(img1,img2):
    arrImg1=convertirImgMatrixRGB(img1)
    arrImg2=convertirImgMatrixRGB(img2)
    for i in range(img1.size[1]):
        for j in range(img1.size[0]):
            sumaPixel= (arrImg1[i][j]-arrImg2[i][j])
            arrImg1[i][j]=sumaPixel
    imgSuma=Image.fromarray(arrImg1)
    return imgSuma



if __name__ == '__main__':
	img1=Image.open("orig_1.jpg")
	oscura=aplicarBrillo(img1,oscuro)
	oscura.save("oscuro.jpg")		#esta capa es innecesaria guardarla
	clara=aplicarBrillo(img1,claro)
	clara.save("clara.jpg")			#esta capa es innecesaria guardarla
	mala=restabrillo(clara, oscura)
	mala.save("hdr.jpg")
