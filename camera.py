
import cv2 as cv
import os

def resolutionChange(capture, width, height):
    capture.set(3, width)
    capture.set(4, height)

class Camera:

    def __init__(self, url, width, height):
        self.url = url
        self.frameWidth = width
        self.frameHeight = height

        self.capture = cv.VideoCapture(self.url)
        resolutionChange(self.capture, self.frameWidth, self.frameHeight)


    def __str__(self):
        return f"Camera URL is :{self.url}"
    

    def read(self):
        scene = self.capture.read()
        self.frame = scene[1]
        return scene
    
    def addText(self, text, BLPoint, size, colour, thickness):
        cv.putText(self.frame, text, BLPoint, cv.FONT_HERSHEY_SIMPLEX, size, colour, thickness, cv.LINE_AA, False)


    def cleanup(self):
        self.capture.release()
        cv.destroyAllWindows()
        print("\n -------- The Video Stopped Playing -------- \n")

        # Remove all photos created
        if not os.path.isdir("peoplePhotos/"):
            print(f"Error: Directory 'peoplePhotos/' does not exist or is not a directory.")
            return
    
        for filename in os.listdir("peoplePhotos/"):
            path = os.path.join("peoplePhotos/", filename)
            if os.path.isfile(path):
                try:
                    os.remove(path)
                    print(f"file {path} was deleted")
                except:
                    print("error")


    def createScreenshotPerson(self, frame, person):
        x1,y1,x2,y2 = person.getPosition()
        cropped = frame[y1:y2, x1:x2]
        addr = f"peoplePhotos/Person{person.getTrackID()}.jpg"
        cv.imwrite(addr, cropped)
        return addr
        

