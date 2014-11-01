__author__ = 'francisco'

import numpy as np
from StringIO import StringIO
import time
from mpi4py import MPI
from pylab import *
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

def cortarImagen(ruta, x, y):
    im = Image.open(ruta+'1.jpg')
    data= np.array(im.convert("RGB"))
    region = im.crop((0, 0,632 ,236 ))
    region.save("new1", "JPEG")
    region = im.crop((0, 236,632 ,474 ))
    region.save("new2", "JPEG")

ruta='/home/francisco/Documentos/Laboratorio-2-Paralela-2014/Produccion/Francisco Ramirez/Estrategia Paralelo/'
cortarImagen(ruta,0,236)


