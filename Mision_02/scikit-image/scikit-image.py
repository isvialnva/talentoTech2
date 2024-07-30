import skimage

camera = skimage.data.camera()
print(type(camera))
print(camera.shape)

skimage.io.imshow(camera)
skimage.io.show()
