import sys
import urllib.request
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import uic

form_class = uic.loadUiType("capstone.ui")[0]
#화면을 띄우는데 사용되는 Class 선언

d = []
f = []
class OptionWindow(QDialog) :


    def __init__(self, parent):
        super(OptionWindow, self).__init__(parent)
        option_ui = "capstone2.ui"
        uic.loadUi(option_ui, self)
        self.show()

        # 버튼에 기능을 할당하는 코드

        self.btn_Text.clicked.connect(self.btn_printTextFunction)     #이줄은 저장 버튼


    def btn_printTextFunction(self):      #저장버튼 함수

        # Lineedit의 글자를 배열에 저장
        d.append(self.lineedit_Test1.text())
        f.append(self.lineedit_Test2.text())
        print(d)
        print(f)



class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

        #버튼에 기능을 연결하는 코드
        self.btn_1.clicked.connect(self.button1Function)
        self.btn_2.clicked.connect(self.button2Function)



    #btn_1이 눌리면 작동할 함수
    def button1Function(self) :
        OptionWindow(self)

    #btn_2가 눌리면 작동할 함수
    def button2Function(self) :
        self.qPixmapFileVar = QPixmap()
        self.qPixmapFileVar.load("증명.png")
        self.qPixmapFileVar = self.qPixmapFileVar.scaledToWidth(150)
        self.lbl_picture.setPixmap(self.qPixmapFileVar)




if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()



