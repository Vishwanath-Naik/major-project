import os
from detectionAPI import detection
from detectionAPI import detect_from_video

# Set the path to the folder which contains all the images
PATH=r'yolov7-master\data\images'
count=0
for file in os.listdir(PATH):
    value=detection(PATH,file)
    if(str(value)=="True"):
        count=count+1
    print(file+": "+str(value)) # prints True or False in the Terminal 
print("Total number of images containing garbage bins: "+str(count))

