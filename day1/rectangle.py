import cv2
import matplotlib.pyplot as plt

img = cv2.imread("images.jpeg")

rect = cv2.rectangle(img,(30,30),(100,100),(0,255,0),1)

plt.imshow(rect)
plt.show()