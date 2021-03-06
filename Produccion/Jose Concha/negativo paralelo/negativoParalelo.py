__author__ = 'jose'
from PIL import Image
import time
from mpi4py import MPI
import numpy as np
inicio = time.time()
comm = MPI.COMM_WORLD
rank = comm.rank
size = comm.size
img = Image.open("4M.jpg")
def negativo(im):
    x,y = im.size
    pix = im.load()
    imagen = Image.new("RGB",(x,y))
    for i in range(x):
        for j in range(y):
            imagen.putpixel((i,j),(255-pix[i,j][0],255-pix[i,j][1],255-pix[i,j][2]))
    return imagen

#---------------------------------------------
if rank ==0:
    ancho,alto = img.size
    for i in range(2,size):
        if i <size-1:
            imgFraccion = img.crop((0,(i-2)*alto/(size-2),ancho,((i-1)*alto/(size-2))-1))
            comm.send(np.array(imgFraccion.convert("RGB")),dest=i)
        else:
            imgFraccion = img.crop((0,(i-2)*alto/(size-2),ancho,(alto-1)))
            comm.send(np.array(imgFraccion.convert("RGB")),dest=i)
if rank >=2:
    imgWork = Image.fromarray(comm.recv(source=0))
    imgWork = negativo(imgWork)
    comm.send(np.array(imgWork.convert("RGB")),dest=0)
if rank==0:
    if size<3:
        imagen = Image.fromarray(comm.recv(source=2))
    else:
        img1 = comm.recv(source=2)
        for i in range(3,size):
            img2 = comm.recv(source=i)
            img1 = np.vstack((img1,img2))
        imagen = Image.fromarray(img1)
    imagen.save("negativoParalelo.png")
    final = time.time()-inicio
    print "Parallel time [seconds] = " + str(final)
