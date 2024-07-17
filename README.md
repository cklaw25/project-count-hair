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
