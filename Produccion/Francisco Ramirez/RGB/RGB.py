__author__ = 'Fco_Hernan'

import numpy as np
from PIL import Image
import time


# convierte una imagen tipo Imagen (de la libreria PIL) en una matriz(ETD) con la informacion RGB de la imagen
def convertirImgMatrixRGB(img):
    return np.array(img.convert("RGB"))


# procedimiento : Suma los componentes R, G, B del pixel de la imagen con el color que se quiere
# y cada suma se divide en dos, obteniendo un promedio
def mezclarRGB(img,r,g,b):
    arrImg=convertirImgMatrixRGB(img)
    for i in range(img.size[1]):
        for j in range(img.size[0]):
            arrImg[i][j][0] = (arrImg[i][j][0]+r)/2
            arrImg[i][j][1] = (arrImg[i][j][1]+g)/2
            arrImg[i][j][2] = (arrImg[i][j][2]+b)/2
    imgRGB=Image.fromarray(arrImg)
    return imgRGB

def main():
    starting_point=time.time()
    img=Image.open("8K.jpg")
    r=50
    g=160
    b=320
    imgRGB=mezclarRGB(img,r,g,b)
    imgRGB.save("output.png")    #guarda la imagen RGB
    elapsed_time=time.time()-starting_point
    print ""
    print "Serial Time [seconds]: " + str(elapsed_time)

main()