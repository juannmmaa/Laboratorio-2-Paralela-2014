__author__ = 'francisco'

import numpy as np
from PIL import Image


# convierte una imagen tipo Imagen (de la libreria PIL) en una matriz(ETD) con la informacion RGB de la imagen
def convertirImgMatrixRGB(img):
    return np.array(img.convert("RGB"))

# convierte una imagen tipo Imagen (de la libreria PIL) a imagen en Negativo
# procedimiento : multiplica por base 255 cada casilla de la matriz RGB para convertir la imagen en negativo
def mezclarRGB(img,R,G,B):
    arrImg=convertirImgMatrixRGB(img)
    print arrImg
    for i in range(img.size[1]):
        for j in range(img.size[0]):
            print str(i),",",str(j)
            print arrImg[i][j]
            arrImg[i][j][0] = (arrImg[i][j][0]+R)/2
            arrImg[i][j][1] = (arrImg[i][j][1]+G)/2
            arrImg[i][j][2] = (arrImg[i][j][2]+B)/2
            print arrImg[i][j]
    imgNegativa=Image.fromarray(arrImg)
    return imgNegativa



def main():
    img=Image.open("ViendoFacebook.png")
    R=191
    G=191
    B=191
    imgNegativa=mezclarRGB(img,R,G,B)
    imgNegativa.save("output3.png")    #guarda la imagen negativo

main()