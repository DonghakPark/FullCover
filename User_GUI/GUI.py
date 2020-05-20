import sys
from PyQt5.Qtwidgets import QApplication, Qwidget

class Myapp(Qwidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle(" Full_Cover ")
        self.move(300,300)
        self.resize(400, 200)
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    wx = Myapp()
    sys.exit(app.exec_())