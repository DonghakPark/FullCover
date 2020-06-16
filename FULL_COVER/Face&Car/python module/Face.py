import cv2
import numpy as np
import os
from PIL import Image

def Face_reg():
    labels = ["Dong","Hong"] #사용자 라벨
 
    def gstreamer_pipeline(
        capture_width=400,
        capture_height=400,
        display_width=400,
        display_height=400,
        framerate=30,
        flip_method=0,
    ):
        return (
        "nvarguscamerasrc ! "
        "video/x-raw(memory:NVMM), "
        "width=(int)%d, height=(int)%d, "
        "format=(string)NV12, framerate=(fraction)%d/1 ! "
        "nvvidconv flip-method=%d ! "
        "video/x-raw, width=(int)%d, height=(int)%d, format=(string)BGRx ! "
        "videoconvert ! "
        "video/x-raw, format=(string)BGR ! appsink"
        % (
            capture_width,
            capture_height,
            framerate,
            flip_method,
            display_width,
            display_height,
        )
    )
    #Jetson Nano에서 사용할 카메라 파이프라인

    face_cascade = cv2.CascadeClassifier('./haarcascade_frontalface_default.xml')
    #OpenCV 모델 로드
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read("face-trainner.yml") 
    #recognizer 설정

    cap = cv2.VideoCapture(gstreamer_pipeline(flip_method=0), cv2.CAP_GSTREAMER)
    #카메라 오픈

    if cap.isOpened() == False :
        exit()

    count =0
    name = ''
    while True :
        ret, img = cap.read() 
        gray  = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
        #그레이 색상으로 변경
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)

        for (x, y, w, h) in faces :
            roi_gray = gray[y:y+h, x:x+w] 

            id_, conf = recognizer.predict(roi_gray)
            #카메라로 부터 오는 frame을 recognizer로 전송
            print(id_, conf)
            #정확도 출력 (cmd창에)
            if conf>=50:
                font = cv2.FONT_HERSHEY_SIMPLEX 
                name = labels[id_]
                cv2.putText(img, name, (x,y), font, 1, (0,0,255), 2)
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
                if conf>=67:
                    count =1
            #정확도와 라벨명을 이미지에 씌운다.

        print("Recognize")

        if count ==1:
            cv2.imwrite('Face_result.jpg', img) 
            break
 
    cap.release()
    cv2.destroyAllWindows()
    #열어둔 카메라 닫기
    return name, conf