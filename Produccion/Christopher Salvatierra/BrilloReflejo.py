from __future__ import division
__author__ = 'Christopher Salvatierra L.'


import numpy as np
from PIL import Image
from PIL import ImageEnhance




# convierte una imagen tipo Imagen (de la libreria PIL) en una matriz(ETD) con la informacion RGB de la imagen
def convertirImgMatrixRGB(img):
    return np.array(img.convert("RGB"))



#Trabajando en como matriz siempre
def aplicarBrillo(img,factor):
    arrImg=convertirImgMatrixRGB(img) #pasamos la imagen a una matriz para aplicar operaciones matematicas
    #si el factor es menor a cero la imagen se oscurece (rango 0 a -1)
    if factor <0:#para oscurecer la imagen
        for i in range(img.size[1]):
            for j in range(img.size[0]):
                brillo= lambda x: x*(1+factor)
                arrImg[i][j]=brillo(arrImg[i][j])
    #si el factor es mayor a cero se aclara (rango 0 a 1)
    else:#brillo
        for i in range(img.size[1]):
            for j in range(img.size[0]):
                brillo= lambda x: x+ (255-x)*factor
                arrImg[i][j]=brillo(arrImg[i][j])
    imgBrillante=Image.fromarray(arrImg) #Se convierte la matriz a imagen nuevamente para devolverla
    return imgBrillante

def main():
    img=Image.open("imagenMuestra2.jpg")
    print"Ingrese factor (debe ingresar valor decimal, entre -1 y 0 para oscurecer y entre 0 y 1 para aclarar"
    factor=input()
    imgBrillo = aplicarBrillo(img,factor)
    imgBrillo.save("resultado1.jpg")
    imgBrillo.show()


main()
