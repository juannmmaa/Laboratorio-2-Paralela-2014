__author__ = 'jose'
from PIL import Image
import numpy as np

def convertirImgMatrixRGB(img):
    return np.array(img.convert("RGB"))
def medio(arr):
    n = len(arr)
    if n%2 ==0:
        return (arr[n/2]+arr[(n/2)+1])/2

    else:
        return arr[(n/2)+1]
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
                sorted(suma)
                arrAux[x][y][z]=medio(suma)
                del suma
    linealImg = Image.fromarray(arrAux)
    return linealImg
def main():
    img = Image.open('Lenna.png')
    convImg = filtroLineal(img)
    convImg.save('nlLenna.png')
main()