import sys
import urllib.request
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import uic
#import sensing
import time
import matplotlib.pyplot as plt

form_class = uic.loadUiType("sensor.ui")[0]
#화면을 띄우는데 사용되는 Class 선언


class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

        #버튼에 기능을 연결하는 코드
        self.btn_1.clicked.connect(self.button1Function)

    #btn_1이 눌리면 작동할 함수
    def button1Function(self) :

        #while True:
        data = ['1','2','3']

        #for i in range(0,20):

            #get = sensing.sen()
            #data.append(str(get))

            #if get >= 250:
             #   self.textBrowser_2.setPlainText("위험상황입니다.")
            #else:
             #   self.textBrowser_2.setPlainText("정상입니다.")
            #self.textBrowser_3.setPlainText("정상입니다.")

        view = self.listView
        model = QStandardItemModel()
        for f in data:
            model.appendRow(QStandardItem(f))
        view.setModel(model)

        plt.plot(data, color='red')
        plt.xlabel("Time")
        plt.ylabel("Gas_data")
        plt.draw()
        fig = plt.gcf()
        fig.set_figwidth(320/fig.dpi)
        fig.set_figheight(240/fig.dpi)
        fig.savefig("myfile.png")

        self.qPixmapFileVar = QPixmap()
        self.qPixmapFileVar.load("myfile.png")
        self.qPixmapFileVar = self.qPixmapFileVar.scaled(320,240)
        self.lbl_picture.setPixmap(self.qPixmapFileVar)
        time.sleep(1)

if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()