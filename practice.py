import cv2 as cv
import numpy as np

frameWidth = 910
frameHeight = 540

def resolutionChange(capture, width, height):
    capture.set(3, width)
    capture.set(4, height)


def main():

    img = cv.imread('testPhotos/cat.jpg')
    cv.imshow('Cat', img)

    # # ---- Bitwise Operators ----
    # blank = np.zeros((400, 400), dtype='uint8')
    # rectangle = cv.rectangle(blank.copy(), (30,30), (370,370), 255, -1)
    # circle = cv.circle(blank.copy(), (200,200), 200, 255, -1)

    # cv.imshow('Rectangle', rectangle)
    # cv.imshow('Circle', circle)

    # bitwise_and = cv.bitwise_and(rectangle, circle)
    # cv.imshow('and', bitwise_and)

    # bitwise_or = cv.bitwise_or(rectangle, circle)
    # cv.imshow('or', bitwise_or)

    # bitwise_xor = cv.bitwise_xor(rectangle, circle)
    # cv.imshow('xor', bitwise_xor)

    # bitwise_not = cv.bitwise_not(rectangle)
    # cv.imshow('not square', bitwise_not)





    # # ---- Blurring ----
    # # Done to smooth out an image
    
    # # Method 1 - Averaging (in a kernal of x by y takes the average intensity for middle value)
    # average = cv.blur(img, (3,3))
    # cv.imshow('avgBlur', average)

    # # Method 2 - Guassian blur (takes weight for center, more natural but less blur)
    # gauss = cv.GaussianBlur(img, (7,7), 0)
    # cv.imshow('gaussBlur', gauss)

    # # Method 3 - Median Blur (least blurring, best for small grid kernals, smudge effect for high amount)
    # median = cv.medianBlur(img, 3)
    # cv.imshow('medianBlur', median)

    # # Method 4 - Bilateral (pixels further away influence the blur, smudge effect for high amount)
    # bilateral = cv.bilateralFilter(img, 10, 15, 15)
    # cv.imshow('bilateralBlur', bilateral)





    # # ---- Color Channels ----
    # b,g,r = cv.split(img)

    # blank = np.zeros(img.shape[:2], dtype='uint8')
    # blue = cv.merge([b,blank,blank])
    # green = cv.merge([blank, g, blank])
    # red = cv.merge([blank, blank, r])

    # cv.imshow('Blue', blue)
    # cv.imshow('Green', green)
    # cv.imshow('Red', red)

    # merged = cv.merge([b,g,r])
    # cv.imshow('merged', merged)





    # # ---- Color Spaces ----
    # # helpful for converting colors for other libraries

    # gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    # cv.imshow('Cat_grey', gray)

    # # BGR to HSV
    # hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    # cv.imshow('HSV', hsv)

    # # BGR to L*a*b
    # lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
    # cv.imshow('LAB', lab)

    # # BGR to rgb
    # rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    # cv.imshow('RGB', rgb)





    # # ----- Greyscaling and stuff -----
    # # convert to greyscale
    # gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    # cv.imshow('Cat_grey', gray)

    # # Blur
    # blur = cv.GaussianBlur(img, (9,9), cv.BORDER_DEFAULT)
    # cv.imshow('Cat_blur', blur)

    # # Edge Cascade, combine with blur to reduce line amount
    # canny = cv.Canny(blur, 125, 175)
    # cv.imshow('canny', canny)

    # # Dilating the image, thickens the outline
    # dilated = cv.dilate (canny, (3,3), iterations=1)
    # cv.imshow('dilated', dilated)

    # # Eroding the image, reduces thickness of the outline
    # eroded = cv.erode(dilated, (3,3), iterations=1)
    # cv.imshow('eroded', eroded)

    # # Resize and crop an image, change last parameter if increasing size (google it)
    # resized = cv.resize(img, (500,500), interpolation=cv.INTER_AREA)
    # cv.imshow('resize', resized)

    # # Cropping, array slicing
    # cropped = img[50:200, 200:400]
    # cv.imshow('cropped', cropped)





    # # ---- Image Transformations ----
    # def translate(img, x, y): # -x,-y do left and up
    #     transMat = np.float32([[1,0,x], [0,1,y]])
    #     dimensions = (img.shape[1], img.shape[0])
    #     return cv.warpAffine(img, transMat, dimensions)
    
    # translated = translate(img, -100, 100)
    # cv.imshow('Translated', translated)

    # # rotation, skipped does not look helpful

    # # flipping
    # flip = cv.flip(img, 1) # 0 is x, 1 is y, 2 is both
    # cv.imshow('flip', flip)





    # # ---- Contour Detection ----

    # gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    # cv.imshow('Gray', gray)

    # blank = np.zeros(img.shape, dtype='uint8')
    # cv.imshow('Blank', blank)

    # # Method 1 - this one is better
    # blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)

    # canny = cv.Canny(blur, 125, 175)
    # cv.imshow('Canny', canny)

    



    # # Method 2 - thresh converts into binary (black or white)
    # ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
    # cv.imshow('thresh', thresh)

    # # finding contours
    # contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
    # print (f'{len(contours)} contours found')

    # contours = cv.drawContours(blank, contours, -1, (0,0,255), 1)
    # cv.imshow('contours', contours)





    # #  ---- Video Stuff ----
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

    # drawScreen = np.zeros((frameHeight, frameWidth, 3), dtype='uint8')
    # drawScreen[:] = 0,255,0
    # cv.rectangle(drawScreen, (0,0), (100,100), (255,0,0), 2)
    # cv.imshow('drawing', drawScreen)

    cv.waitKey(0)




if __name__ == "__main__":
    main()