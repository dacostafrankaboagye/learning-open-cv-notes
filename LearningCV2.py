import cv2 as cv
import numpy as np


# Image transformation

# Translation
# shifting an image along the x and y axis
# do a translation fnx parameters(img, x,y) x and y = pixels to shift along the x and y
# the fnx returns cv.wrapAffine(img, trnaMatrix, dimensions)
# create a translation matrix >> np.float32([[1,0,x],[0,1,y]])
# dimensions = tuple of (w,h) >> (img.shape[1], img.shape[0])
# -x ==> left
# x ==> right
# -y ==> up
# y ==> down

def translate(img, x, y):
    transMat = np.float32([[1, 0, x], [0, 1, y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)


img = cv.imread("circuit_elements/capacitor1.jpg")
cv.imshow("img", img)
translated = translate(img, -60, 30)
cv.imshow("trans", translated)
#
# cv.waitKey(0)


# rotation
# do a rotating fnx, para(img, angle, rotPoint=None)
# take the height and width of the image
# if rotating point is none, we rotate about the center ; rotPoint = (w//2, h//2)
# rotation matrix ==> cv.getRotationMatrix2D(rotPoint, angle, scaleVlue=1.0)
# dimensions = width and height tuple
#return cv.warpAffine(img, rotMatrix, dimension)

def rotate(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2, height//2)

    rotMatrix = cv.getRotationMatrix2D(rotPoint, angle, scale=1.0)
    dimensions = (width, height)
    return cv.warpAffine(img, rotMatrix, dimensions)

img = cv.imread("circuit_elements/capacitor1.jpg")
cv.imshow("img1", img)


rotated = rotate(img, 180)
# for clockwise the angle should be negative

cv.imshow("rotated", rotated)
# cv.waitKey(0)


# flipping
#cv.flip(img, flipcode)
#flipcode can be 0= vertical flip : over the x axis, 1: horizontal flip: over the y axis, -1 : both

# img = cv.imread("circuit_elements/capacitor1.jpg")
# cv.imshow("img1", img)
#
# flipped_x = cv.flip(img, 0)
# cv.imshow("flipped_x", flipped_x)
#
# flipped_y = cv.flip(img, 1)
# cv.imshow("flipped_y", flipped_y)
#
# flipped_b = cv.flip(img, -1)
# cv.imshow("flipped_b", flipped_b)
#
# cv.waitKey(0)


# contour detection
# [img --> gray --> blur --> canny edges --> find contours ]

# method 1

# read the image
# convert to grayscale ==> cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# now grab the images using the canny
# now find the contours ==> it returns two things: contours and hierarchies
# use the cv.contours(canny, mode, method)
# mode = cv.RET_TREE= all the hierarchical contours OR cv.RETR_EXTERNAL = for external contours
# OR cv.RETR_LIST = all the conyours in the image
#method = cv.CHAIN_APPROX_NONE or cv.CHAIN_APPROX_SIMPLE = compresses all the methods that are returned

# blur the images before you find the edges

# edgesimg = cv.imread("Resources/Photos/cats.jpg");
# cv.imshow("img1", img)
# 
# grayed = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow("grayed", grayed)
# 
# blur = cv.GaussianBlur(grayed, (5,5), cv.BORDER_DEFAULT)
# cv.imshow("blurred", blur)
# 
# canny = cv.Canny(blur, 125, 175)
# cv.imshow("canny edges", canny)
# 
# contours, hierarchy = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
# print(f"There were {len(contours)} contour(s) found!!")
# 
# cv.waitKey(0)

# method 2

# img = cv.imread("Resources/Photos/cats.jpg");
# cv.imshow("img1", img)
#
# grayed = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow("grayed", grayed)
#
# ret, thresh = cv.threshold(grayed, 125, 255, cv.THRESH_BINARY)  # converting to binary form
# # threshold = 125 the Max = 255  do forget the binary
# cv.imshow("threshed", thresh)
#
# contours, hierarchy = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
# print(f"There were {len(contours)} contour(s) found!!")
#
# cv.waitKey(0)


# lets drwa the contours that open cv found on on a blank image

img = cv.imread("Resources/Photos/cats.jpg");
cv.imshow("img1", img)

grayed = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("grayed", grayed)

ret, thresh = cv.threshold(grayed, 125, 255, cv.THRESH_BINARY)  # converting to binary form
# threshold = 125 the Max = 255  do forget the binary
cv.imshow("threshed", thresh)

contours, hierarchy = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f"There were {len(contours)} contour(s) found!!")

blank = np.zeros(img.shape, dtype='uint8')
cv.imshow("blanked", blank)

cv.drawContours(blank, contours, -1, (0,0,255), 2)
cv.imshow("blank", blank)

# threshold is something

cv.waitKey(0)
