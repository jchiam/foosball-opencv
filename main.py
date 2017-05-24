import lib

IMAGE=''                    # path to image frame
BALL_COLOR_THRESHOLD=200    # reject ball colour value less than __

img = lib.detect_ball(IMAGE, BALL_COLOR_THRESHOLD)
lib.show_image(img, 'detected ball')
