import cv2
import face_recognition


known_person_image_path = r"C:\Users\96650\OneDrive\Desktop\webtask\idk.jpg"
known_person_image = face_recognition.load_image_file(known_person_image_path)

face_locations = face_recognition.face_locations(known_person_image)
if face_locations:
    known_person_encoding = face_recognition.face_encodings(known_person_image)[0]
else:
    print("No faces found in the known person image.")
    exit()
    
video_path = r"C:\Users\96650\OneDrive\Desktop\webtask\la.mp4"
video_capture = cv2.VideoCapture(video_path)
frame_number = 0
known_person_count = 0
unknown_person_count = 0
speed_factor = 2 

while True:
    ret, frame = video_capture.read()

    if not ret:
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

    # Display frame
    cv2.putText(frame, f"Frame: {frame_number}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
    cv2.putText(frame, f"Known Persons: {known_person_count}", (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)  
    cv2.putText(frame, f"Unknown Persons: {unknown_person_count}", (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2) 

    cv2.imshow('Video', frame)

    if cv2.waitKey(int(25 / speed_factor)) & 0xFF == ord('q'):
        break

    frame_number += 1

video_capture.release()
cv2.destroyAllWindows()
