import requests
url="https://127.0.0.1:5000/"

# Set path of individual file
#PATH=r'detection-Out/sample1.jpeg'
PATH=r'clean-dirty/yolov7-master/data/images/videoplayback.mp4'
data={'Path':PATH}
print("SENDING DATA...")    
requests.post(url,json=data)
print("Successfull!")