__author__ = 'Diego Navia F.'


import numpy as np
from PIL import Image


# convierte una imagen tipo Imagen (de la libreria PIL) en una matriz(ETD) con la informacion RGB de la imagen
def convertirImgMatrixRGB(img):
    return np.array(img.convert("RGB"))

# convierte una imagen tipo Imagen (de la libreria PIL) a imagen en Negativo
# procedimiento : multiplica por base 255 cada casilla de la matriz RGB para convertir la imagen en negativo
def convertirImgNegativo(img):
    arrImg=convertirImgMatrixRGB(img)
    for i in range(img.size[1]):
        for j in range(img.size[0]):
            arrImg[i][j]=arrImg[i][j]*255
    imgNegativa=Image.fromarray(arrImg)
    return imgNegativa



def main():
    img=Image.open("ViendoFacebook.png")
    imgNegativa=convertirImgNegativo(img)
    imgNegativa.save("output3.png")    #guarda la imagen negativo

main()
