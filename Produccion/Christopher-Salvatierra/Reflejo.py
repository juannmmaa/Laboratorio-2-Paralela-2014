from __future__ import division
__author__ = 'Christopher Salvatierra L.'


import numpy as np
from PIL import Image
from PIL import ImageEnhance

# convierte una imagen tipo Imagen (de la libreria PIL) en una matriz(ETD) con la informacion RGB de la imagen
def convertirImgMatrixRGB(img):
    return np.array(img.convert("RGB"))


def aplicarReflejo(img):
    inv = img #se hace una copia de la imagen
    inv = inv.rotate(180) #se gira
    copiaInvertida = convertirImgMatrixRGB(inv) #se convierten en matrices ambas imagenes
    imgMatriz = convertirImgMatrixRGB(img)
    
    arreglo = np.vstack((imgMatriz,copiaInvertida))
    #print copiaInvertida
    imgInvertida = Image.fromarray(arreglo)
    return imgInvertida

def main():
    img=Image.open("imagenMuestra2.jpg")
    imgReflejo = aplicarReflejo(img)
    imgReflejo.save("reflejo.jpg")

import time #Libreria
starting_point=time.time() #Donde quiere empezar a calcular el tiempo
main()
elapsed_time=time.time()-starting_point #calculo
print ""
print "Serial Time [seconds]: " + str(elapsed_time) #segundos
