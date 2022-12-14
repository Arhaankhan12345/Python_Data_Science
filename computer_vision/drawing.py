
import cv2
from datetime import datetime as dt

cam=cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_SIMPLEX
Color_black =(0,0,0,) # black
color_white = (225,225,225) # white

while cam.isOpened():
    status, image = cam.read()
    if status:
        # add a box
        cv2.rectangle(image,(5,5),(300,40),(0,225,0),-2)
        #add text
        cv2.putText(image,"Live camera Feed",(10,30),font, 1 ,Color_black, 1)
        # add a clock
        timestr=dt.now().strftime("%H:%M:%S")
        cv2.putText(image, timestr,(10,70), font,1, Color_black,2)
        cv2.imshow("live Camera",image)
        if cv2.waitKey(1)==27:# 27 is the ASCII for the Escape key
            break
cam.release()
cv2.destroyAllWindows()