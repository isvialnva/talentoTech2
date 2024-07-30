import cv2
import numpy as np

# image = cv2.imread('Lobo.jpeg')
image = cv2.imread('Lobo.jpeg', cv2.IMREAD_GRAYSCALE)
height, width = image.shape[:2]

center = (width/2, height/2)
tx, ty = 100, 50
M = np.float32([[1, 0, tx], [0, 1, ty]])
kernel = np.array([[-1, -1, -1],
                   [-1,  9, -1],
                   [-1, -1, -1]])

sobelx = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=5)
sobely = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=5)

edges = cv2.magnitude(sobelx, sobely)


# angle = 45
# M = cv2.getRotationMatrix2D(center, angle, 1.0)

rotate = cv2.warpAffine(image, M, (width, height))
translated = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
sharpened = cv2.filter2D(image, -1, kernel)
edges = cv2.normalize(edges, None, 0, 255, cv2.NORM_MINMAX, dtype=cv2.CV_8U)

cv2.imshow('Imagen', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
