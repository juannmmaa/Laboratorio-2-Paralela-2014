# -*- coding: cp1252 -*-
__author__ = 'Luis Miguel leon'
import numpy as np
from PIL import Image

def convertirImgMatrixRGB(img):
    return np.array(img.convert("RGB"))

def filtrohdr(imag,imag1,imag2,imag3,blanco):
    alto=imag.size[1]
    ancho=imag.size[0]
    arrblanco=convertirImgMatrixRGB(blanco)
    arrImagE = [convertirImgMatrixRGB(imag),convertirImgMatrixRGB(imag1),convertirImgMatrixRGB(imag2),convertirImgMatrixRGB(imag3)]

    aa=arrImagE[2][0][11][0]
    bb=arrImagE[2][0][11][1]
    cc=arrImagE[2][0][11][2]
    
    print aa
    print bb
    print cc
    ee= aa+bb+cc
    print ee
#   Proceso de redimensionado
    for i in range(ancho):
        for j in range(alto):
            claro=arrImagE[0][i][j]
            claro[0]=0
            claro[1]=0
            claro[2]=0
            oscuro = claro
            contadorC=0
            contadorO=0
            d=0;
            for k in range(4):
                a =arrImagE[k][i][j][0]
                b =arrImagE[k][i][j][1]
                c =arrImagE[k][i][j][2]
                
                d= (a+b+c)/float(3)
                if(d <127):
                    oscuro=oscuro+arrImagE[k][i][j]
                    contadorO=contadorO+1
                else:
                    claro=claro+arrImagE[k][i][j]
                    contadorC=contadorC+1
                
            if(contadorO>contadorC):
                arrblanco[i][j]=oscuro/contadorO
            else:
                arrblanco[i][j]=claro/contadorC
       
    imgRedimencionada=Image.fromarray(arrblanco)
    return imgRedimencionada

def main():
   
    imag = Image.open("orig_0.jpg")
    imag1 = Image.open("orig_1.jpg")
    imag2 = Image.open("orig_2.jpg")
    imag3 = Image.open("orig_2.jpg")

    base = Image.open("base.jpg")
    base = base.resize((imag.size[0], imag.size[1]), Image.ANTIALIAS)#para crear una imagen en blanco con la cual obtengo el tamaÃ±o de la final de la imagen redimencionada.
    base.save("output1.jpg")
    blanco = Image.open("output1.jpg")
    
    imgfinal=filtrohdr(imag,imag1,imag2,imag3,blanco)
    imgfinal.save("salidaFinal.jpg")
    #saludo = raw_input("Escribe lo que sea")
    #print saludo
main()







