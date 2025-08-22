import cv2
import matplotlib.pyplot as plt

img = cv2.imread("images.jpeg")

cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

blurred = cv2.GaussianBlur(img,(5,5),3)

plt.imshow(blurred)

plt.show()