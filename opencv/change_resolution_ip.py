import cv2
import time
# cap = cv2.VideoCapture(0)
cap = cv2.VideoCapture("rtsp://admin:123456@192.168.1.63/live/ch1")

# cap = cv2.VideoCapture("rtsp://admin:123456@192.168.1.108/live/ch1")
# if not (cap.isOpened()):
#     print("Could not open video device")

# def make_1080p():
#     cap.set(3, 1920)
#     cap.set(4, 1080)

# def make_720p():
# cap.set(cv2.CAP_PROP_FRAME_WIDTH, 160)

# cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 120)
# def rescale_frame(frame, percent=75):
#     width = int(frame.shape[1] * percent/ 100)
#     height = int(frame.shape[0] * percent/ 100)
#     dim = (width, height)
#     return cv2.resize(frame, dim, interpolation =cv2.INTER_AREA)

# def make_480p():
#     cap.set(3, 640)
#     cap.set(4, 480)

# def change_res(width, height):
#     cap.set(3, width)
#     cap.set(4, height)

# make_720p()


# cap = cv2.VideoCapture(0)

cap.set(3,1280)

cap.set(4,720)

# time.sleep(2)

# cap.set(15, -8.0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    # frame75 = rescale_frame(frame, percent=75)
    # cv2.imshow('frame75', frame75)
    # frame150 = rescale_frame(frame, percent=150)
    # cv2.imshow('frame75', frame150)
    print(frame.shape)

    # Our operations on the frame come here
    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame   
    cv2.imshow('frame',frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()