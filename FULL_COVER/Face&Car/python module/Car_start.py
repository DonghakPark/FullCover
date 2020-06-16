import cv2
import time
import Car_Number_Recog

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
    #Jetson Nano 카메라 사용을 위한 파이프라인

def start():
    camera = cv2.VideoCapture(gstreamer_pipeline(flip_method=0), cv2.CAP_GSTREAMER)
    #Jetson Nano 카메라 오픈
    count = 0

    while True:
        (grabbed, frame) = camera.read()
        count += 1
        if not grabbed:
            break

        cv2.imshow("Tracking", frame)
        time.sleep(0.025)

        print(count)
        if count == 40:
            cv2.imwrite('temp.jpg', frame)
            break
    camera.release()
    cv2.destroyAllWindows()
    result = Car_Number_Recog.Recog()
    # 카메라를 통해서 사진을 촬영 후 반환
    return result
