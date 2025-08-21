import cv2
import matplotlib.pyplot as plt

img = cv2.imread("shiva.jpg")

blurred = cv2.blur(img,(15,15))
plt.subplot(3, 5, 1)
plt.imshow(cv2.cvtColor(blurred,cv2.COLOR_BGR2RGB))

plt.show()