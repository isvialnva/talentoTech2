import skimage

image_path = 'Lobo.jpeg'
image = skimage.io.imread(image_path)
image_rotate = skimage.transform.rotate(image, angle=90)
image_smoothed = skimage.filters.gaussian(image, sigma=2)

skimage.io.imshow(image_rotate)
skimage.io.imshow(image_smoothed)

skimage.io.show()
