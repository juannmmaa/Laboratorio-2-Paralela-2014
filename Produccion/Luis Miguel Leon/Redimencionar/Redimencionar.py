# -*- coding: cp1252 -*-
__author__ = 'Luis Miguel leon'
import numpy as np
from PIL import Image

def convertirImgMatrixRGB(img):
    return np.array(img.convert("RGB"))

def redimencionarImg(img,img2):
    alto=img.size[1]
    ancho=img.size[0]
    finalAncho=img2.size[1]
    finAlto= img2.size[0]
    distanX = (ancho-1)/float(finalAncho)
    distanY = (alto-1) /float(finAlto)
    arrImg=convertirImgMatrixRGB(img)
    arrImg2=convertirImgMatrixRGB(img2)
    
#   Proceso de redimensionado
    for i in range(finalAncho):
        for j in range(finAlto):
            #Variables x y dependiendo de resolucion de salida.
            x = (distanX * j);
            y = (distanY * i);

            #Direfencia entre distancia y el pixel que esta.
            diferX = (distanX * j) - x;
            diferY = (distanY * i) - y;

            #Tomo pixeles adyacentes, dependiendo de la resolucion que debo entregar.
            a = arrImg[x][y] 
            b = arrImg[x][y+1]
            c = arrImg[x+1][y]
            d = arrImg[x+1][y+1]

            # color azul
            blue =  ((a[2])&0xff)*(1-diferX)*(1-diferY) + ((b[2])&0xff)*(diferX)*(1-diferY) + ((c[2])&0xff)*(diferY)*(1-diferX) + ((d[2])&0xff)*(diferX*diferY)

            # color verde
            green = ((a[1])&0xff)*(1-diferX)*(1-diferY) + ((b[1])&0xff)*(diferX)*(1-diferY) + ((c[1])&0xff)*(diferY)*(1-diferX) + ((d[1])&0xff)*(diferX*diferY)

            # color rojo
            red =   ((a[0])&0xff)*(1-diferX)*(1-diferY) + ((b[0])&0xff)*(diferX)*(1-diferY) + ((c[0])&0xff)*(diferY)*(1-diferX) + ((d[0])&0xff)*(diferX*diferY)

            nuevoPixel = arrImg2[i][j]
            nuevoPixel[0]=red 
            nuevoPixel[1]=green 
            nuevoPixel[2]=blue 

            arrImg2[i][j] = nuevoPixel;
    
    imgRedimencionada=Image.fromarray(arrImg2)
    return imgRedimencionada

def main():
    
    imag = Image.open("base.png")
    #Tamaño de imagen tiene que estar en la misma escala que la original.
    imag = imag.resize((100, 100), Image.ANTIALIAS)#para crear una imagen en blanco con la cual obtengo el tamaño de la final de la imagen redimencionada.
    imag.save("output1.jpg")

    
    img=Image.open("prueba.jpg")
    img2=Image.open("output1.jpg")
    
    imgRedimencionada=redimencionarImg(img,img2)
    imgRedimencionada.save("salidaFinal.jpg")
    #saludo = raw_input("Escribe lo que sea")
    #print saludo
main()









