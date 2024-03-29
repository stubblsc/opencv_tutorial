import cv2
import numpy as np

img = cv2.imread('images/messi5.jpg')
px = img[100,100]
print(px)

# accessing only blue pixel
blue = img[100,100,0]
print(blue)

img[100,100] = [255,255,255]
print img[100,100]

# accessing RED value
img.item(10,10,2)
img.itemset((10,10,2),100)

# modifying RED value
img.itemset((10,10,2),100)
img.item(10,10,2)

print(img.shape)
print(img.size)
print(img.dtype)

ball = img[280:340, 330:390]
img[273:333, 100:160] = ball

b,g,r = cv2.split(img)
img = cv2.merge((b,g,r))
# or
b = img[:,:,0]
img[:,:,2] = 0
