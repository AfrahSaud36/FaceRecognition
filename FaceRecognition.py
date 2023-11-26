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
