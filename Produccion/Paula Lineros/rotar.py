
import ImageFilter
import numpy as np
import time
from numpy import array, shape, reshape, zeros, transpose
from PIL import Image, ImageChops, ImageOps

# convierte una imagen tipo Imagen (de la libreria PIL) en una matriz(ETD) con la informacion RGB de la imagen
def convertirImgMatrixRGB(img):
    return np.array(img.convert("RGB"))

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
    
def main(): #Comentar el que no se quiera utilizar
    starting_point=time.time() #Donde quiere empezar a calcular el tiempo
    imgTrans = rotar90(img)
    imgTrans.save("imagentranspuesta90.png") #guarda la imagen transpuesta 90 grados
    imgTrans = rotar180(img)
    imgTrans.save("imagentranspuesta180.png") #guarda la imagen transpuesta 180 grados
    imgTrans = rotar270(img)
    elapsed_time=time.time()-starting_point #calculo
    print ""
    print "Serial Time [seconds]: " + str(elapsed_time) #segundos
    
main()
