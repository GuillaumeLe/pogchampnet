import cv2
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from PIL import Image

images = []
vidcap = cv2.VideoCapture('video.mp4')
success,image = vidcap.read()

count = 0
success = True
print('Extraying video')
while success:
  if count%10 == 0:
    image = cv2.resize(image, (384, 216)) 
    images.append(image)
    cv2.imwrite("samples/frame%d.jpg" % count, image)
    print(count)     # save frame as JPEG file

  success,image = vidcap.read()
  count += 1
print('video sample size', len(images))