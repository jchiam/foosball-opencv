import sys
import cv2
import numpy as np

def detect_ball(file, ball_color_threshold):
    # image read in grayscale and size scaled to 1/4
    img = cv2.imread(file, cv2.IMREAD_REDUCED_GRAYSCALE_4)
    img = cv2.medianBlur(img, 5)

    # create base image for display
    cimg = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)

    # detect circles
    circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1, 100, param1=50, param2=30, minRadius=0, maxRadius=20)
    if circles is None:
        print 'No circles detected...'
        return nil

    # mark each circle and reject invalid circles by colour
    num_circles = 0
    circles = np.uint16(np.around(circles))
    for i in circles[0,:]:
        # reject circles of invalid colours
        if img[i[1], i[0]] < ball_color_threshold:
            continue
        # draw the outer circle
        cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
        # draw the center of the circle
        cv2.circle(cimg,(i[0],i[1]),2,(0,255,255),3)
        numCircles += 1

    if num_circles == 0:
        print 'No acceptable circles...'
        return nil

    return cimg

def show_image(img, title=''):
    cv2.imshow('detected ball', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
