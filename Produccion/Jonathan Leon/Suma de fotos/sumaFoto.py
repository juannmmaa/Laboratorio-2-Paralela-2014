__author__ = 'jonathan'


import numpy as np
from PIL import Image

#Nivel de transparencia de imagen 1
ALFA=0.3

def convertirImgMatrixRGB(img):
    return np.array(img.convert("RGB"))

#suma las imagenes pixel a pixel, usando un valor alfa para sacar una proporcion de mezcla entre imagenes
def sumarImagenes(img1,img2,alfa):
    arrImg1=convertirImgMatrixRGB(img1)
    arrImg2=convertirImgMatrixRGB(img2)
    for i in range(img1.size[1]):
        for j in range(img1.size[0]):
            sumaPixel= (arrImg1[i][j]*(alfa))+(arrImg2[i][j]*(1-alfa))
            arrImg1[i][j]=sumaPixel
    imgSuma=Image.fromarray(arrImg1)
    return imgSuma

def main():
    img1=Image.open("galaxia.jpg")
    img2=Image.open("barco.jpg")
    imagenSumada=sumarImagenes(img1,img2,ALFA)
    imagenSumada.save("resultado.jpg")

main()


