import cv2
import matplotlib.pyplot as plt

img = cv2.imread("shiva.jpg")

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
plt.hist(gray.ravel(),256,[0,256])
plt.xlabel("Pixel Intensity (0-255)")
plt.ylabel("Number of Pixels")

plt.axis("off")
plt.show()