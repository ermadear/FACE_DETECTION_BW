import cv2

# Load the cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# To capture video from webcam.
cap = cv2.VideoCapture(0)

while True:

    # Read the frame
    _, img = cap.read()

    # Convert into grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 5)

    # Draw rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(gray, (x, y), (x+w, y+h), (0, 0, 0), 2)

    # Display the output
    cv2.imshow('Detektsi Wajah', gray)

    # Stop if escape key is pressed
    k = cv2.waitKey(30)
    if k==27:
        break

# Release the VideoCapture object
cap.release()
