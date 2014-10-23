
import ImageFilter
import numpy as np
from numpy import array, shape, reshape, zeros, transpose
from PIL import Image, ImageChops, ImageOps


# convierte una imagen tipo Imagen (de la libreria PIL) en una matriz(ETD) con la informacion RGB de la imagen
def convertirImgMatrixRGB(img):
    return np.array(img.convert("RGB"))

# convierte una imagen tipo Imagen (de la libreria PIL) a imagen en Negativo
# procedimiento : multiplica por base 255 cada casilla de la matriz RGB para convertir la imagen en negativo


def invertirImgColores(img): # al parecer es la misma que el negativo
    arrImg=convertirImgMatrixRGB(img)
    for i in range(img.size[1]):
        for j in range(img.size[0]):
            arrImg[i][j]=(arrImg[i][j])*255
    imgColor=Image.fromarray(arrImg)
    return imgColor

def rotar90(img):
    arrImg = convertirImgMatrixRGB(img)
    n = img.size[0]
    m = img.size[1]
    final = np.array(Image.new("RGB",(m,n)))
    for i in range(n): #fila
        for j in range(m): #columna
            final[i][j] = arrImg[::, ((i*-1)-1)][j]
    imgColor = Image.fromarray(final)
    return imgColor

def rotar180(img):
    return rotar90(rotar90(img)) #debido a que el algoritmo de cambio de posicion es el mismo

def rotar270(img):
    return rotar180(rotar90(img))
    
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
    img=Image.open("imagennormal.png") #abre imagen
    imgColor=invertirImgColores(img)
    imgColor.save("imageninvertida.png") #guarda la imagen con colores invertidos
    imgTrans = rotar90(img)
    imgTrans.save("imagentranspuesta90.png") #guarda la imagen transpuesta 90 grados
    imgTrans = rotar180(img)
    imgTrans.save("imagentranspuesta180.png") #guarda la imagen transpuesta 180 grados
    imgTrans = rotar270(img)
    imgTrans.save("imagentranspuesta270.png") #guarda la imagen transpuesta 270 grados
    imgGris = escalaGrises(img)
    imgGris.save("imagenescaladegris.png") #guarda la imagen en escala de grises

main()
