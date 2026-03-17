import cv2

image = cv2.imread('image.png')

print(f"Type of the image: {type(image)}")
print(f"Shape of the image array: {image.shape}")