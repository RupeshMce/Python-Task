import cv2

img = cv2.imread("/home/whirldata/body_measurment/white_bg.jpg")

img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

a = img_gray.max()  
_, thresh = cv2.threshold(img_gray, a/2+60, a,cv2.THRESH_BINARY_INV)


contours, hierarchy = cv2.findContours(
                                   image = thresh.copy(), 
                                   mode = cv2.RETR_TREE, 
                                   method = cv2.CHAIN_APPROX_SIMPLE)

contours = sorted(contours, key = cv2.contourArea, reverse = True)

c_0 = contours[0]

x, y, w, h = cv2.boundingRect(c_0)
img_copy = img.copy()


img_box = cv2.rectangle(img_copy, (x, y), (x+w, y+h), color = (255, 0, 0), thickness = 2)



# final = cv2.drawContours(img_copy, contours, contourIdx = -1, 
                        #  color = (255, 0, 0), thickness = 2)




cv2.imshow("original_image",img)

cv2.imshow("gray_image",img_gray)

cv2.imshow("Threshold",thresh)

cv2.imshow("Countours",img_copy)


cv2.waitKey(0)
