from numpy.matrixlib.defmatrix import matrix

__author__ = 'jose'
import numpy as np
from PIL import Image
import math
import time

def convertirImgMatrixRGB(img):
    return np.array(img.convert("RGB"))
def filtroLinealS(arrImg):
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
def filtroLinealS2(arrImg):
    arrAux = arrImg
    nucleo =[[.0625,.125,.0625],[.125,.25,.125],[.0625,.125,.0625]]
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
def filtroLinealR(arrImg):
    arrAux = arrImg
    nucleo =[[-1,-1,-1],[-1,9,-1],[-1,-1,-1]]
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
                if suma>255:
                    suma=255
                elif suma<0:
                    suma =0
                arrAux[x][y][z]=suma
    return arrAux
def convolucionImg(img, caso = 0):
    arrImg = convertirImgMatrixRGB(img)
    if caso ==0:
        arrAux = filtroLinealS(arrImg)
    elif caso == 1:
        arrAux = filtroLinealS2(arrImg)
    elif caso == 2:
        arrAux = filtroLinealR(arrImg)
    convImg = Image.fromarray(arrAux)
    return convImg
def main():
    ini_point=time.time()
    starting_point=time.time()
    img = Image.open('Lenna.png')
    convImg = convolucionImg(img)
    convImg.save('conv0.png')
    elapsed_time=time.time()-starting_point
    print "Convolucion 0 - Time [seconds]: " + str(elapsed_time)

    starting_point=time.time()
    convImg = convolucionImg(img,1)
    convImg.save('conv1.png')
    elapsed_time=time.time()-starting_point
    print "Convolucion 1 -  Time [seconds]: " + str(elapsed_time)

    starting_point=time.time()
    convImg = convolucionImg(img,2)
    convImg.save('conv2.png')
    elapsed_time=time.time()-starting_point
    print "Convolucion 2 -  Time [seconds]: " + str(elapsed_time)

    elapsed_time=time.time()-ini_point
    print ""
    print "Convolucion Total -  Time [seconds]: " + str(elapsed_time)
main()