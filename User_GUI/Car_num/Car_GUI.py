import sys
import urllib.request
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import uic
import numpy as np
import cv2
from PyQt5 import QtCore
from PyQt5 import QtWidgets
from PyQt5 import QtGui

#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType("pushbuttonTest.ui")[0]

class ShowVideo(QtCore.QObject):

    flag = 0

    camera = cv2.VideoCapture(0)

    ret, image = camera.read()
    height, width = image.shape[:2]

    VideoSignal1 = QtCore.pyqtSignal(QtGui.QImage)

    def __init__(self, parent=None):
        super(ShowVideo, self).__init__(parent)

    @QtCore.pyqtSlot()
    def startVideo(self):
        global image

        run_video = True
        while run_video:
            ret, image = self.camera.read()
            color_swapped_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

            qt_image1 = QtGui.QImage(color_swapped_image.data,
                                    self.width,
                                    self.height,
                                    color_swapped_image.strides[0],
                                    QtGui.QImage.Format_RGB888)
            self.VideoSignal1.emit(qt_image1)

            loop = QtCore.QEventLoop()
            QtCore.QTimer.singleShot(25, loop.quit) #25 ms
            loop.exec_()


class ImageViewer(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(ImageViewer, self).__init__(parent)
        self.image = QtGui.QImage()
        self.setAttribute(QtCore.Qt.WA_OpaquePaintEvent)

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        painter.drawImage(0, 0, self.image)
        self.image = QtGui.QImage()

    def initUI(self):
        self.setWindowTitle('Test')

    @QtCore.pyqtSlot(QtGui.QImage)
    def setImage(self, image):
        if image.isNull():
            print("Viewer Dropped frame!")

        self.image = image
        if image.size() != self.size():
            self.setFixedSize(image.size())
        self.update()

#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

        #버튼에 기능을 연결하는 코드
        self.btn_1.clicked.connect(self.button1Function)

        self.btn_2.clicked.connect(self.button2Function)

    #btn_1이 눌리면 작동할 함수
    def button1Function(self) :
        print("btn_1 Clicked")

    #btn_2가 눌리면 작동할 함수
    def button2Function(self) :


        # self.qPixmapFileVar = QPixmap()
        # self.qPixmapFileVar.load("증명.png")
        # self.qPixmapFileVar = self.qPixmapFileVar.scaledToWidth(150)
        # self.lbl_picture.setPixmap(self.qPixmapFileVar)


if __name__ == "__main__" :
    app = QApplication(sys.argv)

    myWindow = WindowClass()
    myWindow.show()
    app.exec_()