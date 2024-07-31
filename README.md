----------------------------------------------------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------------------------------------------------
Aim : 

-) create a software which is able to count the number of hair in an image

-) Create a hardware which can scan and capture an image of the entire surface of a person’s head for the software to analyze

-) Mimic and automate the process of trichoscopy

----------------------------------------------------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------------------------------------------------
How to use : 
1. intall opencv on IDE or computer      (https://www.youtube.com/watch?v=T5BVLQG3Pxk)
2. manually change the name of the image you want to image process by opening the script
3. run the program in terminal      (https://www.youtube.com/watch?v=enfCPH_2k6A)

----------------------------------------------------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------------------------------------------------
Description : 

image processing software that uses opencv to detect and count the number of hairs in an image

----------------------------------------------------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------------------------------------------------
Process and refleciton (report) : 

In order to complete the first objective which is the software, I have to learn how to use image processing. I decided to use opencv as it works well with python and also it is a widely used extension due to its accurate readings and giant database which is useful for machine learning, image processing and object detection.

I learnt how to use opencv by following the official documentation of opencv and techwithtim tutorial series on opencv. After understanding the fundamentals, I had to choose which approach I was going to use to do the image processing. I could either count the number of lines within the image or count the number of endpoints of lines in the image. I initially decided to go with the first one. It seemed like a more straightforward approach and there are more resources related to it. Opencv has a function called houghlines which basically detects objects that have similar shapes to a line. However, when I ran the program through different images, it was not able to give me an accurate reading. After reviewing the process image, I presumed the reason behind the error was due to the overlapping of lines which made it difficult for the program to differentiate which ones have already been counted. 

During that time, I couldn't find a solution so I decided to take a different approach, which was to count the number of endpoints in an image. But due to the lack of resources online and my lack of understanding of opencv, I decided to learn more about it.

While reading the documentation laterwards, I discovered the solution to my initial overlapping lines problem. For houghlines function, opencv allows the user to input and change the parameters such as the threshold detection sensitivity and minimum line gap value in order to have the program be adapted to analyze different types of images. By changing the parameters manually, I was able to get a result that was incredibly close to its actual value, making the program highly accurate.

Unfortunately, this raised an issue, which was that in order to analyze an image, the function’s parameters have to be manipulated manually every single time through trial and error, which makes it inconvenient and I wanted to find a way to automate this task and collect an accurate reading every time without changing the values manually. Then I realized, this issue can be tackled with ease, and that is to run the image through many different variants of the program, similar to the analogy below.

Finally, I ended up with the source code below. To summarize what it does, it takes in an image of choosing and it gets analyzed and the number of hair is counted many times by many different variants of Houghlines function, meaning Houghlines function with different ranges of parameter values. Once the image processing is complete, it appends all the final results collected by all the different variants of the Houghlines function into a list. The median and the distribution of the data is displayed as the output through use of import statistics and import matplotlib.

----------------------------------------------------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------------------------------------------------
After completing the hair counting program, the following step was to work on a hardware that can minimic and automate the trichoscopy procedure. I was inspired by stuff made here, a content creator who made a robot that could cut hair for him. I decided to use his design as a foundation for my hardware’s prototype. After some adjusting, I landed on a design above.
Essentially, the hardware had to have x y z axis mobility for the arm holding the dermatoscope in order to examine all parts of the head. Furthermore, the dermatoscope has to be able to rotate 90 degree horizontally and vertically in order for the dermatoscope to be able to be placed and fit onto the surface of the head to get a clearer image of the scalp since the closer the microscope is to the scalp, the less likely confounding variables such as long hair blocking the camera from will interrupt process. Additionally, the hardware has to have the ability to locate common balding areas and scan that area from top to bottom automatically, allowing the images to be processed by the program written. To summarize : 

1. Hardware can move up, down, left, right, front left
2. Dematoscope can rotate 90 degrees both horizontally and vertically
3. Additional software allowing hardware to locate area to examine and move the dermatoscope accordingly

I decided to separate the hardware into 3 separate components shown above. For component 1, I decided to utilize and purchase a linear actuator with x y z axis mobility. It will be connected to an arduino which is a microcontroller, a compact integrated circuit designed to govern a specific operation in an embedded system. I chose to use this over a raspberry pi as the linear actuator requires 4 stepper motor, which an arduino works better with. I bought a linear actuator on taobao that had a traveling distance of 300 mm, 300 mm, 150 mm respectively. However, when it first arrived, the 3d printed collar collapsed on itself during delivery, therefore it had to be shipped back to the producer for fixing. So during that time, I decided to write the program beforehand (component 3) so everything will be prepared once the linear actuator has been fixed.

For component 3, the objective is to give the microcontroller the ability to scan the layout of the user’s head, once it has, it will pinpoint common balding parts on the scanned image and send a command to the linear actuator to have the dermatoscope to navigate towards the pinpointed location without hurting or bumping into user’s head. I used the same programming language I used for the software part of the project python to make them more compatible. 

First step is to understand what I am trying to locate. There are different stages to balding. However, most balding begins at the frontal and temple area then the crown area of the head. Therefore the machine will mainly try to locate these 3 areas. Once the software has located the area, that area will be outlined, then the dermatoscope will navigate towards that area and start capturing images, after each image capture, it will be displaced around 3 cm to the right until the row of that area has been thoroughly scanned, then the dermatoscope will move around 3 cm downwards and repeat the process until that entire area has been examined. The images will be stored in a file that will be run through the image processing software.

The program first imports opencv in order to give python image processing abilities. Then, it processes the live video frame by frame using the while loop. 
For each frame, each pixel has a rgb value associated, which gives it its color. In order for the python program to process and understand values, it has to be converted to hsv values, which is how python reads and understands color binarily. Then the pixels are filtered out using the InRange() function. Essentially, it scans each pixel and sees whether it is within range of hsv values (lower_black and upper_black). If not, the pixel is removed leaving a frame with only pixels that are black in color. It then colors the pixels within range to make it more distinct during the output process. I struggled to find the correct parameters for the hsv value range for color black. Luckily, I found "Detecting Colour in an Image using OpenCv and Python" who provided the hsv values for all the colors in the color wheel.
----------------------------------------------------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------------------------------------------------
