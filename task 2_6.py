import cv2

image = cv2.imread('image.png')
image_copy = image.copy()

# Draw rectangle (top-left corner, bottom-right corner)
cv2.rectangle(image_copy, (50, 50), (300, 250), (0, 255, 0), 3)

cv2.imshow('Image with Rectangle', image_copy)

cv2.waitKey(0)
cv2.destroyAllWindows()