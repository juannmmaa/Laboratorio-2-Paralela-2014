from mpi4py import MPI
import colorsys
import numpy as np
from PIL import Image, ImageEnhance
import time

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.rank


# propiedades de NP para cambiar de modo RGB a HSV y viceversa
rgb_to_hsv = np.vectorize(colorsys.rgb_to_hsv)
hsv_to_rgb = np.vectorize(colorsys.hsv_to_rgb)

# convertimos imagen a RGB para cambiar tonalidades rojas, azules y verdes.
def convertirImgMatrixRGB(img):
	return np.array(img.convert("RGB"))



def distribuirEnP(size,altura):
	if (rank == 0):
		cuoc = (altura) / (size-2) #c : cuociente
		rest = (altura) % (size-2) #r : resto
		conta = 0
	for p in range(size-2):
		if (p+1) != (size-2):
			conta = conta + cuoc
			comm.send(conta, dest = p+2)
		else:
			conta = conta+cuoc+rest
			comm.send(conta, dest = p+2)



def buscarRangoFinal(base,altura):
	if rank==2:
		p=2
		conta=0
		rangos_end=[]
		valor=0
		for i in range(altura):
			for j in range(base):
				if(valor==0):
					valor=comm.recv(source=p)
				if conta==valor:
					rangos_end = rangos_end + [i,j]
					comm.send(rangos_end,dest=p)
					rangos_end=[]
					p = p + 1
					conta = conta + 1
					valor=0
				else:
					conta = conta + 1


def cortarImagen(x, y,base):
	im = Image.open('m.jpg')
	region = im.crop((0, x, base, y))
	region.save("cut"+str(rank)+".jpg")
	tonos(region)
	retoquecolor(region)
	blanquear(region)



def unirImagen():
	im1 = Image.open('new'+str(rank)+'.jpg')
	im1 = np.array(im1.convert("RGB"))
	for i in range(3, size):
		im2 = Image.open('new'+str(i)+'.jpg')
		im2 = np.array(im2.convert("RGB"))
		im1=np.vstack((im1, im2))
	im1=Image.fromarray(im1)
	im1.save("end.png")

# Resaltamos ciertos tonos como el rojo por sobre los demas para dar un efecto adicional.
def retoquecolor(img):
	for i in range(img.size[0]):
		for j in range(img.size[1]):
			r, g, b = img.getpixel((i, j))
			img.putpixel((i, j), ((r+220)/3, (r+g+170)/3, (r+g+b+70)/3))
	img.save("new"+str(rank)+".jpg")


# funcion que blanquea las tonalidades verdes.
def blanquear(img):
	arrImg = convertirImgMatrixRGB(img)
	for i in range(img.size[1]):
		for j in range(img.size[0]):
			if(arrImg[i][j][1]>200 and arrImg[i][j][0]<80 and arrImg[i][j][2]<80):
				arrImg[i][j][0] =255
				arrImg[i][j][1] =255
				arrImg[i][j][2] =255
	imgblanqueada = Image.fromarray(arrImg)
	imgblanqueada.save("new"+str(rank)+".jpg")


# asigna mayor brillo y contraste a la imagen
def tonos(img):
	arrImg=convertirImgMatrixRGB(img)
	factor=0.1
	for i in range(img.size[1]):
			for j in range(img.size[0]):
				brillo= lambda x: x+ (255-x)*factor
				arrImg[i][j]=brillo(arrImg[i][j])
	imgBrillante=Image.fromarray(arrImg)
	imgtono= ImageEnhance.Contrast(imgBrillante).enhance(3)
	imgtono.save("new"+str(rank)+".jpg")


# resaltamos matiz de la imagen 
def color(imagen, matiz):
	img = imagen.convert('RGBA')
	arr = np.array(np.asarray(img).astype('float'))
	imgresaltada = Image.fromarray(cambiar_matiz(arr, matiz/360.).astype('uint8'), 'RGBA')

	return imgresaltada

# aplicamos grado de matiz al modo HSV
def cambiar_matiz(arr, grado_matiz):
    r, g, b, a = np.rollaxis(arr, axis=-1)
    h, s, v = rgb_to_hsv(r, g, b)
    h = grado_matiz
    r, g, b = hsv_to_rgb(h, s, v)
    arr = np.dstack((r, g, b, a))
    return arr

def main():
    #Asignamos un grado de matiz para resaltar colores
    matiz=180
    img = Image.open('2.jpg')
    starting_point=time.time()
    img=color(img,matiz)
    img.save("m.jpg")
    data=convertirImgMatrixRGB(img)
    altura = data.shape[0]
    base = data.shape[1]
	
    if rank == 0:
    	print ""
    	print "altura,base: ",altura,base
    	distribuirEnP(size,altura)

    
    if rank >= 2:

    	fin = comm.recv(source=0)

	if size != 3:
		if rank == 2:
			ini = 0
			i = 1
			if size > 0:
				comm.send(fin, dest=3)

	else:
		ini=0
		comm.send(fin,dest=2)


	if size != 3:
		if rank !=2:
			ini=comm.recv(source=rank-1)
			if (rank+1)<size:
				comm.send(fin,dest=rank+1)
	else:
		ini=comm.recv(source=2)
	print "rank ",rank,", ini,fin :",ini,",",fin

	cortarImagen(ini,fin,base)

    if rank==2:
	exito=0
	while exito==0:
		try:
			unirImagen()
			exito=1
		except:
			print "imagenes aun no listas, reintentando..."
     


    if rank ==2:
	# Calculo de tiempo
	elapsed_time=time.time()-starting_point
	elapsed_time_int = int(elapsed_time)
	print "Parallel Time [seconds]: " + str(elapsed_time)
	print ""


main()
