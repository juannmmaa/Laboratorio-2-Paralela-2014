__author__ = 'juank'

import numpy as np
from PIL import Image
from PIL import ImageEnhance

# convierte una imagen tipo Imagen (de la libreria PIL) en una matriz(ETD) con la informacion RGB de la imagen
def convertirImgMatrixRGB(img):
    return np.array(img.convert("RGB"))
# convierte una imagen tipo Imagen (de la libreria PIL) a imagen en Negativo
# procedimiento : multiplica por base 255 cada casilla de la matriz RGB para convertir la imagen en negativo

def myEqualize(img): #funcion para cambiar brillo y contraste
    img=img.convert('L')
    contr = ImageEnhance.Contrast(img)
    img = contr.enhance(0.5)
    bright = ImageEnhance.Brightness(img)
    img = bright.enhance(0.2)
    img.show()
    return img
def PasarDiaNoche(img):
    arrImg = convertirImgMatrixRGB(img)
    for i in range(img.size[1]):
        for j in range(img.size[0]):
            arrImg[i][j][0] = arrImg[i][j][0] * 0.1 #rojo
            arrImg[i][j][1] = arrImg[i][j][1] * 0.4 #verde
            arrImg[i][j][2] = arrImg[i][j][2] *1.6 #azul
    imgNoche = Image.fromarray(arrImg)
    return imgNoche
def main():
    img=Image.open("paisaje2.jpg")
    arrImg = convertirImgMatrixRGB(img)
    imgNoche=PasarDiaNoche(img)
    imgNoche.save("paisajeNoche.jpg")


main()