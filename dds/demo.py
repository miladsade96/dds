"""
    Yolov5 First Test
"""

import yolov5

# Instantiating and loading pre-trained model
model = yolov5.load("models/yolov5s.pt")

# Path to test image
path = "images/Drone.jpeg"

# inference process
results = model(path)

# Displaying the results
results.show()
