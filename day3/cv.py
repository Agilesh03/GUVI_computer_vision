import cv2
import matplotlib.pyplot as plt

# viewing or reading the image
img = cv2.imread("image.jpg")

#displaying the image
image = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
plt.imshow(image)
plt.axis("off")

#saving the image
cv2.imwrite("output.jpg",img)

plt.show()