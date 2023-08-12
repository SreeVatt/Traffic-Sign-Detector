import time
from pymata4 import pymata4
import winsound
import multiprocessing

import cv2





count=0
trigpin=11
ecopin=12

board = pymata4.Pymata4()


def the_callback(data):
    global count
    print("distance :", data[2])
    if data[2] < 100:
        winsound.Beep(500 - data[2], 500 - data[2])


def Disrtdetct():
    board.set_pin_mode_sonar(trigpin,ecopin,the_callback)
    while True:
        try:
            time.sleep(1)
            board.sonar_read(trigpin)
        except:
            board.shutdown()

def Red_detection():
    print("Starting Detection")
    f=2500
    d=50
    ss= cv2.CascadeClassifier("C:\Users\sreev\OneDrive\Documents\GitHub\Initial")
    cap =cv2.VideoCapture(0)

    cap.set(4,480)
    cap.set(3,360)
    k=0
    while True:
        ret, img =cap.read()
        gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        cv2.imshow("Screen",img)
        SS=ss.detectMultiScale(gray,1.3,5)
        for(x,y,w,s) in SS:
            print("Stop Sign Detected",k)
            winsound.Beep(1500,500)
            k=k+1

        key = cv2.waitKey(30)
        if key == ord('q'):
            cap.release()


if __name__ == '__main__':
    (Red_detection() and Disrtdetct())
