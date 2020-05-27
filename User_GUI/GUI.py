import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QListView
from PyQt5.QtGui import QIcon

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        btn1 = QPushButton('차량 번호 등록', self)
        btn1.setGeometry(30, 100, 180, 60)

        btn2 = QPushButton("차량 인식", self)
        btn2.setGeometry(30, 200, 180, 60)

        Carnum = QListView(self)
        self.setWindowTitle("Car_Number_recognizer")
        self.setWindowIcon(QIcon('./dku_logo.png'))
        self.setGeometry(300,300,1000,600)
        self.show()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())