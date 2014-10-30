__author__ = 'jose'
import numpy as np
from PIL import Image
import time
def convertirImgMatrixRGB(img):
    return np.array(img.convert("RGB"))
def convertirImgNegativo(img):
    arrImg = convertirImgMatrixRGB(img)
    for i in range(img.size[1]):
        for j in range(img.size[0]):
            arrImg[i][j] = 255-arrImg[i][j]
    imgNegativo = Image.fromarray(arrImg)
    return imgNegativo
def main():
    starting_point=time.time()
    img = Image.open('Lenna.png')
    imgNegativo = convertirImgNegativo(img)
    imgNegativo.save('LennaNegativo.png')
    elapsed_time=time.time()-starting_point
    print ""
    print "Serial Time [seconds]: " + str(elapsed_time)
main()
