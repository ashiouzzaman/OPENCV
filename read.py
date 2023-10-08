import cv2 as cv

# # Reading image from directory
# img = cv.imread("Photos/cat.jpg")

# # Showing Image
# cv.imshow("Pussy Cat", img)

# Reading video
video = cv.VideoCapture('Videos/kitten.mp4')

while True:
    isTrue, frame = video.read()
    cv.imshow('Kitten Video', frame)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

video.release()
cv.destroyAllWindows()





# cv.waitKey(0)

