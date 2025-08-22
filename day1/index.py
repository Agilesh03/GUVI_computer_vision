import cv2
import matplotlib.pyplot as plt

img = cv2.imread("images.jpeg")

cv2.rectangle(img,(30,30),(100,100),(255,0,0),2)

plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))
plt.axis("off")
plt.imsave("output.jpeg",img)
cropped = img[50:550 , 100:400]
print("cropped image", cropped.shape)
plt.show()