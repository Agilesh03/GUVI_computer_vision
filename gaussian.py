import cv2
import matplotlib.pyplot as plt

# viewing or reading the image
img = cv2.imread("shiva.jpg")

gaussian = cv2.GaussianBlur(img, (15, 15), 5)
plt.imshow(cv2.cvtColor(gaussian,cv2.COLOR_BGR2RGB))
plt.axis("off")
plt.show()