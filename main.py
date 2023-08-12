import cv2
import winsound


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
        k=k+1
        winsound.Beep(500,500)
    key = cv2.waitKey(30)
    if key == ord('q'):
        cap.release()

