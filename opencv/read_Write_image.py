import cv2

color=cv2.imread("/home/whirldata/Documents/Python_Task/Python-Task/opencv/img1.jpg",1)

cv2.imshow('image',color)
k=cv2.waitKey(0)


if k == 27:
    print("Check")
elif k==ord("g"):
    grayscale=cv2.imread("/home/whirldata/Documents/Python_Task/Python-Task/opencv/img1.jpg",0)
    cv2.imwrite("grayscale.png",grayscale)
    exit()

elif k==ord("o"):
    cv2.imwrite("color.png",color)
    exit()

elif k==ord("a"):
    alpha=cv2.imread("/home/whirldata/Documents/Python_Task/Python-Task/opencv/img1.jpg",-1)
    cv2.imwrite("alpha.png",alpha)
    exit()

cv2.destroyAllWindows()