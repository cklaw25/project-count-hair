import cv2          #opencv
import numpy as np
import statistics
import datetime as dt
import matplotlib.pyplot as plt

data = []
trange = ["50", "55", "60", "65", "70", "75", "80", "85", "90", "95", "100"]
minrange = ["100", "105", "110", "115", "120", "125", "130", "135", "140", "145", "150"]
maxrange = ["10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20"]

def imageprocess(t, min, max):
    image = cv2.imread('storage/image u wanna upload')    #input image name here
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)      #grayscale image
    edges = cv2.Canny(gray, 50, 150)        #edge detection
    lines = cv2.HoughLinesP(edges, 1, np.pi / 180, threshold=t, minLineLength=min, maxLineGap=max)      #detecting and rawing lines on image

    line_count = 0

    if lines is not None:       #counting hair by scanning image row by row
        for line in lines:
            x1, y1, x2, y2 = line[0]
            cv2.line(image, (x1, y1), (x2, y2), (0, 0, 255), 2)
            line_count += 1

    #cv2.imshow('Detected Lines', image)        #shows image after being manipulated
    #cv2.waitKey(0)
    cv2.destroyAllWindows()

    print(f"Number of lines drawn: {line_count}")
    data.append(line_count)

for tr in trange:       #creates different variants of the algorithum and repeats image process process multiple times for a large range of data
    for minr in minrange:
        for maxr in maxrange:
            imageprocess(int(tr), int(minr), int(maxr))
            print(tr, minr, maxr)

print(data)
data = [int(i) for i in data]
medianlist = statistics.median(data)
print(medianlist)       #print median value
n = len(data)
mean = sum(data)/n
#print(mean)

def scatter_plot():     #show data distribution by plotting graph using all the data collected
    i = int(len(data))
    inputs = data
    inputs2 = []
    for x in range(i):
        inputs2.append(1)
    title = "title"
    xlabel = "x"
    ylabel = "y"

    x = np.array(inputs)
    y = np.array(inputs2)

    plt.scatter(x, y)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()

scatter_plot()