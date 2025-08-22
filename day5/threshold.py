import cv2
import matplotlib.pyplot as plt

img = cv2.imread("images.jpeg")
grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

_, binary = cv2.threshold(grayscale, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

plt.subplot(1, 2, 1)
plt.title("Grayscale")
plt.imshow(grayscale, cmap="gray")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.title("Binary (Otsu)")
plt.imshow(binary, cmap="gray")
plt.axis("off")

plt.show()
