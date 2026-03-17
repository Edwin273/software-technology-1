import cv2
image = cv2.imread('image.png')
resized_img = cv2.resize(image, (400, 300))
cv2.imshow('Resized Image', resized_img)
cv2.waitKey(0)
cv2.destroyAllWindows()