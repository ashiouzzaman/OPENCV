import cv2 as cv

# Reading image from directory
img = cv.imread("Photos/cat.jpg")

# Showing Image
cv.imshow("Pussy Cat", img)


cv.waitKey(0)

