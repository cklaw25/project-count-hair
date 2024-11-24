import cv2
import numpy as np
import statistics
import datetime as dt
import matplotlib.pyplot as plt
#speed increasing code
import numpy as np

data = []
trange = ["50", "55", "60", "65", "70", "75", "80", "85", "90", "95", "100"]
minrange = ["100", "105", "110", "115", "120", "125", "130", "135", "140", "145", "150"]
maxrange = ["10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20"]

#speed increasing code
skip = "\n"
value = 1

def imageprocess(t, min, max):
    global line_count
    image = cv2.imread('picturename.png') #change picture name here
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 50, 150)
    #lines = cv2.HoughLinesP(edges, 1, np.pi / 180, threshold=50, minLineLength=125, maxLineGap=20)
    lines = cv2.HoughLinesP(edges, 1, np.pi / 180, threshold=t, minLineLength=min, maxLineGap=max)

    line_count = 0

    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line[0]
            cv2.line(image, (x1, y1), (x2, y2), (0, 0, 255), 2)
            line_count += 1

    cv2.destroyAllWindows()

    print(f"Number of lines drawn: {line_count}")
    data.append(line_count)

writestuff = open("datainput.txt", "w")
writebackup = open("backup.txt", "w")

for tr in trange:
    for minr in minrange:
        for maxr in maxrange:
            imageprocess(int(tr), int(minr), int(maxr))
            print(tr, minr, maxr)
            #speed increaisng code
            inputlist = [line_count, tr, minr, maxr]
            writestuff.write(str(inputlist))
            writestuff.writelines(skip)
            writebackup.write(str(inputlist))
            writebackup.writelines(skip)

writestuff.write(str(data))
writestuff.close()
writebackup.write(str(data))
writebackup.close()

print(data)
data = [int(i) for i in data]
medianlist = statistics.median(data)
print(medianlist)
n = len(data)
mean = sum(data)/n
#print(mean)

def scatter_plot():
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

myownlist = data
median = medianlist
listfixed = []
def sortgoodstuff():
    global myownlist, median
    #readstuff = open("datainput.txt", "r")
    #readinglines = readstuff.readlines()

    myownlist = [float(ele) for ele in myownlist]
    # printing result
    #print(myownlist)
    #print(myownlist[0] + myownlist[1])
    deletevalue = 0
    myownlist2 = myownlist

    def closest(myownlist, median):
        myownlist = myownlist2
        myownlist = np.asarray(myownlist)
        idx = (np.abs(myownlist - median)).argmin()
        print("idx : " + str(idx+1))
        print("---"*5)
        #print(readinglines[idx])
        print("---" * 5)
        del myownlist2[idx]

        readstuff = open("datainput.txt", "r")
        readinglines = readstuff.readlines()
        print(readinglines[idx])
        listfixed.append(readinglines[idx])
        ptr = 1
        with open("datainput.txt", "w") as fw:
            for line in readinglines:
                if ptr != (idx + 1):
                    # print("hello world")
                    fw.write(line)
                ptr += 1
        fw.close()
        readstuff.close()

        return myownlist[idx]

    for i in range(20):
        print("---" * 5)
        print(closest(myownlist, median))
        print(myownlist)
        print(myownlist2)
        print("---" * 5)


sortgoodstuff()
scatter_plot()
print("fixed list : " + str(listfixed))


#1. detect line endpoint caue deteching lines always have errors especially when overlapping
#2. circle them to see if right or not
#3. count the number of circles ?

print(f"Number of lines drawn: {line_count}")'''


