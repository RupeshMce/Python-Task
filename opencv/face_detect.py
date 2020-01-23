import cv2
import face_recognition
import numpy

cap = cv2.VideoCapture(0)
while(True):
    try:
        # Capture frame-by-frame
        ret, frame = cap.read()
        # cv2.imwrite("data.jpg",frame)
        # image = face_recognition.load_image_file("data.jpg")
        face_landmarks_list = face_recognition.face_landmarks(frame)
        landmarks=[]
        for j in range(len(face_landmarks_list)):
            for i in face_landmarks_list[j]:
                landmarks.extend(face_landmarks_list[j][i])
        for i in landmarks:
            cv2.circle(frame,i, 1, (0,0,255), -1)



        # Our operations on the frame come here
        # gray = cv2.cvtColor(frame)

        # Display the resulting frame
        image  = cv2.resize(frame,(1080, 720))
        # image  = cv2.cvtColor(image,cv2.COLOR_RGB2BGR)
        cv2.imshow('frame',image)
        cv2.resizeWindow('frame', 800,600)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    except :
        continue
    

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()