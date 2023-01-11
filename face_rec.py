import cv2
import numpy as np

# Load the cascade classifier
face_cascade = cv2.CascadeClassifier('face.xml')

# Create a dictionary to store the images and names
images = {'bill.jpg':'Name1',
          'face2.jpg':'Name2',
          'face3.jpg':'Name3',
          # Add more images as necessary
         }

# Get the webcam
cap = cv2.VideoCapture(0)

while True:
    # Read a frame from the webcam
    ret, frame = cap.read()

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the frame
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    # Draw a rectangle around each face
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]

        # Initialize the matching result and name
        match_val = 0
        match_name = None

        # Compare the face to each image in the dictionary
        for image_name, image_label in images.items():
            face_to_compare = cv2.imread(image_name, 0)

            # Compare the face to the current image
            res = cv2.matchTemplate(roi_gray, face_to_compare, cv2.TM_CCOEFF_NORMED)
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

            # Update the match if necessary
            if max_val > match_val:
                match_val = max_val
                match_name = image_label

        # Draw the name of the matching image
        if match_name is not None:
            cv2.putText(frame, match_name, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Show the frame
    cv2.imshow('Webcam', frame)

    # Exit the loop if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close the window
cap.release()
cv2.destroyAllWindows()
