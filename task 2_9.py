import cv2

img1 = cv2.imread('image.png')
img2 = cv2.imread('image2.png')

if img1 is None or img2 is None:
    print("Error: One of the images was not found.")
    exit()

img2_resized = cv2.resize(img2, (img1.shape[1], img1.shape[0]))

added = cv2.add(img1, img2_resized)
subtracted = cv2.subtract(img1, img2_resized)

cv2.imshow('Added Image', added)
cv2.imshow('Subtracted Image', subtracted)

cv2.waitKey(0)
cv2.destroyAllWindows()