# game.py
import cv2
import numpy as np
import directkeys

# Define the region of interest (ROI) for steering wheel detection
roi_x = 100
roi_y = 100
roi_width = 200
roi_height = 200

# Initialize the camera
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if not ret:
        break

    # Crop the frame to the ROI
    roi = frame[roi_y:roi_y+roi_height, roi_x:roi_x+roi_width]

    # Convert the ROI to grayscale
    gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)

    # Apply thresholding to detect the steering direction
    _, thresh = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)

    # Calculate the sum of pixel values in the left and right halves
    left_sum = np.sum(thresh[:, :roi_width // 2])
    right_sum = np.sum(thresh[:, roi_width // 2:])

    # Determine the direction based on pixel sums
    if left_sum > right_sum:
        directkeys.press_key('A')  # Press 'A' to move left
    else:
        directkeys.release_key('A')  # Release 'A'
    
    # Display the frame
    cv2.imshow('Steering Detection', frame)

    # Exit the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close all windows
cap.release()
cv2.destroyAllWindows()