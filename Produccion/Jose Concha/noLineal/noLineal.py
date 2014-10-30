__author__ = 'jose'
from PIL import Image
import numpy as np
import time
inicio = time.time()
def convertirImgMatrixRGB(img):
    return np.array(img.convert("RGB"))
def medio(arr):
    n = len(arr)
    if n%2 ==0:
        return int(arr[n/2])+int(arr[(n/2)+1])/2
    else:
        return arr[(n/2)]
def maximo(arr):
    n = len(arr)
    return arr[n-1]
def filtroLineal(img):
    arrImg=convertirImgMatrixRGB(img)
    arrAux = arrImg
    for z in range(3):
        for x in range(len(arrAux)):
            for y in range(len(arrAux[0])):
                suma = []
                for i in range(3):
                    for j in range(3):
                        try:
                            suma.append( arrImg[x-1+i][y-1+j][z])
                        except IndexError:
                            pass
                suma=sorted(suma)
                arrAux[x][y][z]=medio(suma)
                del suma
    linealImg = Image.fromarray(arrAux)
    return linealImg
def main():
    img = Image.open('Lenna.png')
    convImg = filtroLineal(img)
    convImg.save('nlLenna0.png')

main()

final = time.time()-inicio
print "Serial time[seconds] = " + str(final)