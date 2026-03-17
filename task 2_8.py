import cv2

image = cv2.imread('image.png')
image_copy = image.copy()

# Draw something (reuse what you did before)
cv2.circle(image_copy, (100, 100), 50, (0, 0, 255), 3)

# Save image
cv2.imwrite('output.png', image_copy)

# Display (optional but recommended)
cv2.imshow('Saved Image', image_copy)

cv2.waitKey(0)
cv2.destroyAllWindows()