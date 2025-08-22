import cv2
import matplotlib.pyplot as plt

img = cv2.imread("images.jpeg")
grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

sift = cv2.SIFT_create()

keypoints, descriptors = sift.detectAndCompute(grayscale, None)

sift_img = cv2.drawKeypoints(grayscale, keypoints, None, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

plt.imshow(sift_img, cmap="gray")
plt.axis("off")
plt.show()
