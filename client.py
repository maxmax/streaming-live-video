import cv2
import numpy as np
import socket
import struct
from io import BytesIO
import imutils
import numpy as np
# import argparse

# initialize the list of class labels MobileNet SSD was trained to
# detect, then generate a set of bounding box colors for each class
# CLASSES = ["background", "aeroplane", "bicycle", "bird", "boat",
#	"bottle", "bus", "car", "cat", "chair", "cow", "diningtable",
#	"dog", "horse", "motorbike", "person", "pottedplant", "sheep",
#	"sofa", "train", "tvmonitor"]
# COLORS = np.random.uniform(0, 255, size=(len(CLASSES), 3))

# Capture frame
cap = cv2.VideoCapture(0)

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 8080))

while cap.isOpened():
    _, frame = cap.read()
    # Resize video
    frame = imutils.resize(frame, width=400)

    # Since we will need width and height a little later, we will get them now
    (h, w) = frame.shape[:2]
    # print("[INFO] h...", h)
    # print("[INFO] h...", w)

    # Detected ....

    memfile = BytesIO()
    np.save(memfile, frame)
    memfile.seek(0)
    data = memfile.read()

    # Send form byte array: frame size + frame content
    client_socket.sendall(struct.pack("L", len(data)) + data)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
