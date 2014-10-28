__author__ = 'jose'
import numpy as np
from PIL import Image
import colorsys
import time

def convertirImgMatrixRGB(img):
    return np.array(img.convert("RGB"))
def convertirImgSepia(img):
    arrImg = convertirImgMatrixRGB(img)
    for i in range(img.size[1]):
        for j in range(img.size[0]):
            arrImg[i][j][0] = arrImg[i][j][0]*0.393 + arrImg[i][j][1]*0.769 + arrImg[i][j][2]*0.189
            arrImg[i][j][1] = arrImg[i][j][0]*0.349 + arrImg[i][j][1]*0.686 + arrImg[i][j][2]*0.168
            arrImg[i][j][2] = arrImg[i][j][0]*0.272 + arrImg[i][j][1]*0.534 + arrImg[i][j][2]*0.131
    imgSepia = Image.fromarray(arrImg)
    return imgSepia
    imgSepia = Image.fromarray(arrImg)
    return imgSepia
def convertirImgSepiaV2(img):
    arrImg=convertirImgMatrixRGB(img)
    tonoSepia=10
    luminancia=[]
    for i in range(img.size[1]):
        luminancia.append([])
        for j in range(img.size[0]):
            aux = arrImg[i][j][0]*0.299+ arrImg[i][j][1]*0.587+ arrImg[i][j][2]*0.072
            luminancia[i].append(aux)
    for i in range(img.size[1]):
        for j in range(img.size[0]):
            arrImg[i][j][0] = luminancia[i][j] + (2*tonoSepia)
            arrImg[i][j][1] = luminancia[i][j] + (1*tonoSepia)
            arrImg[i][j][2] = luminancia[i][j] - (1*tonoSepia)
    imgSepia = Image.fromarray(arrImg)
    return imgSepia
def main():
    starting_point=time.time()
    img = Image.open('Lenna.png')
    imgSepia = convertirImgSepiaV2(img)
    imgSepia.save('LennaSepia.png')
    elapsed_time=time.time()-starting_point
    print ""
    print "Serial Time [seconds]: " + str(elapsed_time)

main()
