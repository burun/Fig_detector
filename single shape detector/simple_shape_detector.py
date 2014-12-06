import numpy as np
import cv2

img = cv2.imread('100.jpg')
gray = cv2.imread('100.jpg', 0)

ret, thresh = cv2.threshold(gray, 100, 255, 1)
_, contours, hierarchy = cv2.findContours(thresh, 1, 2)


for cnt in contours:
    approx = cv2.approxPolyDP(cnt, 0.1 * cv2.arcLength(cnt, True), True)
    print len(approx)
    if len(approx) == 5:
        print "pentagon"
        cv2.drawContours(img, [cnt], 0, 255, -1)
    elif len(approx) == 3:
        print "triangle"
        cv2.drawContours(img, [cnt], 0, (0, 255, 0), -1)
    elif len(approx) == 4:
        print "square"
        cv2.drawContours(img, [cnt], 0, (0, 0, 255), 2)
    elif len(approx) == 9:
        print "half-circle"
        cv2.drawContours(img, [cnt], 0, (255, 255, 0), -1)
    elif len(approx) > 15:
        print "circle"
        cv2.drawContours(img, [cnt], 0, (0, 255, 255), -1)

while(1):
    cv2.imshow('img', img)
    k = cv2.waitKey(0)
    if k == 27:
        break
    cv2.destroyAllWindows()
