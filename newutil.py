
import cv2
import numpy as np
import random

# Initialize a list to store circle locations
circle_locations = []

def detect_and_draw_circles(image):
    # Convert the image to HSV color space
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Define the lower and upper bounds for red in HSV
    lower_red = np.array([0, 100, 100])
    upper_red = np.array([10, 255, 255])

    # Create a mask for red color
    mask = cv2.inRange(hsv, lower_red, upper_red)

    # Find contours in the mask
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Find the largest red circle
    largest_circle = None
    max_radius = 0
    for contour in contours:
        (x, y), radius = cv2.minEnclosingCircle(contour)
        if radius > max_radius:
            max_radius = radius
            largest_circle = contour

    # Draw the largest red circle
    if largest_circle is not None:
        cv2.drawContours(image, [largest_circle], -1, (0, 0, 255), 2)

        # Generate random circles within the largest red circle
        for _ in range(20):  # Draw a random number of circles (1 to 5)
            rand_x = random.randint(int(x - max_radius), int(x + max_radius))
            rand_y = random.randint(int(y - max_radius), int(y + max_radius))
            while not cv2.pointPolygonTest(largest_circle, (rand_x, rand_y), False) >= 0:
                rand_x = random.randint(int(x - max_radius), int(x + max_radius))
                rand_y = random.randint(int(y - max_radius), int(y + max_radius))
            radius = 2
            cv2.circle(image, (rand_x, rand_y), radius, (0, 255, 0), 2)  # Draw a green circle

            # Save the circle location
            circle_locations.append((rand_x, rand_y, radius))

# Function to check if a point is inside a circle
def is_point_inside_circle(point, circle):
    center, radius = circle
    return (point[0] - center[0]) ** 2 + (point[1] - center[1]) ** 2 <= radius ** 2

# Mouse callback function
def on_mouse_click(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        for i, circle in enumerate(circle_locations):
            if is_point_inside_circle((x, y), ((circle[0], circle[1]), circle[2])):
                del circle_locations[i]
                break

# Read the image
image = cv2.imread('captured_image.jpg')

# Create a window and set the mouse callback function
cv2.namedWindow('Image with Random Circles in Largest Red Circle')
cv2.setMouseCallback('Image with Random Circles in Largest Red Circle', on_mouse_click)

while True:
    # Clone the original image to keep the original for every run
    image_copy = image.copy()
    circle_locations = []

    # Run the detection function
    detect_and_draw_circles(image_copy)

    # Display the image with circles drawn in the red circle
    cv2.imshow('Image with Random Circles in Largest Red Circle', image_copy)

    key = cv2.waitKey(0) & 0xFF
    if key == ord('s'):  # Press 'q' to quit the program
        #cv2.imwrite('analysed_captured_image.jpg', image_copy)
        final = cv2.imread("captured_image.jpg")
        finalimage = final.copy()
        for i in circle_locations:
            outputimage = cv2.circle(finalimage, (i[0], i[1]), 2, (0, 255, 0), 2)
        cv2.imwrite("analysed_captured_image.jpg", outputimage)
        break

# Print circle locations found
print("Circle Locations:")
for i, (x, y, radius) in enumerate(circle_locations, 1):
    print(f"Circle {i}: Center at ({x}, {y}), Radius: {radius}")
print("---"*10)
print("circle shit : " + str(circle_locations))
addlocations = open("newlocation.txt", "w")
for i in circle_locations:
    addlocations.write(str(i[0]) +" "+ str(i[1]) + "\n")
addlocations.close()

cv2.destroyAllWindows()