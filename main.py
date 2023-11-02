from ultralytics import YOLO
from PIL import Image

# Define model
model=YOLO('yolov8n.pt')

# object detection on an image
#image1 = Image.open("cats.jpg")
#result = model.predict(source=image1, save=True) # save detected image

# video and webcam object detection
resultWebcam=model.predict(source="0",show=True) # 0 for webcam
#resultVideo=model.predict(source="ExampleVideo.mp4",show=True)