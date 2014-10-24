from __future__ import division
__author__ = 'Christopher Salvatierra L.'


import numpy as np
from PIL import Image
from PIL import ImageEnhance

# convierte una imagen tipo Imagen (de la libreria PIL) en una matriz(ETD) con la informacion RGB de la imagen
def convertirImgMatrixRGB(img):
    return np.array(img.convert("RGB"))


def aplicarReflejo(img):
    imgMatriz = convertirImgMatrixRGB(img)
    filas = img.size[1]
    columnas = img.size[0]
    filTotal = filas
    copia = imgMatriz
    print copia
    for i in range (filas):
        for j in range(columnas):
            fila = copia[i][j] #tomar la primera fila de la matriz y se copia en un arreglo

    return 0

def main():
    img=Image.open("imagenMuestra2.jpg")
    imgReflejo = aplicarReflejo(img)

main()
