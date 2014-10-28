"""
generadorGIF.py

Este programa corre un comando de la API ImageMagick

para instalar:
ejecutar en un terminal
  #sudo apt-get install imagemagick

"""
from os import system
import time

def toGif(fp,delay,output):
  #el delay representa la pausa entre una imagen y otra y loop 0 especifica que el gif se repite en un bucle. *jpg tomara todos los archivos *jpg (para este caso, puede ser cualquier formato de imagen)
  system('convert -delay %d -loop 0 %s %s ' % (delay,fp,output))

def main():
  starting_point=time.time()
  nombreSalida="animacion.gif"
  delay=10
  filepath="imagenes/*png"
  toGif(filepath,delay,nombreSalida)
  elapsed_time=time.time()-starting_point
  print ""
  print "Serial Time [seconds]: " + str(elapsed_time)


