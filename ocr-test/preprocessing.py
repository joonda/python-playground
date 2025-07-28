#  image preprocessing

import cv2

img = cv2.imread('./img/test.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.medianBlur(gray, 5)
gray = cv2.filter2D(gray, -1, cv2.getGaussianKernel(5, 0))

_, binary = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)

cv2.imwrite('./img/test_clean.png', binary)
