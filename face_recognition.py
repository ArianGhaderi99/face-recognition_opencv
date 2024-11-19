import cv2

# load the cascade
face_cascade= cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

#To capture video from webcam
capture= cv2.VideoCapture(0)


while True:
  
  #read the frame
  ret,img=capture.read()

  #convert to grayscale
  gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

  #Detect the faces
  faces= face_cascade.detectMultiScale(gray,1.1,4)

  #Draw rectangle around each faces
  for x , y , w , h in faces:
    cv2.rectangle(img,(x,y),(x+w , y+h),(255,0,0),2)

  #Display
  cv2.imshow("img",img)
  k= cv2.waitKey(30)

#release the videocapture object
cap.release()