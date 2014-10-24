"""
generadorGIF.py

Este programa corre un comando de la API ImageMagick

para instalar:
ejecutar en un terminal
  #sudo apt-get install imagemagick

"""
from os import system

nombreSalida="animacion.gif"
delay=10
filepath="imagenes/*png"
#el delay representa la pausa entre una imagen y otra y loop 0 especifica que el gif se repite en un bucle. *jpg tomara todos los archivos *jpg (para este caso, puede ser cualquier formato de imagen)
system('convert -delay %d -loop 0 %s %s ' % (delay,filepath,nombreSalida))
