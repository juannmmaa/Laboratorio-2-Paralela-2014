__author__ = 'jose'
import numpy as np
from PIL import Image
def convertirImgMatrixRGB(img):
    return np.array(img.convert("RGB"))
def convertirImgColor(img):
    arrImg=convertirImgMatrixRGB(img)
    imgAux=arrImg
    for i in range(img.size[1]):
        for j in range(img.size[0]):
            arrImg[i][j][1] = imgAux[i][j][2]
            arrImg[i][j][2] = imgAux[i][j][0]
    imgColor = Image.fromarray(arrImg)
    return  imgColor
def main():
    img = Image.open('Lenna.png')
    imgColor = convertirImgColor(img)
    imgColor.save('LennaColor.png')

main()