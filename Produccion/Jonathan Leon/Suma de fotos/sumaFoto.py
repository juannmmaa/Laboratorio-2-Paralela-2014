__author__ = 'jonathan leon'

"""
sumaFoto.py

Entrada : 2 urls con imagenes, un valor float entre 0 y 1 

Salida  : Una imagen mezclada a partir de las originales

"""

import numpy as np
import os.path
from PIL import Image

def sumaFoto(url1,url2,alfa):   
    if os.path.exists(url1)==False: #comprobamos existencia de archivo
        return "No se encontro el archivo %s" %(url1)
     if os.path.exists(url2)==False:  #comprobamos existencia de archivo
        return "No se encontro el archivo %s" %(url2)    
    if alfa>1 or <0:                  #comprobamos valor del alfa  
        return "Valor alfa invalido, debe ser entre 0 y 1."
    
    img1=Image.open(url1)
    img2=Image.open(url2)
    
    return resultado=Image.blend(img1,img2,alfa)  #sumamos las imagenes  
       


