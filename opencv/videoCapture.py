import cv2
# cap = cv2.VideoCapture("192.168.43.228:8080")
cap = cv2.VideoCapture("rtsp://admin:123456@192.168.1.63/live/ch1")

# cap = cv2.VideoCapture("rtsp://admin:123456@192.168.1.108/live/ch1")
if not (cap.isOpened()):
    print("Could not open video device")
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame   
    cv2.imshow('frame',frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()