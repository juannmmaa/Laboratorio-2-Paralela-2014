import numpy as np
from PIL import Image


# convertimos imagen a RGB para cambiar tonalidades rojas, azules y verdes.
def convertirImgMatrixRGB(img):
    return np.array(img.convert("RGB"))

# Primer paso para aplicar efecto infrarrojo a imagen es aplicar negativo
def convertirImgNegativo(img):
    arrImg = convertirImgMatrixRGB(img)
    for i in range(img.size[1]):
        for j in range(img.size[0]):
            arrImg[i][j] = 255-arrImg[i][j]
    imgNegativo = Image.fromarray(arrImg)
    return imgNegativo

def rgb(img):
    arrImg=convertirImgMatrixRGB(img)
    r=170
    g=0
    b=100
    for i in range(img.size[1]):
        for j in range(img.size[0]):
            arrImg[i][j][0] = (arrImg[i][j][0]+r)/2
            arrImg[i][j][1] = (arrImg[i][j][1]+g)/2
            arrImg[i][j][2] = (arrImg[i][j][2]+b)/2
    imgRGB=Image.fromarray(arrImg)
    return imgRGB

# ... Aun no sabemos si nos sirve utilizar esta funcion. 
def sumarImagenes(img1,img2):
    ALFA=0.5
    arrImg1=convertirImgMatrixRGB(img1)
    arrImg2=convertirImgMatrixRGB(img2)
    for i in range(img1.size[1]):
        for j in range(img1.size[0]):
            sumaPixel= (arrImg1[i][j]*(1-alfa))+(arrImg2[i][j]*(alfa))
            arrImg1[i][j]=sumaPixel
    imgSuma=Image.fromarray(arrImg1)
    return imgSuma

def main():
    img = Image.open('1.jpg')
    imgNegativo = convertirImgNegativo(img)
    imgfinal=rgb(imgNegativo)
    imgfinal.save("output.png")
main()
