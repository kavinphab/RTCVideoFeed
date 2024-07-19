# process_rtc_video.py
import cv2
from pathlib import Path

def process_video_feed():
    cap = cv2.VideoCapture(0)  # connect to camera

    if not cap.isOpened():
        print("Error: Could not open video feed.")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame")
            break

        # Example processing: convert to grayscale
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Display the resulting frame
        cv2.imshow('Gray Video Feed', gray_frame)

        # press q to break
        if cv2.waitKey(1) == ord('q'):
            break

    cap.release() #disconnect from camera
    cv2.destroyAllWindows()

if __name__ == "__main__":
    process_video_feed()
