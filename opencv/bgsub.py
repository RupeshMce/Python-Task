import cv2
import numpy as np
# fgbg = cv2.createBackgroundSubtractorMOG2()

frame = cv2.imread('/home/whirldata/Downloads/IMG_0449.JPG')

# fgmask = fgbg.apply(frame)
cv2.imshow('frame', fgmask)
# if cv2.waitKey(1) & 0xFF == ord('q'):
#     break

cv2.imwrite("Human_Contour.png",fgmask)

# while(True):
#     ret, frame = cap.read()
#     fgmask = fgbg.apply(frame)
#     cv2.imshow('frame', fgmask)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()
