import cv2
import matplotlib.pyplot as plt

# reading the image
img = cv2.imread("shiva.jpg")

# convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# detect edges
edges = cv2.Canny(gray, 100, 300)

# display edges
plt.imshow(edges, cmap="gray")
plt.axis("off")
plt.show()
