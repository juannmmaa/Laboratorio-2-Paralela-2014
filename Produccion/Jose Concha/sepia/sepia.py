__author__ = 'jose'
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
	im = Image.open("4M.jpg")
	im = sepia(im)
	im.save("4M0.png")
main()
final = time.time() -inicio

print "serial time [seconds] = " +str(final)
