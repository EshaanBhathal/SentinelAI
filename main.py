import cv2 as cv
from ultralytics import YOLO

from camera import Camera
from person import Person

CAMERA_URL = "rtsp://admin:Bhathal@7@10.0.0.252:554/cam/realmonitor?channel=1>&subtype=0"
#CAMERA_URL = 0    # For testing



def main():
    
    # Creates objects
    video = Camera(CAMERA_URL, 1920, 1080)
    model = YOLO('yolov8n.pt')

    # loop through frames
    while True:

        # Read the frame
        isCaptured, frame = video.read()
        if not isCaptured:
            break
        video.addText("Press 'q' to Exit", (20,70), 2, (255,255,255), 6)

        # Track objects on the frame
        tracking = model.track(frame, persist=True, conf=0.5)[0]

        # looping through all objects
        for box in tracking.boxes:

            # Only tracking humans
            if box.id is None or int(box.cls.item()) != 0:
                break

            track_id = int(box.id.item()) 

            # New person
            if track_id not in Person.people_ids:
                Person(track_id)

            # Finding the person
            person = Person.people_objects[Person.people_ids.index(track_id)]

            # Updating information for the person
            conf = float(box.conf.item())
            cls = int(box.cls.item())
            box = [int(x) for x in box.xyxy[0]]
            person.setInfo(conf, cls, box)
            person.increaseFrames()

            # Drawing the tracking boxes
            person.displayBox(frame, model, video.frameWidth, video.frameHeight)

        # Display the frame
        cv.imshow('frame', frame)

        # Exiting the program when 'q' pressed
        if cv.waitKey(20) & 0xFF==ord('q'):
            break;

    video.cleanup()



if __name__ == "__main__":
    main()