import cv2
import matplotlib.pyplot as plt

img = cv2.imread("images.jpeg")
grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

plt.subplot(1, 2, 1)
plt.title("Grayscale Image")
plt.imshow(grayscale, cmap="gray")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.title("Histogram")
plt.hist(grayscale.ravel(), bins=256, range=[0,256])
plt.xlabel("Pixel Intensity")
plt.ylabel("Frequency")

plt.show()
