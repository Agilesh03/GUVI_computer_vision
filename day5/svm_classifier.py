import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets,svm, metrics
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

digits = datasets.load_digits()
x = digits.images
y = digits.target

n_samples = len(x)
X = x.reshape((n_samples, -1))

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, shuffle=False)

clf = svm.SVC(gamma=0.001)
clf.fit(X_train ,y_train)
y_pred = clf.predict(X_test)
print(("classification report:\n", metrics.classification_report(y_test, y_pred)))


images_and_prediction = list(zip(digits.images[n_samples // 2:], y_pred))
for index, (image, prediction) in enumerate(images_and_prediction[:4]):
    plt.subplot(1, 4, index + 1)
    plt.axis("off")
    plt.imshow(image, cmap=plt.cm.gray_r, interpolation="nearest")
    plt.title(f'Pred:{prediction}')

plt.show()