'''import cv2
import random
import numpy as np

cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)  # convert to hsv color grading
    # lower_blue = np.array([90, 50, 50]) #hsv color input in brackets
    # upper_blue = np.array([130, 255, 255]) #only show blue shit , go to hsv color picker to get right color sequences
    lower_blue = np.array([0, 0, 0])
    upper_blue = np.array([250, 255, 30])

    mask = cv2.inRange(hsv, lower_blue,
                       upper_blue)  # everything in this range will show but everything will be deleted ?
    # a mask tells u which pt of image u should keep
    result = cv2.bitwise_and(frame, frame, mask=mask)  # use mask in this code to combine it with other image wtf ?
    # look it up to understand it more

    #my own shit to cotour imaeg im cooked :(


    cv2.imshow("frame", result)  # show color
    cv2.imshow("mask", mask)  # show black and white, show 0 and 1

    if cv2.waitKey(1) == ord("q"):
        green = np.uint8([[[0, 0, 0]]])
        hsv_green = cv2.cvtColor(green, cv2.COLOR_BGR2HSV)
        print(hsv_green)
        break

cap.release()
cap.destroyAllWindows()
'''

'''
import cv2          #import opencv, image processing module
import numpy as np
cap = cv2.VideoCapture(1)           #access and use webcam video

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
'''

'''chat gpt code
import cv2
import numpy as np

# Initialize the video capture object
cap = cv2.VideoCapture(1)

while True:
    ret, frame = cap.read()

    if not ret:
        print("Error: Couldn't grab frame. Exiting.")
        break

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Threshold the image to find black objects
    _, thresholded = cv2.threshold(gray, 30, 255, cv2.THRESH_BINARY)

    # Find contours of black objects
    contours, _ = cv2.findContours(thresholded, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Draw a circle around each black object
    for contour in contours:
        (x, y, w, h) = cv2.boundingRect(contour)
        if cv2.contourArea(contour) > 100:  # Filter small objects
            cv2.circle(frame, (x + w // 2, y + h // 2), max(w, h) // 2, (0, 0, 255), 2)

    cv2.imshow('Black Objects Detection', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the VideoCapture and destroy any OpenCV windows
cap.release()
cv2.destroyAllWindows()'''

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
