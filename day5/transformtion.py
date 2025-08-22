import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("images.jpeg")
rows, cols = img.shape[:2]

M_translate = np.float32([[1, 0, 50], [0, 1, 100]])  
translated = cv2.warpAffine(img, M_translate, (cols, rows))


scaled = cv2.resize(img, None, fx=1.5, fy=1.5) 

M_rotate = cv2.getRotationMatrix2D((cols/2, rows/2), 45, 1) 
rotated = cv2.warpAffine(img, M_rotate, (cols, rows))
plt.subplot(2, 2, 1)
plt.title("Original")
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.axis("off")

plt.subplot(2, 2, 2)
plt.title("Translated")
plt.imshow(cv2.cvtColor(translated, cv2.COLOR_BGR2RGB))
plt.axis("off")

plt.subplot(2, 2, 3)
plt.title("Scaled")
plt.imshow(cv2.cvtColor(scaled, cv2.COLOR_BGR2RGB))
plt.axis("off")

plt.subplot(2, 2, 4)
plt.title("Rotated")
plt.imshow(cv2.cvtColor(rotated, cv2.COLOR_BGR2RGB))
plt.axis("off")

plt.show()
