__author__ = 'jonathan'


import numpy as np
from PIL import Image

#Nivel de transparencia de imagen 1, para que queden igualmete mezcladas se debe usar un alfa=0.5
ALFA=0.5

def convertirImgMatrixRGB(img):
    return np.array(img.convert("RGB"))

#mezcla 2 imagenes en una,el alfa es usado para definir el nivel de transparencia de las imagenes.
def sumarImagenes(img1,img2,alfa):
    arrImg1=convertirImgMatrixRGB(img1)
    arrImg2=convertirImgMatrixRGB(img2)
    for i in range(img1.size[1]):
        for j in range(img1.size[0]):
            sumaPixel= (arrImg1[i][j]*(1-alfa))+(arrImg2[i][j]*(alfa))
            arrImg1[i][j]=sumaPixel
    imgSuma=Image.fromarray(arrImg1)
    return imgSuma

def main():
    img1=Image.open("galaxia.jpg")
    img2=Image.open("barco.jpg")
    imagenSumada=sumarImagenes(img1,img2,ALFA)
    imagenSumada.save("resultado.jpg")

main()


