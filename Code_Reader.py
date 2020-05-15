import cv2 as cv
import pyzbar.pyzbar as pyzbar
import numpy as np

cam = cv.VideoCapture(0)

while True:

    ret, frame = cam.read()
    decoded_objects = pyzbar.decode(frame)
    if decoded_objects:  # To check weather any data retrieved or not.
            points = np.array(decoded_objects[0].polygon, np.int32)
            cv.polylines(frame, [points], True, (0, 255, 55), 5)
            cv.putText(frame, str(decoded_objects[0].type) + " " + str(decoded_objects[0].data), (0, 50), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv.LINE_AA)

    cv.imshow("live", frame)
    if cv.waitKey(1) & 0xff == ord("q"):
        break


cam.release()
cv.destroyAllWindows()
