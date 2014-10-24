__author__ = 'jose'
import numpy as np
from PIL import Image
def convertirImgMatrixRGB(img):
    return np.array(img.convert("RGB"))
def convolucionImg(img):    #media movil
    arrAux = convertirImgMatrixRGB(img)
    arrImg = arrAux
    for i in range(img.size[1]):
        for j in range(img.size[0]):
            if (i>0 and i<img.size[1]-1) and (j>0 and j<img.size[0]-1):
                media = arrImg[i-1][j]+arrImg[i-1][j-1]+arrImg[i][j-1]+arrImg[i+1][j-1]+arrImg[i+1][j]+arrImg[i+1][j+1]+arrImg[i][j+1]+arrImg[i-1][j+1]
                arrAux[i][j]=media/8
    convImg = Image.fromarray(arrAux)
    return convImg
def main():
    img = Image.open('Lenna.png')
    convImg = convolucionImg(img)
    convImg.save('convLenna.png')
main()