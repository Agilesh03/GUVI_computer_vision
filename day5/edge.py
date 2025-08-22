import cv2
import matplotlib.pyplot as plt

img = cv2.imread("images.jpeg")

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

edges = cv2.Canny(gray,100,100)

plt.imshow(edges)

plt.show()