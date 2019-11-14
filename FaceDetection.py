import cv2
import numpy as np
f_detect = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
e_detect = cv2.CascadeClassifier("haarcascade_eye.xml")
d_Video = cv2.VideoCapture(1)
white True:
  ret,img = d_Video.read()
  gScale = cv2.cvtColor(img,cv2.COLOR_BG2GRAY)
  d_Face = f_detect.detectMultiScale(gScale,1.3,5)
  for(x,y,w,h) in d_Face:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,198),2)
    egScale = gScale[y:y+h,w:w+h]
    eColor = img[y:y+h,w:w+h]
    eye = e_detect.detectMultiScale(egScale)
    for (ex,ey,ew,eh) in eye:
      cv2.rectangle(eColor,(ex,ey),(ex+ew,ey+eh),(255,0,0),2)
    cv2.imshow('img',img)
    button = cv2.waitKey(30) & 0xff
    if button == 27:
      break
d_video.release()
d_video.destroyAllWindows()
