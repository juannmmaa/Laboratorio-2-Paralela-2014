# -*- coding: cp1252 -*-
__author__ = 'Luis Miguel leon'
import numpy as np
from PIL import Image
import time

def convertirImgMatrixRGB(img):
    return np.array(img.convert("RGB"))

def filtrohdr(imag,imag1,imag2,imag3,blanco):
    ancho=imag.size[0]
    alto=imag.size[1]
    print ancho
    print alto
    arrblanco=convertirImgMatrixRGB(blanco)
    arrImagE = [convertirImgMatrixRGB(imag),convertirImgMatrixRGB(imag1),convertirImgMatrixRGB(imag2),convertirImgMatrixRGB(imag3)]

    aa=arrImagE[2][0][11][0]
    bb=arrImagE[2][0][11][1]
    cc=arrImagE[2][0][11][2]
    
    print aa
    print bb
    print cc
    ee= int(aa)+int(bb)+int(cc)
    print ee
#   Proceso de redimensionado
    for i in range(alto):
        for j in range(ancho):
            Rc=0
            Gc=0
            Bc=0
            Ro=0
            Go=0
            Bo=0
            contadorC=0
            contadorO=0
            d=0;
            for k in range(4):
                a =arrImagE[k][i][j][0]
                b =arrImagE[k][i][j][1]
                c =arrImagE[k][i][j][2]
                
                d= (int(a)+int(b)+int(c))/float(3)
                if(d <127):
                    Ro=Ro+a
                    Go=Go+b
                    Bo=Bo+c
                    contadorO=contadorO+1
                else:
                    Rc=Rc+a
                    Gc=Gc+b
                    Bc=Bc+c
                    contadorC=contadorC+1 
            if(contadorO>contadorC):
                arrblanco[i][j][0]= Ro/contadorO
                arrblanco[i][j][1]= Go/contadorO
                arrblanco[i][j][2]= Bo/contadorO
            else:
                arrblanco[i][j][0]=Rc/contadorC
                arrblanco[i][j][1]=Gc/contadorC
                arrblanco[i][j][2]=Bc/contadorC
    imgRedimencionada=Image.fromarray(arrblanco)
    return imgRedimencionada

def main():
    starting_point=time.time()
    imag = Image.open("orig_0.jpg")
    imag1 = Image.open("orig_1.jpg")
    imag2 = Image.open("orig_2.jpg")
    imag3 = Image.open("orig_3.jpg")

    base = Image.open("base.jpg")
    base = base.resize((imag.size[0], imag.size[1]), Image.ANTIALIAS)#para crear una imagen en blanco con la cual obtengo el tamaño de la final de la imagen redimencionada.
    base.save("output1.jpg")
    blanco = Image.open("output1.jpg")
    
    imgfinal=filtrohdr(imag,imag1,imag2,imag3,blanco)
    imgfinal.save("salidaFinal.jpg")
    #saludo = raw_input("Escribe lo que sea")
    #print saludo
    elapsed_time=time.time()-starting_point
    print ""
    print "Serial Time [seconds]: " + str(elapsed_time)
main()







