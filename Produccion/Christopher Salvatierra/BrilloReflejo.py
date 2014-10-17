__author__ = 'Christopher Salvatierra L.'


import numpy as np
from PIL import Image
from PIL import ImageEnhance



# convierte una imagen tipo Imagen (de la libreria PIL) en una matriz(ETD) con la informacion RGB de la imagen
def convertirImgMatrixRGB(img):
    return np.array(img.convert("RGB"))

#aplicar brillo con libreria PIL
def aplicarBrillo(img,factor):
    imagen = ImageEnhance.Brightness(img)
    imConBrillo = imagen.enhance(factor) #si el factor esta entre 0.0 y 1.0 la imagen se opacara, de ahi en mas aumentara el brillo
                                         #y si el valor es menor que 0 la imagen queda completamente negra
    return imConBrillo

#aplicar reflejo con libreria PIL
def aplicarReflejo(img):
    xsize, ysize = img.size

    #se debe hacer una copia de la imagen
    imgCopia = img.copy()
    #se debe rotar la imagen
    imgCopia = imgCopia.rotate(180)
    #se pega bajo la imagen original
    img = img.rotate(90) #roto las imagenes
    imgCopia=imgCopia.rotate(90)
    arrImg=convertirImgMatrixRGB(img) #se transforman en matriz para poder ser sumadas
    arrImgCopia = convertirImgMatrixRGB(imgCopia)
    arrResul=arrImg + arrImgCopia #suma de ambas imagenes
    print arrResul
    imgReflejo=Image.fromarray(arrResul) #convierte la matriz en imagen
    imgReflejo = imgReflejo.rotate(270) #se rota para que quede vertical

    #se aplica transparencia a la imagen rotada
    return imgReflejo


def main():
    img=Image.open("imagenMuestra.jpg")
    print"ingrese factor"
    factor = input()
    imgBrillo = aplicarBrillo(img,factor)
    imgBrillo.save("resultado.jpg")

    imgReflejo = aplicarReflejo(img)
    imgReflejo.save("copia.png")


###Puede servir para unir las imagenes al final
'''
    #opens an image:
    im = Image.open("imagenMuestra.jpg")
    #creates a new empty image, RGB mode, and size 400 by 400.
    new_im = Image.new('RGB', (400,400))
    #Here I resize my opened image, so it is no bigger than 100,100
    im.thumbnail((100,100))
    #Iterate through a 4 by 4 grid with 100 spacing, to place my image
    for i in xrange(0,500,100):
        for j in xrange(0,500,100):
            #I change brightness of the images, just to emphasise they are unique copies.
            im=Image.eval(im,lambda x: x+(i+j)/30)
               #paste the image at location i,j:
            new_im.paste(im, (i,j))

    #new_im.save("union.png") '''

main()
