import os
import cv2
import shutil

# Path to YOLOv7 detection script
DETECT_SCRIPT = 'yolov7-master/detect.py'

# Path to YOLOv7 model weights
MODEL_WEIGHTS = 'yolov7-master/models/Clean-Dirty.pt'

# Confidence threshold for object detection
CONF_THRESHOLD = 0.3

# Interval (in seconds) between frame captures
FRAME_INTERVAL = 10

# Input video file
VIDEO_FILE = 'E:/major project/clean-dirty/yolov7-master/data/images/videoplayback.mp4'

# Output directory for detection results
OUT_DIR = 'detection-Out'

# Create output directory if it doesn't exist
if not os.path.exists(OUT_DIR):
    os.makedirs(OUT_DIR)

# Open video file
cap = cv2.VideoCapture(VIDEO_FILE)

# Get video dimensions
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Initialize frame counter
frame_num = 0

# Loop over frames
while True:
    # Read next frame
    ret, frame = cap.read()
    
    # Break loop if end of video file is reached
    if not ret:
        break
    
    # Increment frame counter
    frame_num += 1
    
    # Check if it's time to capture a new frame
    if frame_num % int(FRAME_INTERVAL * cap.get(cv2.CAP_PROP_FPS)) == 0:
        # Generate filename for output image
        out_file = os.path.join(OUT_DIR, f'frame{frame_num:04d}.jpg')
        
        # Save current frame as JPEG image
        cv2.imwrite(out_file, frame, [cv2.IMWRITE_JPEG_QUALITY, 100])
        
        # Run YOLOv7 object detection on saved image
        os.system(f'python {DETECT_SCRIPT} --weights {MODEL_WEIGHTS} --img {width} --conf {CONF_THRESHOLD} --source {out_file} --save-txt')
        
        # Copy detection output image to output directory
        for file in os.listdir('yolov7-master/runs/detect'):
            if file.endswith('.jpg') or file.endswith('.png'):
                shutil.copy(os.path.join('yolov7-master/runs/detect', file), OUT_DIR)
        
        # Remove detection output directory
        shutil.rmtree('yolov7-master/runs/detect')

# Release video file
cap.release()
