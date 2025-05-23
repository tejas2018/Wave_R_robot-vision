"""
cv_ex1.py - read and show image

"""
import cv2

# read the color image
img1 = cv2.imread('wisdom.jpg')
# img.shape : size of the image --> row,column,depth 
print(img1.shape)
print(img1)
# pop up window for image show
# cv2.imshow(title_name, image_array)
cv2.imshow('image color',img1)

# read the color image and turn it to grayscale
# cv2.imread(image_name,flag)
# flag=1 (defalut): color , flag=0:grayscale
img2 = cv2.imread('wisdom.jpg',0)


print(img2.shape)
print(img2)
# system will pause until it gets pressed key in 5000 ms
p=cv2.waitKey(5000)
# show the pressed key in ASCII code, if no key is pressed, p=-1
print('pressed key : ', p)

cv2.imshow('image gray',img2)

# cv2.waitKey(0) will pause the system until any key is pressed
cv2.waitKey(0)
# assign the Window to be closed
cv2.destroyWindow('image gray')

cv2.waitKey(0)
# close all windows
cv2.destroyAllWindows()
 
