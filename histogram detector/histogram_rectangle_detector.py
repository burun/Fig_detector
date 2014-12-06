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
    img = cv2.imread('43.jpg')
    gray = cv2.imread('43.jpg', 0)

    thresh_value = cv2.getTrackbarPos('thresh', 'img')
    maxval = cv2.getTrackbarPos('maxval', 'img')
    thresh_type = cv2.getTrackbarPos('type', 'img')

    # Threshold and find all contours
    ret, thresh = cv2.threshold(gray, thresh_value, maxval, thresh_type)
    # thresh = cv2.adaptiveThreshold(
    #     gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 3, 5)
    _, contours, hierarchy = cv2.findContours(thresh, 1, 2)

    rectangles = []

    # Select rectangles
    for cnt in contours:
        approx = cv2.approxPolyDP(
            cnt, 0.01 * cv2.arcLength(cnt, True), True)
        if len(approx) == 4:
            rectangles.append(cnt)

    # Find the largest rectangles and draw contours
    areas = [cv2.contourArea(c) for c in rectangles]
    max_index = np.argsort(areas)
    for i in max_index:
        cnt = rectangles[i]
        # cv2.drawContours(img, [cnt], 0, (0, 0, 255), 2)
        x, y, w, h = cv2.boundingRect(cnt)
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imshow('img', img)
    k = cv2.waitKey(0)
    if k == 27:
        break

cv2.destroyAllWindows()
