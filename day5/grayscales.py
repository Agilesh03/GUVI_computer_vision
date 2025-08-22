import cv2
import matplotlib.pyplot as plt

img = cv2.imread("images.jpeg")
grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

plt.imshow(grayscale, cmap="gray")
plt.axis("off")
plt.show()
