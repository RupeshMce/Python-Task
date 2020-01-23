import cv2
import imutils

# Read image and convert it to grayscale. 
image = cv2.imread('/home/whirldata/body_measurment/mask/IMG_0432.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (15, 15), 0)
cv2.imshow('gray', imutils.resize(gray,width = 500))
 
# threshold the image, then perform a series of erosions +
# dilations to remove any small regions of noise
# thresh = cv2.threshold(gray, 45, 255, cv2.THRESH_BINARY)[1]
# cv2.imshow('thresh', imutils.resize(thresh,width = 500))
# thresh = cv2.erode(thresh, None, iterations=2)
# cv2.imshow('erode', imutils.resize(thresh,width = 500))
# thresh = cv2.dilate(thresh, None, iterations=2)
# cv2.imshow('dilate', imutils.resize(thresh,width = 500))
 
# find contours in thresholded image, then grab the largest
# one
cnts = cv2.findContours(gray.copy(), cv2.RETR_EXTERNAL,
	cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
c = max(cnts, key=cv2.contourArea)

cv2.drawContours(image, [c], -1, (0, 255, 255), 10)

# Display the image.
cv2.imshow('img', imutils.resize(image,width = 500))
k=cv2.waitKey(0)
if k == 27:
    print("Check")
    cv2.imwrite("Human_Contour.png",image)
