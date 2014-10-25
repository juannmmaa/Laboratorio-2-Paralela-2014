__author__ = 'jose'
import numpy as np
from PIL import Image
def convertirImgMatrixRGB(img):
    return np.array(img.convert("RGB"))
def matrizNorma(arr):
    suma =0
    for i in range(3):
        for j in range(3):
            suma += arr[i][j]
    return suma
def filtroLineal(arrImg):
    arrAux = arrImg
    nucleo =[[.11,.11,.11],[.11,.11,.11],[.11,.11,.11]]
    for z in range(3):
        for x in range(len(arrAux)):
            for y in range(len(arrAux[0])):
                suma = 0
                for i in range(3):
                    for j in range(3):
                        try:
                            suma += int(arrImg[x-1+i][y-1+j][z]*nucleo[i][j])
                        except IndexError:
                            suma += 0
                arrAux[x][y][z]=suma
    return arrAux
def borde(arrImg):
    arrAux = arrImg
    nucleo =[[0,1,0],[1,-4,1],[0,1,0]]
    for z in range(3):
        for x in range(len(arrAux)):
            for y in range(len(arrAux[0])):
                suma = 0
                for i in range(3):
                    for j in range(3):
                        try:
                            suma += int(arrImg[x-1+i][y-1+j][z]*nucleo[i][j])
                        except IndexError:
                            suma += 0
                arrAux[x][y][z]=suma
    return arrAux
def convolucionImg(img, caso = 0):
    arrImg = convertirImgMatrixRGB(img)
    if caso ==0:
        arrAux = filtroLineal(arrImg)
    elif caso == 1:
        arrAux = borde(arrImg)
    convImg = Image.fromarray(arrAux)
    return convImg
def main():
    img = Image.open('Lenna.png')
    convImg = convolucionImg(img,1)
    convImg.save('convLenna.png')
main()