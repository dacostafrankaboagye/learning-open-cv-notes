import cv2 as cv
import numpy as np


# reading images
# img = cv.imread("other_images/joshua-koblin-eqW1MPinEV4-unsplash.jpg")
#
# cv.imshow("c++", img)
# cv.waitKey(0)
# _________________________________________________________________________
# reading videos
#   parameter for the video capture is either an integer i.e for the webcam or the path
#   for the integer == webcam, 0  1=the camera first connected 2 = the camera secondly connected.
# we use a while loop to read the video frame by frame
# [ note: the capture.read() = reads the video frame by frame. returns two values : boolean & the frame.
#

# A error (-215:Assertion failed) would occur is a wrong path is given or python runs out of a frame

# capture = cv.VideoCapture(0)

# capture = cv.VideoCapture("other_videos/cat_human_short.mp4")
#
# while True:
#     isTrue, frame = capture.read()
#     cv.imshow("video",frame)
#
#     if cv.waitKey(20) & 0xFF == ord("d"):
#         break
#
# capture.release()
# cv.destroyAllWindows()

# _________________________________________________________________________

# resizing and rescaling videos and images

# method1: would work for images videos and live videos/camera
# it is a good practise to downscale your video file

# we are resizing to a particular dimension
# say dimension  = tuple of width and height  d = (w,h)

# to rescale frame use a fnx. to return cv.resize(frame, dimension, interpolation=cv.INTER_AREA)
# the function, two parameters = (a,b) = (frame and scale=0.75) u can set a default incase u forget
# not that frame.shape[1] = real width and frame.shape[0] = height ... multiple each by the scale
# and return an int of it as demonstrated

# the video
# def rescaleframe(frame, scale=0.55):
#     width = int (frame.shape[1] * scale)
#     height = int (frame.shape[0] * scale)
#     dimensions = (width, height)
#
#     return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)
#
# capture = cv.VideoCapture("other_videos/cat_human_short.mp4")
#
# while True:
#     isTrue, frame = capture.read()
#
#     frame_resized = rescaleframe(frame)
#
#     cv.imshow("video",frame_resized)
#     #cv.imshow("vid", frame)
#
#     if cv.waitKey(20) & 0xFF == ord("d"):
#         break
#
# capture.release()
# cv.destroyAllWindows()


# the image

# img = cv.imread("other_images/car2.jpg")
#
def resfr(frame, scale=0.30):
    w = int(frame.shape[1] * scale)
    h = int(frame.shape[0] * scale)
    dim = (w, h)
    return cv.resize(frame, dim, interpolation=cv.INTER_AREA)


#
# res = resfr(img)
# cv.imshow("img", res)
#
# cv.waitKey(0)

# another way to resizing or rescaling
#  note: would work for only live camera/ video [not given]


# _________________________________________________________________________

# drawing shapes and putting text
# we can work with a blank image

# blank image
# blank = np.zeros((500, 500), dtype="uint8")
# cv.imshow("blank", blank)

# painting the image certain color
# np.zeros((height, width, # of color channels), dtype="")
# blank = np.zeros((600, 600, 3), dtype='uint8')
# color = (0, 255, 0)  # green
# blank[:] = color
# cv.imshow("blank", blank)

# drawing a rectangle
# cv.rectangle(theimage, pt1, pt2, color, thickness=none, linetype=None, shift=None)
# img = np.zeros((500, 500, 3), dtype='uint8')
# img[:] = 255, 255, 255
green = 0, 255, 0
black = 0, 0, 0
red = 0, 0, 255
white = 255, 255, 255
# cv.rectangle(img, (0,0), (500,250), green, thickness=2)
# to fill it, use thickness = cv.FILLED or thickness = -1;
# instead of giving the start and the end pos, you can use the width and height
# note: width = img.shape[1], height = img.shape[0]
# cv.rectangle(img, (0, 250), (500, 500), red, thickness=-1)
# cv.rectangle(img, (0, img.shape[0] // 2), red. thickness=cv.FILLED)
# cv.rectangle(img, (0, 0), (500, 250), black, thickness=cv.FILLED)
# cv.imshow("sh", img)

# drawing a circle
# img = np.zeros((500, 500, 3), dtype='uint8')
# cv.circle(img, (250,250), 50, white, thickness=2)
# cv.imshow("img", img)

# drawing a line
# img = np.zeros((500,500, 3), dtype='uint8')
# cv.line(img, (0,0), (500,500), white, thickness=3)
# cv.imshow("img", img)


# how to write text on an image
# cv.putText(img, text, origin, fontface, fontscale, color, thickness=None, lineType = None, bottomLeftOrigin=None)
# img = cv.imread("other_images/family3.jpg")
# # cv.line(img, (80,40),(80,100), red, thickness=2)
# cv.circle(img,(115, 75), 30, red, thickness=2)
# cv.putText(img, "face detected", (115, 30), cv.FONT_HERSHEY_PLAIN, 1.0, red,)
# cv.imshow("img", resfr(img))
# cv.waitKey(0)


# 5 essential functions
# img = cv.imread("other_images/pyth_image.jpg")
# cv.imshow("img", img)

# a. converting an image to grayscale
# seeing the intensity distribution
# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow("im", gray)
# cv.waitKey(0)

# b. bluring  ==> there are many
# removes some of the noise in an image
# blur = cv.GaussianBlur(img, (3,3), cv.BORDER_DEFAULT)
# # to increase the blur, increase the (3,3) say to (7,7) >> it should be od btw
# cv.imshow("blurred", blur)
# cv.waitKey(0)

# c. Edge cascade ==> there are many
# finding the edges that are present int the image
# img = cv.imread("other_images/travel1.jpg")
# canny = cv.Canny(img, 125, 175)
# 125, 175 are threshold values
# cv.imshow("canny edges", canny)
# # to reduce the number of edges use blur as the img parameter
# cv.waitKey(0)

# d. dilating the image
# it takes from the edges
# img = cv.imread("other_images/travel1.jpg")
# canny = cv.Canny(img, 125, 175)
# dilated = cv.dilate(canny, (3,3), iterations=3)
# cv.imshow("dilated", dilated)


# e. Eroding
# a way of erasing the dilated to get back the img
# eroded = cv.erode(dilated, (3,3), iterations=3)
# cv.imshow("eroded", eroded)
# cv.waitKey(0)


# f. resizing
# img = cv.imread("other_images/jonathan-borba-DUrU_bZV8So-unsplash.jpg")
# cv.imshow("hm", img)
# resized = cv.resize(img,(500,500), interpolation=cv.INTER_CUBIC)
# # when trying to enlarge, use cv.INTER_CUBIC OR INTER_LINEAR
# cv.imshow("hum", resized)
# cv.waitKey(0)

# g. cropping
img = cv.imread("other_images/car1.jpg")
cv.imshow("hm", resfr(img))

cropped = resfr(img)[50:200, 200:400]
cv.imshow("cropped", cropped)

cv.waitKey(0)