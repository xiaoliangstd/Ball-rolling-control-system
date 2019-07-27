import cv2 as cv  







gray = cv.imread('sucai.png', cv.IMREAD_GRAYSCALE)

gray = cv.medianBlur(gray,5) 

edges = cv.Canny(gray, 50, 150, apertureSize = 3)


cv.imshow("dliang.png",edges)

cv.waitKey(0)