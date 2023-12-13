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

# Load the known person image and encoding
known_person_image_path = r"C:\Users\96650\OneDrive\Desktop\webtask\idk.jpg"
known_person_image = face_recognition.load_image_file(known_person_image_path)
# Check if there are faces in the image before attempting to get encodings
face_locations = face_recognition.face_locations(known_person_image)
if face_locations:
    known_person_encoding = face_recognition.face_encodings(known_person_image)[0]
else:
    print("No faces found in the known person image.")
    # You might want to handle this case, e.g., by selecting a different image.
    exit()
# Choose the path to the uploaded viedo file 
video_path = r"C:\Users\96650\OneDrive\Desktop\webtask\la.mp4"
# Open the video file
video_capture = cv2.VideoCapture(video_path)
frame_number = 0
known_person_count = 0
unknown_person_count = 0
speed_factor = 2  # Increase the speed by a factor of 2

while True:
    ret, frame = video_capture.read()

    if not ret:
        # Break the loop if the video is finished
        break

    face_locations = face_recognition.face_locations(frame)
    face_encodings = face_recognition.face_encodings(frame, face_locations)

    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        matches = face_recognition.compare_faces([known_person_encoding], face_encoding)
        name = "Unknown"

        if matches and matches[0]:
            name = "Known Person"
            known_person_count += 1
        else:
            unknown_person_count += 1

        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 0.5, (255, 255, 255), 1)

    # Display frame number, recognized names, and counts
    cv2.putText(frame, f"Frame: {frame_number}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
    cv2.putText(frame, f"Known Persons: {known_person_count}", (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)  # Red color
    cv2.putText(frame, f"Unknown Persons: {unknown_person_count}", (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)  # Red color

    cv2.imshow('Video', frame)

    if cv2.waitKey(int(25 / speed_factor)) & 0xFF == ord('q'):
        break

    frame_number += 1

# Release the video capture object and close all windows
video_capture.release()
cv2.destroyAllWindows()
