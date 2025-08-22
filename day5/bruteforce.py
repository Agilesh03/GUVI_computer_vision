import cv2
import matplotlib.pyplot as plt

img1 = cv2.imread("images.jpeg", cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread("images.jpeg", cv2.IMREAD_GRAYSCALE)

sift = cv2.SIFT_create()
kp1, des1 = sift.detectAndCompute(img1, None)
kp2, des2 = sift.detectAndCompute(img2, None)

bf = cv2.BFMatcher()

matches = bf.knnMatch(des1, des2, k=2)


good_matches = []
for m, n in matches:
    if m.distance < 0.75 * n.distance:
        good_matches.append([m])

match_img = cv2.drawMatchesKnn(img1, kp1, img2, kp2, good_matches, None, flags=2)

plt.imshow(match_img)
plt.axis("off")
plt.show()
