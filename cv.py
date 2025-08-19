import cv2
import matplotlib.pyplot as plt


# viewing or reading the image
img = cv2.imread("image.jpg")

#displaying the image
image = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
plt.imshow(image)
plt.axis("off")


#resizing the image
resized = cv2.resize(img,(200,200))
plt.imshow(cv2.cvtColor(resized,cv2.COLOR_BGR2RGB))

#cropping the image
cropped = img[50:250, 100:400]
print("cropped image" , cropped.shape)

#color the picture into gray
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
plt.imshow(gray, cmap="gray")

# blurring the image
blurred = cv2.blur(img,(15,15))
plt.subplot(3, 5, 1)
plt.imshow(cv2.cvtColor(blurred,cv2.COLOR_BGR2RGB))

# edges the images
gray = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
edges = cv2.Canny(gray,100,300)
plt.imshow(cv2.cvtColor(edges,cv2.COLOR_BGR2RGB))

# gaussian the image
gaussian = cv2.GaussianBlur(img, (15, 15), 5)
plt.imshow(cv2.cvtColor(gaussian,cv2.COLOR_BGR2RGB))
plt.axis("off")

# histogram
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
plt.hist(gray.ravel(),256,[0,256])
plt.xlabel("Pixel Intensity (0-255)")
plt.ylabel("Number of Pixels")

# threshold
_, thresh = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
plt.imshow(thresh, cmap="gray")

plt.show()

#saving the image
cv2.imwrite("output.jpg",img)