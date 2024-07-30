import skimage

astronaut = skimage.data.astronaut()
print(type(astronaut))
print(astronaut.shape)

skimage.io.imshow(astronaut)
skimage.io.show()
