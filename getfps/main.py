import string
import cv2
import time


def main ():

    print(cv2.__version__)
    width = 640
    height = 460
    cam = cv2.VideoCapture(2)
    cam.set(cv2.CAP_PROP_FRAME_WIDTH,width)
    cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
    cam.set(cv2.CAP_PROP_FPS,60)
    cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))

    while(True):
        ignore, frame = cam.read()
        cv2.imshow('webcam',frame)
        cv2.moveWindow('webcam',0,0)
        
        if cv2.waitKey(1) & 0xff == ord('q'):
            break
    cam.release()

if __name__ == "__main__":
    main()