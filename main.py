import cv2 as cv
from ultralytics import YOLO

from camera import Camera
from person import Person
from message import Message

RECIPIENTS = ["eshaan.cs.test@gmail.com"]
CAMERA_URL = "rtsp://admin:Bhathal@7@10.0.0.252:554/cam/realmonitor?channel=2>&subtype=0"
#CAMERA_URL = 0    # For testing



def main():
    
    # Creates objects
    video = Camera(CAMERA_URL, 1290, 720)
    model = YOLO('yolov8n.pt')
    # model.to('cuda') # If you want to use the GPU
    print(model.device)
    email = Message("eshaan.cs.test@gmail.com", "lnqt sqdg tiln aeov")
    i = 1

    # loop through frames
    while True:
        i += 1

        # Read the frame
        isCaptured, frame = video.read()
        ogFrame = frame.copy()
        if not isCaptured:
            break
        video.addText("Press 'q' to Exit", (20,70), 2, (255,255,255), 6)

        if (i % 4 != 0):
            continue

        # Track objects on the frame
        tracking = model.track(frame, persist=True, conf=0.5, classes=[0])[0]

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

            # Drawing the tracking boxes
            person.displayBox(frame, model, video.frameWidth, video.frameHeight)

            # Creating an image of the person and sending an email
            if (person.getFrameNumber() == 10):
                photo = video.createScreenshotPerson(ogFrame, person)
                email.sendEmail(RECIPIENTS, photo, person.getTrackId(), person.getConfidence())


            person.increaseFrames()


        # Display the frame
        cv.namedWindow('frame', cv.WINDOW_NORMAL)
        cv.setWindowProperty('frame', cv.WND_PROP_FULLSCREEN, cv.WINDOW_FULLSCREEN)
        cv.imshow('frame', frame)

        # Exiting the program when 'q' pressed
        if cv.waitKey(20) & 0xFF==ord('q'):
            break;

    video.cleanup()
    print("\n -------- The Program Has Terminated -------- \n")


if __name__ == "__main__":
    main()