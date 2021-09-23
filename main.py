import cv2
import numpy as np

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

while True:

    # images taken from the camera. Saves to "frame".
    ret, frame = cap.read()

    # to make a mirror effect.
    frame = cv2.flip(frame, 1)

    # converted from BGR to HSV format.
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # the lower and upper borders of the red color in hsv format.
    # if you want the other colors, you should change the values (bottom values).
    lower_red = np.array([161,155,84])
    upper_red = np.array([179,255,255])

    # color masking.
    red_mask = cv2.inRange(hsv_frame, lower_red, upper_red)

    # it is used to print the images taken from the camera to the screen.
    cv2.imshow("Camera", frame)
    # masked camera image.
    cv2.imshow("Mask Camera", red_mask)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()