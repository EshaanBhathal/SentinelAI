import cv2 as cv
from camera import Camera

CAMERA_URL = "rtsp://admin:Bhathal@7@10.0.0.252:554/cam/realmonitor?channel=2>&subtype=0"


def main():
    
    # Creates an object for the camera
    video = Camera(CAMERA_URL, 1920, 1080)
    print(video)
    
    # loop through frames
    while True:
        isCaptured, frame = video.read()
        video.addText("Press 'q' to Exit", (20,70), 2, (255,255,255), 6)

        cv.imshow('frame', frame)

        if cv.waitKey(20) & 0xFF==ord('q'): # if q pressed, break loop
            video.cleanup()
            break;



if __name__ == "__main__":
    main()