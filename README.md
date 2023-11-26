# Face Recognition System

## Overview

The Face Recognition System is a project that leverages facial recognition techniques to identify and label faces in a live video stream. The system is capable of detecting faces in real-time and, when a match is found, labeling them as a known person. This project serves as a demonstration of the fundamental functionalities of face recognition technology.

## Features

- **Live Video Feed:** Accesses the live video stream from the webcam, providing a continuous feed of captured frames.
- **Face Detection:** Utilizes the face_recognition library to identify face locations within each frame, drawing rectangles around the detected faces.
- **Face Recognition and Labeling:** Compares detected faces with a pre-loaded image of a known person. If a match is found, labels the face as the "Known Person" and draws a green rectangle.
- **Real-time Display:** Displays the processed video feed with labeled faces and rectangles in real-time.
- **User Interaction:** Continues running until the user presses the 'q' key, closing the video feed window and terminating the program.

```python
import cv2
import face_recognition

known_person_image = face_recognition.load_image_file("C:\\Users\\96650\\OneDrive\\Desktop\\webtask\\.vscode\\person.jpg")
known_person_encoding = face_recognition.face_encodings(known_person_image)[0]

video_capture = cv2.VideoCapture(0) 

while True:
    ret, frame = video_capture.read()

    face_locations = face_recognition.face_locations(frame)
    face_encodings = face_recognition.face_encodings(frame, face_locations)

    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        matches = face_recognition.compare_faces([known_person_encoding], face_encoding)
        name = "Unknown"

        if matches[0]:
            name = "Known Person"

        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 0.5, (255, 255, 255), 1)

    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()
