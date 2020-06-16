import sys
import urllib.request
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import uic
import sensing
import time
import matplotlib.pyplot as plt
from gasLeakage import *
import pandas as pd
import datetime

form_class = uic.loadUiType("sensor.ui")[0]

class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

        self.btn_1.clicked.connect(self.button1Function)

    def button1Function(self) :
        
        count =0    
        temp = []
        temp2 = []
        gas = gasLeakage()

        while True:
            getData = gas.getSensorData()
            gas.controlFan(getData)

            print("[DEBUG] Smoke Sensor Value = %u"%(getData))

            data = [[datetime.datetime.now(), getData]]
            submission = pd.DataFrame(data)
            submission.to_csv('./Gas_DataSet.csv', header = False, mode = 'a', index = False)
            time.sleep(0.5)
            temp.append(getData)
            temp2.append(str(getData))
            count +=1
            if count >= 15:
                break
        
        auth = 0
        for element in temp:
            if element >= 200:
                auth = 1
            
        if auth == 1:
            self.textBrowser_2.setPlainText("위험상황입니다.")
        else:
            self.textBrowser_2.setPlainText("정상입니다.")
        self.textBrowser_3.setPlainText("정상입니다.")

        view = self.listView
        model = QStandardItemModel()
        for f in temp2:
            model.appendRow(QStandardItem(f))
        view.setModel(model)

        plt.plot(temp, color='red')
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

if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()