__author__ = 'Christopher Salvatierra L.'


import numpy as np
from PIL import Image
from PIL import ImageEnhance



# convierte una imagen tipo Imagen (de la libreria PIL) en una matriz(ETD) con la informacion RGB de la imagen
def convertirImgMatrixRGB(img):
    return np.array(img.convert("RGB"))


#Recibiendo una matriz, transformandola a imagen para trabajarla y devolviendo una matriz
def aplicarBrillo(imgMatriz):
    img = Image.fromarray(imgMatriz) #convierto el pedaz ode imagen en una imagen para trabajar con la libreria PIL
    print"ingrese factor para aplicar brillo (metodo 1)"#si el factor esta entre 0.0 y 1.0 la imagen se opacara, de ahi en mas aumentara el brillo
                                                        #y si el valor es menor que 0 la imagen queda completamente negra
    factor = input()
    imagen = ImageEnhance.Brightness(img)
    imConBrillo = imagen.enhance(factor)

    brilloMat = convertirImgMatrixRGB(imConBrillo) #devuelve una matriz con la informacion RGB de la imagen modificada
    return brilloMat

def main():
    img=Image.open("imagenMuestra.jpg")
    imgMatriz = convertirImgMatrixRGB(img) #transformamos la imagen a una matriz, en caso de paralelizar sera facil dividir la imagen en los nodos
    imgBrillo = aplicarBrillo(imgMatriz) #Devuelve una matriz de la imagen con brillo aplicado
    print imgBrillo #comprobamos que nos devuelve una matriz
    imagenMod = Image.fromarray(imgBrillo)
    imagenMod.save("resultado1.jpg")

main()
