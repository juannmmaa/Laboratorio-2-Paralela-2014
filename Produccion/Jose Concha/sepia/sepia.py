__author__ = 'jose'
<<<<<<< HEAD
from PIL import Image, ImageOps
import time
inicio = time.time()
def make_linear_ramp(white):
     ramp = []
     r, g, b = white
     for i in range(255):
         ramp.extend((r*i/255, g*i/255, b*i/255))
     return ramp
def sepia(im):
    sepia = make_linear_ramp((255, 240, 192))
    if im.mode != "L":
        im = im.convert("L")
    # optional: apply contrast enhancement here, e.g.
    im = ImageOps.autocontrast(im)
    # apply sepia palette
    im.putpalette(sepia)
    return im
def main():
	im = Image.open("lenac.jpg")
	im = sepia(im)
	im.save("sepias.png")
=======
import numpy as np
from PIL import Image
import colorsys
import time

def convertirImgMatrixRGB(img):
    return np.array(img.convert("RGB"))
def convertirImgSepia(img):
    arrImg = convertirImgMatrixRGB(img)
    for i in range(img.size[1]):
        for j in range(img.size[0]):
            arrImg[i][j][0] = arrImg[i][j][0]*0.393 + arrImg[i][j][1]*0.769 + arrImg[i][j][2]*0.189
            arrImg[i][j][1] = arrImg[i][j][0]*0.349 + arrImg[i][j][1]*0.686 + arrImg[i][j][2]*0.168
            arrImg[i][j][2] = arrImg[i][j][0]*0.272 + arrImg[i][j][1]*0.534 + arrImg[i][j][2]*0.131
    imgSepia = Image.fromarray(arrImg)
    return imgSepia
    imgSepia = Image.fromarray(arrImg)
    return imgSepia
def convertirImgSepiaV2(img):
    arrImg=convertirImgMatrixRGB(img)
    tonoSepia=10
    luminancia=[]
    for i in range(img.size[1]):
        luminancia.append([])
        for j in range(img.size[0]):
            aux = arrImg[i][j][0]*0.299+ arrImg[i][j][1]*0.587+ arrImg[i][j][2]*0.072
            luminancia[i].append(aux)
    for i in range(img.size[1]):
        for j in range(img.size[0]):
            arrImg[i][j][0] = luminancia[i][j] + (2*tonoSepia)
            arrImg[i][j][1] = luminancia[i][j] + (1*tonoSepia)
            arrImg[i][j][2] = luminancia[i][j] - (1*tonoSepia)
    imgSepia = Image.fromarray(arrImg)
    return imgSepia
def main():
    starting_point=time.time()
    img = Image.open('Lenna.png')
    imgSepia = convertirImgSepiaV2(img)
    imgSepia.save('LennaSepia.png')
    elapsed_time=time.time()-starting_point
    print ""
    print "Serial Time [seconds]: " + str(elapsed_time)

>>>>>>> 677fcd9c777715c5571abefaac2092ed192ff7a1
main()
final = time.time() -inicio

print "serial time [seconds] = " +str(final)
