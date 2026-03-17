import cv2

image = cv2.imread('image.png')

# Crop region (you can tweak these numbers)
cropped = image[50:300, 100:400]

cv2.imshow('Original Image', image)
cv2.imshow('Cropped Image', cropped)

cv2.waitKey(0)
cv2.destroyAllWindows()