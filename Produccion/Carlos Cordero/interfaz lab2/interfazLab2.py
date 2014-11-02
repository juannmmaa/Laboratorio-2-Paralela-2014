# -*- coding: utf-8 -*-

from PyQt4 import QtGui, QtCore
import sys
#-----------------------------------------------------------------------------------------------------------------------
#Clase interfax que llamara a los componentes de la ventana o widget
#-----------------------------------------------------------------------------------------------------------------------
class Interfaz(QtGui.QMainWindow):
    def __init__(self):
        super(Interfaz,self).__init__()

        self.iniciar()

    def iniciar(self):
        #-------------------------------------
        # datos iniciales de la ventana
        #-------------------------------------
        self.setGeometry(0,0,1000,700)
        self.setWindowTitle('PhotoShake - Computacion Paralela')
        self.setWindowIcon(QtGui.QIcon('iconos/Icono.png'))
        #-------------------------------------
        #variables widget
        #-------------------------------------
        self.labelIzquierda = QtGui.QLabel(self)
        self.labelDerecha = QtGui.QLabel(self)
        self.menubar = self.menuBar()
        self.hL = QtGui.QHBoxLayout()
        self.setLayout(self.hL)
        #-------------------------------------
        #funciones de ventana
        #-------------------------------------
        self.archivoMenu()
        self.serialMenu()
        self.paraleloMenu()
        #-------------------------------------
        # StatusBar
        #-------------------------------------
        linedit = QtGui.QLineEdit()
        self.statusBar = QtGui.QStatusBar()
        self.statusBar.addWidget(linedit)
        self.setStatusBar(self.statusBar)

#-----------------------------------------------------------------------------------------------------------------------
# declaracion del menubar con sus conponentes conectados
#-----------------------------------------------------------------------------------------------------------------------
    def serialMenu(self):

        gifAction = QtGui.QAction('Gif',self)
        gifAction.setStatusTip(u'Compilar gif de forma serial')
        gifAction.triggered.connect(self.gifSerial)

        menuserial = self.menubar.addMenu('Serial')
        menuserial.addAction(gifAction)

    def archivoMenu(self):
        #---------------------------------------
        # definir acciones
        #---------------------------------------
        exitAction = QtGui.QAction( 'Salir', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip(u'Salir de la Aplicación')
        exitAction.triggered.connect(self.close)
        #----------------------------------------
        # definir elementos en menubar
        #----------------------------------------
        fileMenu = self.menubar.addMenu('&Archivo')
        fileMenu.addAction(exitAction)

    def paraleloMenu(self):

        gifAction = QtGui.QAction('Gif',self)
        gifAction.triggered.connect(self.gifParalelo)

        menuParalelo = self.menubar.addMenu('Paralelo')
        menuParalelo.addAction(gifAction)
#-----------------------------------------------------------------------------------------------------------------------
# acciones que llamaran los codigos que trabajaran las imagenes
#-----------------------------------------------------------------------------------------------------------------------

    def gifSerial(self):

        self.fname = QtGui.QFileDialog.getOpenFileName(self, 'Open file','/home',"Image Files (*.png *.jpg *.bmp)")
        if self.fname != '':
            self.statusBar.showMessage('Espere un momento...')
            print('Gif Serial')
            self.cargarImagenes()
            self.statusBar.showMessage('')
            #self.fnameTrabajado = 'ruta'

    def gifParalelo(self):
        self.fname = QtGui.QFileDialog.getOpenFileName(self, 'Open file','/home',"Image Files (*.png *.jpg *.bmp)")
        print(self.fname)
        #self.fnameTrabajado = 'RutaParalela'
#-----------------------------------------------------------------------------------------------------------------------
# se  cargan las imagenes obtenidas
#-----------------------------------------------------------------------------------------------------------------------
    def cargarImagenes(self):

        pixmap = QtGui.QPixmap(self.fname)
        maximo = self.geometry()
        pixmap = pixmap.scaled( (maximo.width()/2)-10, (maximo.height())-10)
        #pixmap2 = QtGui.QPixmap(self.fnameTrabajado)
        self.labelIzquierda.setPixmap(pixmap)
        self.labelIzquierda.setGeometry(5,5,(maximo.width()/2)-10, (maximo.height()/2)-10)
        #self.labelDerecha.setPixmap(pixmap2)
        self.labelIzquierda.adjustSize()
        #--------------------------------------------
        #ingresando imagenes a la ventana
        #--------------------------------------------
        self.hL.addWidget(self.labelIzquierda)



#-----------------------------------------------------------------------------------------------------------------------
# Main que llamara la interfaz
#-----------------------------------------------------------------------------------------------------------------------

def main():
    app = QtGui.QApplication(sys.argv)
    I = Interfaz()
    I.show()
    sys.exit(app.exec_())

if __name__=='__main__':
    main()