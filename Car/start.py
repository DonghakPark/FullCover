import cv2
import time
import Car_Number_Recog

def start():
    camera = cv2.VideoCapture(0)
    count = 0

    while True:
        (grabbed, frame) = camera.read()
        count += 1
        if not grabbed:
            break

        cv2.imshow("Tracking", frame)
        time.sleep(0.025)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
        print(count)
        if count == 40:
            cv2.imwrite('temp.jpg', frame)
            break
    camera.release()
    cv2.destroyAllWindows()
    result = Car_Number_Recog.Recog()

    return result