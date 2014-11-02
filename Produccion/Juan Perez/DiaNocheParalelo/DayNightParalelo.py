__author__ = 'juank'

import numpy as np
from PIL import Image
from PIL import ImageEnhance
import time

# convierte una imagen tipo Imagen (de la libreria PIL) en una matriz(ETD) con la informacion RGB de la imagen
def convertirImgMatrixRGB(img):
    return np.array(img.convert("RGB"))
# convierte una imagen tipo Imagen (de la libreria PIL) a imagen en Negativo
# procedimiento : multiplica por base 255 cada casilla de la matriz RGB para convertir la imagen en negativo

def PasarDiaNoche(img):
    img = escalaGrises(img) #desaturar la imagen
    img = aplicarBrillo(img,-0.4)
    arrImg = convertirImgMatrixRGB(img)

    for i in range(img.size[1]):
        for j in range(img.size[0]):
            arrImg[i][j][0] = arrImg[i][j][0] * 0.2 #rojo
            arrImg[i][j][1] = arrImg[i][j][0] * 1.2 #verde
            arrImg[i][j][2] = arrImg[i][j][0] * 3.5 #azul
    imgNoche = Image.fromarray(arrImg)
    #contraste = ImageEnhance.Contrast(imgNoche)
    #imgNoche = contraste.enhance(1.2) #asigna un valor para el contraste de la imagen
    #brillo = ImageEnhance.Brightness(imgNoche)
    #imgNoche = brillo.enhance(0.7) #asigna un valor para el brillo de la imagen
    #nitidez = ImageEnhance.Sharpness(imgNoche)
    #imgNoche = nitidez.enhance(2) #asigna un valor para la nitidez de la imagen
    return imgNoche

def aplicarBrillo(img,factor):
    arrImg=convertirImgMatrixRGB(img)
    #si el factor es menor a cero la imagen se oscurece (rango 0 a -1)
    if factor <0:#para oscurecer la imagen
        for i in range(img.size[1]):
            for j in range(img.size[0]):
                brillo= lambda x: x*(1+factor)
                arrImg[i][j]=brillo(arrImg[i][j])
    #si el factor es mayor a cero se aclara (rango 0 a 1)
    else:#brillo
        for i in range(img.size[1]):
            for j in range(img.size[0]):
                brillo= lambda x: x+ (255-x)*factor
                arrImg[i][j]=brillo(arrImg[i][j])
    imgBrillante=Image.fromarray(arrImg)#se devuelve la matriz a imagen
    return imgBrillante

def escalaGrises(img):
    n = img.size[0]
    m = img.size[1]
    for i in range(n):
        for j in range(m):
            # Obtenemos los colores RGB pixel por pixel
            r, g, b = img.getpixel((i, j))
            # Cambiamos el RGB del pixel
            img.putpixel((i, j), ((r+g+b)/3, (r+g+b)/3, (r+g+b)/3))
    return img
def main():
    starting_point=time.time()
    """las siguientes dos lineas corresponden al nombre del archivo y la extension con el fin de
    nombrar el archivo de salida como <nombreArchivo>Noche.<extension>
    ejemplo: paisaje.jpg -> paisajeNoche.jpg"""
    nombreImg = "paisaje"
    extension = ".jpg"
    img=Image.open(nombreImg + extension)
    arrImg = convertirImgMatrixRGB(img)
    imgNoche=PasarDiaNoche(img)
    imgNoche.save(nombreImg+"Noche2"+extension)
    elapsed_time=time.time()-starting_point
    print ""
    print "Serial Time [seconds]: " + str(elapsed_time)
    imgNoche.show()


main()