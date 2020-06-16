# -*-coding utf-8-*-
import sys
import urllib.request
import cv2
import time
import numpy as np
import threading
import pytesseract
import matplotlib.pyplot as plt
from concurrent.futures import ThreadPoolExecutor
import PIL
import pandas as pd
import datetime

# import pdb

import Face
import start
import Car_Number_Recog

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import uic

form_class = uic.loadUiType("./ui/main.ui")[0]


class MainWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # 초기 화면를 띄우는 코드

        self.facebtn.clicked.connect(self.facebtnFunction)  # 초기 화면의 1번 버튼 ( 안면 인식 )
        self.carbtn.clicked.connect(self.carbtnFunction)  # 초기 화면의 2번 버튼 ( 차량 번호판 인식)

    def facebtnFunction(self):
        FaceMainClass(self)  # 버튼 클릭시 안면 인식 기능 GUI를 띄운다.

    def carbtnFunction(self):  # 버튼 클릭시 차량 번호판 인식 기능 GUI를 띄운다.
        CarMainClass(self)


class FaceMainClass(QDialog):  # 안면 인식 기능 GUI
    def __init__(self, parent):
        super(FaceMainClass, self).__init__(parent)
        option_ui = "./ui/FaceMain.ui"
        uic.loadUi(option_ui, self)  # 지정된 UI 파일을 불러옴
        self.show()  # UI 파일을 받아오고 출력하는 함수

        # 버튼에 기능을 연결하는 코드
        self.btn_1.clicked.connect(self.button1Function)
        self.btn_2.clicked.connect(self.button2Function)

    def button1Function(self):  # btn_1이 눌리면 작동할 함수
        face1class(self)

    def button2Function(self):  # btn_2가 눌리면 작동할 함수
        t_executor = ThreadPoolExecutor(1)
        t = t_executor.submit(Face.Face_reg)  # 원할히 GUI를 구동하기 위해 스레드 사용

        while True:
            if t.done():  # 스레드가 종료 되었을 때
                name, conf = t.result()  # 결과값을 받아옴 Loop 탈출
                break

        self.qPixmapFileVar = QPixmap()
        self.qPixmapFileVar.load("Face_result.jpg")
        self.qPixmapFileVar = self.qPixmapFileVar.scaledToWidth(350)
        self.lbl_picture.setPixmap(self.qPixmapFileVar)  # 안면인식을 통해 얻어온 결과 사진 출력
        self.lbl2_picture.setText(name)  # 해당 사용자 이름 출력

        check = pd.read_csv('facedata.csv')  # 저장된 csv 파일을 읽어옴
        temp = np.array(pd.DataFrame(check, columns=['name']))
        if name in temp:  # 사용자 이름이 저장된 csv 파일에 존재한다면
            self.lbl2_picture_2.setText("문 열림\n %.2f Accur" % conf)  # 문열림
        else:
            self.lbl2_picture_2.setText("미 등록 사용자")


f_name = []
f_home = []


class face1class(QDialog):  # 사용자 정보 등록 UI
    def __init__(self, parent):
        super(face1class, self).__init__(parent)
        option_ui = "./ui/face1.ui"
        uic.loadUi(option_ui, self)
        self.show()
        self.btn_Text.clicked.connect(self.btn_printTextFunction)  # 이줄은 저장 버튼

    def btn_printTextFunction(self):  # 저장버튼 함수

        # Lineedit의 글자를 배열에 저장
        f_name.append(self.lineedit_Test1.text())  # UI에 쓰여진 정보를 해당 변수에 저장
        f_home.append(self.lineedit_Test2.text())
        data = [[f_name[-1], f_home[-1]]]
        submission = pd.DataFrame(data)  # 저장된 데이터를 데이터 프레임으로 변환
        submission.to_csv('./facedata.csv', header=False, mode='a', index=False)  # 변환된 데이터 프레임을 csv 파일로 저장
        self.close()


c_name = []
c_home = []
c_num = []


class car1Class(QDialog):  # 차량 등록 UI
    def __init__(self, parent):
        super(car1Class, self).__init__(parent)
        option_ui = "./ui/car1.ui"
        uic.loadUi(option_ui, self)
        self.show()

        self.btn_Text.clicked.connect(self.btn_printTextFunction)  # 이줄은 저장 버튼

    def btn_printTextFunction(self):  # 저장버튼 함수
        # Lineedit의 글자를 배열에 저장
        c_name.append(self.lineedit_Test1.text())
        c_home.append(self.lineedit_Test2.text())
        c_num.append(self.lineedit_Test3.text())
        data = [[c_name[-1], c_home[-1], c_num[-1]]]
        submission = pd.DataFrame(data)  # 입력된 데이터를 데이터 프레임으로 변환
        submission.to_csv('./cardata.csv', header=False, mode='a', index=False)  # 변환된 데이터 프레임을 csv 파일로 변환
        self.close()


class CarMainClass(QDialog):  # 차량 번호판 인식 기능 GUI
    def __init__(self, parent):
        super(CarMainClass, self).__init__(parent)
        option_ui = "./ui/carmainTest.ui"
        uic.loadUi(option_ui, self)
        self.show()

        # 버튼에 기능을 연결하는 코드
        self.btn_1.clicked.connect(self.button1Function)
        self.btn_2.clicked.connect(self.button2Function)

    def button1Function(self):  # 1번 버튼 클릭시

        car1Class(self)

    def button2Function(self):  # 2번 버튼 클릭시

        t_executor1 = ThreadPoolExecutor(1)
        t1 = t_executor1.submit(start.start)  # 원활한 GUI 구동을 위해 스레드 사용
        show = ""
        while True:
            if t1.done():  # 스레드 종료 시
                print("Recognition complete")
                show = t1.result()  # 결과를 저장

                break
        self.qPixmapFileVar = QPixmap()
        self.qPixmapFileVar.load("result.jpg")
        self.qPixmapFileVar = self.qPixmapFileVar.scaledToWidth(350)
        self.lbl_picture.setPixmap(self.qPixmapFileVar)  # 결과 이미지 표시
        self.lbl2_picture.setText(show)

        check = pd.read_csv('cardata.csv')  # csv파일을 읽어옴
        temp = np.array(pd.DataFrame(check, columns=['car']))

        if show in temp:  # csv파일안에 등록된 번호와 동일하면
            self.lbl2_picture_2.setText("문 열림" + Location)  # 문 열림 과 주차위치 지정
        else:
            self.lbl2_picture_2.setText("미 등록 사용자")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MainWindow()
    myWindow.show()
    app.exec_()