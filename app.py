import subprocess
import sys

def firststep():
    #find head
    #pythonfilepath = "main.py"
    subprocess.run([sys.executable, "main.py"])

def secondstep():
    #find dots
    #pythonfilepath = "newutil.py"
    subprocess.run([sys.executable, "newutil.py"])

def thirdstep():
    #navigate to dots
    #pythonfilepath = "arduino try pygame.py"
    subprocess.run([sys.executable, "arduino try pygame.py"])

def fourthstep():
    #capture image and loop
    #pythonfilepath = "prototype.py"
    subprocess.run([sys.executable, "prototype.py"])

firststep()
secondstep()
thirdstep()
#fourthstep()

#pythonfilepath = "main.py"
#subprocess.run([sys.executable, pythonfilepath])