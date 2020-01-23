import numpy as np 
import cv2 
  
# This will return video from the first webcam on your computer. 
#cap = cv2.VideoCapture("/home/whirldata/FaceNet/FrameWork/VID_20191209_171031.mp4") 
# cap = cv2.VideoCapture("rtsp://admin:123456@192.168.1.108/live/ch1")
cap = cv2.VideoCapture(0)

frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
  
# cap = cv2.VideoCapture('/home/whirldata/Videos/Light_Color_Classfiction/Package/test_Videos/VID-20191106-WA0023.mp4')
out = cv2.VideoWriter('outpy_fast_person_slow_Motion_mobile.avi', cv2.VideoWriter_fourcc(*'MJPG'),  10, (frame_width, frame_height))
# out = cv2.VideoWriter('outpy_fast_person_slow_Motion_mobile.mp4', cv2.VideoWriter_fourcc(*'MP4V'),  20, (1280, 720))
  
# Define the codec and create VideoWriter object 
# fourcc = cv2.VideoWriter_fourcc(*'XVID') 
# fourcc = cv2.VideoWriter_fourcc(*'FMP4')


# out = cv2.VideoWriter('/home/whirldata/Documents/Python_Task/Python-Task/opencv/output.avi', fourcc, 20.0, (640, 480)) 
# loop runs if capturing has been initialized.  
while(True): 
    # reads frames from a camera  
    # ret checks return at each frame 
    ret, frame = cap.read()  
    # print(frame)
  
    # Converts to HSV color space, OCV reads colors as BGR 
    # frame is converted to hsv 
    # hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) 
      
    # output the frame 
    out.write(frame)  
      
    # The original input frame is shown in the window  
    #cv2.imshow('Original', frame) 
  
    # The window showing the operated video stream  
    # cv2.imshow('fr/ame', hsv) 
  
      
    # Wait for 'a' key to stop the program  
    if cv2.waitKey(1) & 0xFF == ord('a'): 
        break
  
# Close the window / Release webcam 
cap.release() 
  
# After we release our webcam, we also release the output 
out.release()  
  
# De-allocate any associated memory usage  
cv2.destroyAllWindows()











