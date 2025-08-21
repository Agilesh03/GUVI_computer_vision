import cv2
import matplotlib.pyplot as plt

img = cv2.imread("shiva.jpg")

_, thresh = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
plt.imshow(thresh, cmap="gray")

plt.axis("off")
plt.show()