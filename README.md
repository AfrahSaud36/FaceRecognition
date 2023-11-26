# Face Recognition System

## Overview

The Face Recognition System is a project that leverages facial recognition techniques to identify and label faces in a live video stream. The system is capable of detecting faces in real-time and, when a match is found, labeling them as a known person. This project serves as a demonstration of the fundamental functionalities of face recognition technology.

## Features

- **Live Video Feed:** Accesses the live video stream from the webcam, providing a continuous feed of captured frames.
- **Face Detection:** Utilizes the face_recognition library to identify face locations within each frame, drawing rectangles around the detected faces.
- **Face Recognition and Labeling:** Compares detected faces with a pre-loaded image of a known person. If a match is found, labels the face as the "Known Person" and draws a green rectangle.
- **Real-time Display:** Displays the processed video feed with labeled faces and rectangles in real-time.
- **User Interaction:** Continues running until the user presses the 'q' key, closing the video feed window and terminating the program.
