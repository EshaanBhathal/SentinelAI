import cv2 as cv
from camera import Camera
from ultralytics import YOLO

CAMERA_URL = "rtsp://admin:Bhathal@7@10.0.0.252:554/cam/realmonitor?channel=1>&subtype=0"
# CAMERA_URL = 0    # For testing


def main():
    
    # Creates an object for the camera
    video = Camera(CAMERA_URL, 1920, 1080)

    model = YOLO('yolov8n.pt')


    # loop through frames
    while True:

        isCaptured, frame = video.read()
        if not isCaptured:
            break
        video.addText("Press 'q' to Exit", (20,70), 2, (255,255,255), 6)

        tracking = model.track(frame, persist=True, conf=0.5)[0]

        # looping through all tracks
        for box in tracking.boxes:

            # Only tracking humans
            if box.id is None or int(box.cls.item()) != 0:
                break



            # printing the boxes
            track_id = int(box.id.item()) 
            conf = float(box.conf.item())
            cls = int(box.cls.item())
            box = [int(x) for x in box.xyxy[0]]


            # Drawing the tracking boxes
            cv.rectangle(frame, (box[0], box[1]), (box[2], box[3]), (255, 0, 0), 2)
            cv.putText(frame, f' ID: {track_id}, {conf:.2f}% {model.names[int(cls)]}', (box[0], box[1]-10),cv.FONT_HERSHEY_SIMPLEX, 2, (255, 0, 0), 3, cv.LINE_AA)

        frame_ = tracking.plot()

        cv.imshow('frame', frame)

        if cv.waitKey(20) & 0xFF==ord('q'): # if q pressed, break loop                                                      # Why I need to spam q?
            video.cleanup()
            break;



if __name__ == "__main__":
    main()