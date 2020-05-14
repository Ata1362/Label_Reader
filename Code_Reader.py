import cv2 as cv
import pyzbar.pyzbar as pbar

def findbarcode(im):
    decodeimage = pbar.decode(im)
    for i in decodeimage:
        x = i.rect.left
        y = i.rect.top
        w = i.rect.width
        h = i.rect.height
    return(x, y, w, h)


cam = cv.VideoCapture(0)


while True:
    ret, frame = cam.read()
    if ret:
        x, y, w, h = findbarcode(frame)
        cv.rectangle(frame, (x, y), (x + w, y + h), (100, 200, 0), 2)
        cv.imshow("Live", frame)

    if cv.waitKey(20) & 0xFF == ord("q"):
        break

cam.release()
cv.destroyAllWindows()


