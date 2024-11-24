import cv2
import numpy as np

# Specifying upper and lower ranges of color to detect in hsv format
lower = np.array([0, 0, 0])
upper = np.array([250, 255, 30]) # (These ranges will detect Yellow)

# Capturing webcam footage
webcam_video = cv2.VideoCapture(0)
width = 640
height = 480
webcam_video.set(cv2.CAP_PROP_FRAME_WIDTH, width)
webcam_video.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
x1, y1, w1, h1 = 200, 100, 230, 254

while True:
    success, frame = webcam_video.read() # Reading webcam footage
    if not success:
        print("Error: Couldn't grab frame. Exiting.")
        break
    video = frame[y1:y1+h1, x1:x1+w1]

    img = cv2.cvtColor(video, cv2.COLOR_BGR2HSV) # Converting BGR image to HSV format

    mask = cv2.inRange(img, lower, upper) # Masking the image to find our color

    mask_contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) # Finding contours in mask image

    # Finding position of all contours
    if len(mask_contours) != 0:
        for mask_contour in mask_contours:
            if cv2.contourArea(mask_contour) > 500:
                x, y, w, h = cv2.boundingRect(mask_contour)
                cv2.rectangle(video, (x, y), (x + w, y + h), (0, 0, 255), 3) #drawing rectangle
                cv2.circle(video, (x + int(w/2), y + int(h/2)), int(h/2), (0, 0, 255), 3)

    cv2.imshow("mask image", mask) # Displaying mask image

    cv2.imshow("window", video) # Displaying webcam image

    key = cv2.waitKey(1)
    if key == ord('s'):
        cv2.imwrite('captured_image.jpg', video)
        print("x axis min : " + str(x))
        print("x axis max : " + str(x+w))
        print("y axis min : " + str(y))
        print("y axis max : " + str(y+h))
        location = []
        location.append(x)
        location.append(x+w)
        location.append(y)
        location.append(y+h)
        print(location)
        addlocation = open("location.txt", "w")
        addlocation.write(str(location))
        addlocation.close()
        break
    if key == ord("q"):
        break

webcam_video.release()
cv2.destroyAllWindows()
