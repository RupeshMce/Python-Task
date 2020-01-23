import cv2  
import numpy as np  
    
# path to input images are specified and   
# images are loaded with imread command  
image1 = cv2.imread('/home/whirldata/Downloads/IMG_0432.JPG')  
image2 = cv2.imread('/home/whirldata/Downloads/IMG_0449.JPG') 
  
# cv2.subtract is applied over the 
# image inputs with applied parameters 
sub = cv2.subtract(image1, image2) 
cv2.imwrite("sub.png",sub)
  
# the window showing output image 
# with the subtracted image  
cv2.imshow('Subtracted Image', sub) 
  
# De-allocate any associated memory usage   
if cv2.waitKey(0) & 0xff == 27:  
    cv2.destroyAllWindows()  
