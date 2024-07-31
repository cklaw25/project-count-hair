import cv2          #import opencv, image processing module
import numpy as np
cap = cv2.VideoCapture(0)           #access and use webcam video

while True:
    _, frame = cap.read()           #store video as a variable for easier processing
    blurred_frame = cv2.GaussianBlur(frame, (5, 5), 0)          #highly effective in removing Gaussian noise from an image, while keeping edges intact
    hsv = cv2.cvtColor(blurred_frame, cv2.COLOR_BGR2HSV)            #convert bgr to hsv values

    lower_black = np.array([0, 0, 0])            #black hsv value
    upper_black = np.array([250, 255, 30])      #upper black hsv value (brighter black)
    mask = cv2.inRange(hsv, lower_black, upper_black)           #find pixels that hav hsv values within this color range

    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)          #use processed image to find outlines of objects

    for contour in contours:            #loop through contour drawing process as it is an video and it processes it frame by frame
        cv2.drawContours(frame, contour, -1, (0, 255, 0), 3)            #draw outline (coutour)
        cv2.imshow("Frame", frame)
        #cv2.imshow("Mask", mask)
        key = cv2.waitKey(1)
        if key == ord("q"):
            break

    if cv2.waitKey(1) == ord("w"):
        break

cap.release()
cv2.destroyAllWindows()
