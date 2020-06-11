import cv2

def Face_reg():
    labels = ["Dong", "Hong"]

    # def gstreamer_pipeline(
    #     capture_width=800,
    #     capture_height=600,
    #     display_width=800,
    #     display_height=600,
    #     framerate=60,
    #     flip_method=0,
    # ):
    #     return (
    #         "nvarguscamerasrc ! "
    #         "video/x-raw(memory:NVMM), "
    #         "width=(int)%d, height=(int)%d, "
    #         "format=(string)NV12, framerate=(fraction)%d/1 ! "
    #         "nvvidconv flip-method=%d ! "
    #         "video/x-raw, width=(int)%d, height=(int)%d, format=(string)BGRx ! "
    #         "videoconvert ! "
    #         "video/x-raw, format=(string)BGR ! appsink"
    #         % (
    #             capture_width,
    #             capture_height,
    #             framerate,
    #             flip_method,
    #             display_width,
    #             display_height,
    #         )
    #     )

    face_cascade = cv2.CascadeClassifier('./haarcascade_frontalface_default.xml')
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read("face-trainner.yml")

    cap = cv2.VideoCapture(0)
    if cap.isOpened() == False:
        exit()

    count = 0
    name = ""
    while True:
        ret, img = cap.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)

        for (x, y, w, h) in faces:
            roi_gray = gray[y:y + h, x:x + w]

            id_, conf = recognizer.predict(roi_gray)
            print(id_, conf)

            if conf >= 50:
                font = cv2.FONT_HERSHEY_SIMPLEX
                name = labels[id_]
                cv2.putText(img, name, (x, y), font, 1, (0, 0, 255), 2)
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
                if conf >=67:
                    count = 1

        cv2.imshow('Preview', img)

        if cv2.waitKey(10) >= 0 or count == 1:
            cv2.imwrite("Face_result.jpg", img)
            break

    cap.release()
    cv2.destroyAllWindows()
    return name