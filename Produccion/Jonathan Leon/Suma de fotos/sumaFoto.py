__author__ = 'jonathan leon'

"""
sumaFoto.py

Entrada : 2 urls con imagenes, un valor float entre 0 y 1 y un valor entero entre
           0 y 2 para el formato de salida. 0=>BMP , 1=>PNG , 2=>JPG 

Salida  : Una imagen llamada suma.bmp|png|jpg

"""

import numpy as np
import os.path
from PIL import Image

def sumaFoto(url1,url2,alfa,formato):   
    if os.path.exists(url1)==False: #comprobamos existencia de archivo
        return "No se encontro el archivo %s" %(url1)
     if os.path.exists(url2)==False:  #comprobamos existencia de archivo
        return "No se encontro el archivo %s" %(url2)    
    if alfa>1 or <0:                  #comprobamos valor del alfa  
        return "Valor alfa invalido, debe ser entre 0 y 1."
    
    img1=Image.open(url1)
    img2=Image.open(url2)
    resultado=Image.blend(img1,img2,alfa)  #sumamos las imagenes  
    return resultado.save("suma."+formato) #returnamos imagen   


