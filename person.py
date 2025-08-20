import cv2 as cv

class Person:

    people_ids = []
    people_objects = []


    def __init__(self, track_id):
        self.track_id = track_id
        Person.people_ids.append(track_id)
        Person.people_objects.append(self)
        self.frames = 1


    def __str__(self):
        return f"Person has track ID: {self.track_id}"
    

    def setInfo(self, conf, cls, box):
        self.conf = conf
        self.cls = cls
        self.box = box


    def increaseFrames(self):
        self.frames += 1


    def displayBox(self, frame, model, width, height):
         # Drawing the tracking boxes
        fontScale = ((self.box[2] - self.box[0]) / width) * 5

        cv.rectangle(frame, (self.box[0], self.box[1]), (self.box[2], self.box[3]), (255, 0, 0), 2)
        cv.putText(frame, f' ID: {self.track_id}, {self.conf:.2f}% {model.names[int(self.cls)]}', (self.box[0], self.box[1]-10),cv.FONT_HERSHEY_SIMPLEX, fontScale, (255, 0, 0), 3, cv.LINE_AA)


    def getTrackID(self):
        return self.track_id
    
    
    def getConfidence(self):
        return self.conf
    

    def getPosition(self):
        return self.box
    

    def getFrameNumber(self):
        return self.frames
