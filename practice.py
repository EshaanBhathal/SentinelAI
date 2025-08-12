import cv2 as cv
import numpy as np

frameWidth = 910
frameHeight = 540

def resolutionChange(capture, width, height):
    capture.set(3, width)
    capture.set(4, height)


def main():

    # capture = cv.VideoCapture(0) # references web cam
    # resolutionChange(capture, frameWidth, frameHeight)

    # while True: # runs video frame by frame
    #     isCaptured, frame = capture.read()
    #     cv.imshow('Video', frame) # displays frames

    #     if cv.waitKey(20) & 0xFF==ord('q'): # if q pressed, break loop
    #         break

    # # cleanup
    # capture.release()
    # cv.destroyAllWindows()

    drawScreen = np.zeros((frameHeight, frameWidth, 3), dtype='uint8')
    drawScreen[:] = 0,255,0
    cv.rectangle(drawScreen, (0,0), (100,100), (255,0,0), 2)
    cv.imshow('drawing', drawScreen)


    cv.waitKey(0)




if __name__ == "__main__":
    main()