
from PIL import Image
import numpy as np
#---valor porcentual con el que se oscurece la imagen------
#--- 0 para que sea completamente negro  y 1 para que------
#----la imagen quede igual---------------------------------
oscurecimiento = 0.6


#---------------------------------------------------------------------------------------
#-----------------se oscure la imagen pixel por pixel, sus entradas son-----------------
#-----------------la imagen y el %de oscurecimiento-------------------------------------
#---------------------------------------------------------------------------------------
def oscurecer(imagen):
    matrix = np.array(imagen.convert('RGB'))
    for i in range(imagen.size[1]):
        for j in range(imagen.size[0]):
            oscuro = matrix[i][j]*oscurecimiento
            matrix[i][j] = oscuro
    imagenFade = Image.fromarray(matrix)
    return imagenFade


#---------------------------------------------------------------------------------------
#-----------------definir main, cargar imagenes y funciones-----------------------------
#---------------------------------------------------------------------------------------
def main():
    #---carga imagen---
    imagen = Image.open('imagenCache.jpg')
    #----llama a la funcion---
    resultadoOscuro = oscurecer(imagen)
    #-----guarda la imagen obtenida----
    resultadoOscuro.save('resultadoCache.jpg')
#---------------------------------------------------------------------------------------

main()