import cv2
import dlib
import argparse


cap = cv2.VideoCapture("rtsp://admin:123456@192.168.1.108/live/ch1")
# cap = cv2.VideoCapture(0)
if not (cap.isOpened()):
    print("Could not open video device")
cnn_face_detector = dlib.cnn_face_detection_model_v1("/home/whirldata/FaceNet/FrameWork/demo/mmod_human_face_detector.dat")
def get_face_postion(bbox):
    return bbox.rect.left(),bbox.rect.top(),bbox.rect.right() - bbox.rect.left(),bbox.rect.bottom()-bbox.rect.top()

while(True):
    # Capture frame-by-frame
    # ret, frame = cap.read()
    frame = cv2.imread("/home/whirldata/FaceNet/Multiple_Face_Detection.jpg")
    print(ret)

    # Our operations on the frame come here
    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    try:
        faces_cnn = cnn_face_detector(frame, 1)
    except Exception as e:
        print(e)
        continue
    for face in faces_cnn:
        x = face.rect.left()
        y = face.rect.top()
        w = face.rect.right() - x
        h = face.rect.bottom() - y

     # draw box over face
        cv2.rectangle(image, (x,y), (x+w,y+h), (0,0,255), 2)


    # Display the resulting frame   
    cv2.imshow('frame',frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()



