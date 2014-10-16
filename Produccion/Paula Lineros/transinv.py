
import ImageFilter
import numpy as np
from numpy import array, shape, reshape, zeros, transpose
from PIL import Image, ImageChops


# convierte una imagen tipo Imagen (de la libreria PIL) en una matriz(ETD) con la informacion RGB de la imagen
def convertirImgMatrixRGB(img):
    return np.array(img.convert("RGB"))

# convierte una imagen tipo Imagen (de la libreria PIL) a imagen en Negativo
# procedimiento : multiplica por base 255 cada casilla de la matriz RGB para convertir la imagen en negativo

def convertirImgNegativo(img):
    arrImg=convertirImgMatrixRGB(img)
    for i in range(img.size[1]):
        for j in range(img.size[0]):
            arrImg[i][j]=arrImg[i][j]*255
    imgNegativa=Image.fromarray(arrImg)
    return imgNegativa

def invertirImgColores(img): # al parecer es la misma que el negativo
    arrImg=convertirImgMatrixRGB(img)
    # for i in range(img.size[1]):
    #     for j in range(img.size[0]):
    #         arrImg[i][j]=(arrImg[i][j])-255
    imgColor=Image.fromarray(arrImg)
    img = ImageChops.invert(imgColor)
    return img

def transpuesta(img, g):
    arrImg=convertirImgMatrixRGB(img)
    imgColor=Image.fromarray(arrImg)
    imagen = imgColor.rotate(g)
    return imagen

def blur(img):
    arrImg=convertirImgMatrixRGB(img)
    imgColor=Image.fromarray(arrImg)
    blurred = imgColor.filter(ImageFilter.BLUR)
    return blurred

def sharpen(img):
    arrImg=convertirImgMatrixRGB(img)
    imgColor=Image.fromarray(arrImg)
    sharpened = imgColor.filter(ImageFilter.SHARPEN)
    return sharpened

def edged(img):
    arrImg=convertirImgMatrixRGB(img)
    imgColor=Image.fromarray(arrImg)
    edged = imgColor.filter(ImageFilter.EDGE_ENHANCE)
    return edged
    
def main():
    img=Image.open("imagennormal.png") #abre imagen
    imgColor=invertirImgColores(img)
    imgColor.save("imageninvertida.png") #guarda la imagen con colores invertidos
    imgBlur=blur(img)
    imgBlur.save("imagenblur.png") #guarda la imagen borrosa
    imgEdged=edged(img)
    imgEdged.save("imagenedged.png") #guarda la imagen "antigua"
    imgSharpen=sharpen(img)
    imgSharpen.save("imagensharpen.png") #guarda la imagen que destaca bordes
    imgTrans = transpuesta(img,90)
    imgTrans.save("imagentranspuesta90.png") #guarda la imagen transpuesta 90 grados
    imgTrans = transpuesta(img,180)
    imgTrans.save("imagentranspuesta180.png") #guarda la imagen transpuesta 180 grados
    imgTrans = transpuesta(img,270)
    imgTrans.save("imagentranspuesta270.png") #guarda la imagen transpuesta 270 grados
    imgNegativa=convertirImgNegativo(img)
    imgNegativa.save("negativo.png") #guarda la imagen negativo


main()