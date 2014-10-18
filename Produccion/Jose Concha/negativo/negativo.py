__author__ = 'jose'
import numpy as np
from PIL import Image
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
    img = Image.open('Lenna.png')
    imgNegativo = convertirImgNegativo(img)
    imgNegativo.save('LennaNegativo.png')
main()