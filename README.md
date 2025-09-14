# Smart Security Camera with YOLOv8 + Email Alerts

A real-time human detection and alerting system built with OpenCV, YOLOv8, and Yagmail.  
The system monitors a live camera feed, tracks people, and sends an email with a screenshot when a person is detected for a certain number of frames.

------------------------------------------------------------
Features
------------------------------------------------------------
- Camera Integration:
  - Stream video via RTSP URL or use a local webcam.
  - Adjustable resolution.
- YOLOv8 Object Detection:
  - Tracks humans in real-time.
  - Bounding boxes drawn around detected people.
- Person Tracking:
  - Assigns unique IDs to each detected person.
  - Counts frames to prevent false positives.
- Screenshot Capture:
  - Crops and saves the detected person’s image.
  - Cleans up old photos automatically.
- Email Notifications:
  - Sends an email with the cropped image of the detected person.
  - Includes ID and confidence score in the message.

------------------------------------------------------------
Project Structure
------------------------------------------------------------
.
├── camera.py       # Handles video capture, text overlay, cleanup, screenshots
├── person.py       # Person tracking logic (IDs, confidence, bounding boxes)
├── message.py      # Email alert system using Yagmail
├── main.py         # Entry point: combines camera, YOLO, and alert system
├── peoplePhotos/   # Temporary folder for cropped screenshots
└── README.md       # Documentation

------------------------------------------------------------
Requirements
------------------------------------------------------------
- Python 3.8+
- Packages:
  - opencv-python
  - ultralytics
  - yagmail
- YOLOv8 model file (e.g., yolov8n.pt)
- Gmail account with App Passwords enabled

------------------------------------------------------------
Configuration
------------------------------------------------------------
- In main.py, update:
  RECIPIENTS = ["your_email@example.com"]
  CAMERA_URL = "rtsp://username:password@ip_address:554/..."
- In message.py, provide your Gmail and app password:
  Message("your_email@gmail.com", "your_app_password")

------------------------------------------------------------
How to Run
------------------------------------------------------------
1. Install dependencies:
   pip install opencv-python ultralytics yagmail
2. Run the program:
   python main.py
3. Controls:
   q = quit program
   (emails are sent automatically when a person is detected)

------------------------------------------------------------
Author
------------------------------------------------------------
Developed by Eshaan Bhathal as a computer vision and security automation project.
