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
    filas = img.size[1]
    columnas = img.size[0]

    '''filTotal = filas
    copia = imgMatriz #una matriz de copia para mantener la original
    print "LA MATRIZ ORIGINAL"
    print copia
    for i in range (0,filas):
        for j in range(0,columnas):
            fila = copia[i][j] #tomar la primera fila de la matriz y se copia en un arreglo
            #copia[i][j] = copia[(filas-1) -i][(columnas-1) -j]
            copia[(filas-1)-i][(columnas-1)-j] = fila #copia la fila obtenida al final de la matriz
    print "LA MATRIZ INVERTIDA"
    '''
    arreglo = np.vstack((imgMatriz,copiaInvertida))
    #print copiaInvertida
    imgInvertida = Image.fromarray(arreglo)
    return imgInvertida

def main():
    img=Image.open("imagenMuestra2.jpg")
    imgReflejo = aplicarReflejo(img)
    imgReflejo.save("reflejo.jpg")
main()
