import numpy as np
import cv2


def nothing(x):
    pass

# Create a window
cv2.namedWindow('img')

# Create trackbars
cv2.createTrackbar('thresh', 'img', 0, 255, nothing)
cv2.createTrackbar('maxval', 'img', 0, 255, nothing)
cv2.createTrackbar('type', 'img', 0, 4, nothing)

# imshow
while(1):
    img = cv2.imread('balls.png')
    gray = cv2.imread('balls.png', 0)

    thresh_value = cv2.getTrackbarPos('thresh', 'img')
    maxval = cv2.getTrackbarPos('maxval', 'img')
    thresh_type = cv2.getTrackbarPos('type', 'img')

    # Threshold and find all contours
    ret, thresh = cv2.threshold(gray, thresh_value, maxval, thresh_type)
    _, contours, hierarchy = cv2.findContours(thresh, 1, 2)

    for cnt in contours:
        approx = cv2.approxPolyDP(cnt, 0.01 * cv2.arcLength(cnt, True), True)
        # print len(approx)
        if len(approx) == 5:
            # print "pentagon"
            cv2.drawContours(img, [cnt], 0, 255, 2)
        elif len(approx) == 3:
            # print "triangle"
            cv2.drawContours(img, [cnt], 0, (0, 255, 0), 2)
        elif len(approx) == 4:
            # print "square"
            cv2.drawContours(img, [cnt], 0, (0, 0, 255), 3)
        elif len(approx) == 9:
            # print "half-circle"
            cv2.drawContours(img, [cnt], 0, (255, 255, 0), 2)
        elif len(approx) > 15:
            # print "circle"
            cv2.drawContours(img, [cnt], 0, (0, 0, 255), 3)
    # Show the pictures
    cv2.imshow('img', img)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:  # ESC
        break

cv2.destroyAllWindows()
