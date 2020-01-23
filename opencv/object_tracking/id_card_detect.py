import imutils
import cv2
import numpy as np
from collections import deque

pts = deque(maxlen=100)

cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    yellowLower = (20, 100, 100)
    yellowUpper = (30,255,255)

    frame = imutils.resize(frame, width=600)
    blurred = cv2.GaussianBlur(frame, (11, 11), 0)
    hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
    
    mask = cv2.inRange(hsv, yellowLower, yellowUpper)
    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)

    cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    center = None

    if len(cnts) > 0:
    # find the largest contour in the mask, then use
    # it to compute the minimum enclosing circle and
    # centroid
        c = max(cnts, key=cv2.contourArea)
        # ((x, y), radius) = cv2.minEnclosingCircle(c)
        x,y,w,h = cv2.boundingRect(c)
        M = cv2.moments(c)
        center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
        pts.appendleft(center)
        # only proceed if the radius meets a minimum size
        if x > 10:
            # draw the circle and centroid on the frame,
            # then update the list of tracked points
            # cv2.circle(frame, (int(x), int(y)), int(radius),(0, 255, 255), 2)
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),5)

            cv2.circle(frame, (x+(w//2),y+(h//2)), 5, (0, 0, 255), -1)
        for i in range(1, len(pts)):
		# if either of the tracked points are None, ignore
		# them
            if pts[i - 1] is None or pts[i] is None:
                continue
    
            # otherwise, compute the thickness of the line and
            # draw the connecting lines
            thickness = int(np.sqrt(1 / float(i + 1)) * 2.5)
            cv2.line(frame, pts[i - 1], pts[i], (0, 0, 255), 5)
    frame = cv2.resize(frame, (1080, 720))
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()