import cv2

image = cv2.imread('image.png')
image_copy = image.copy()

# Draw a line
cv2.line(image_copy, (0, 0), (300, 300), (255, 0, 0), 3)

# Add text
cv2.putText(
    image_copy,
    'Shrimp',
    (50, 50),
    cv2.FONT_HERSHEY_SIMPLEX,
    1,
    (0, 255, 255),
    2
)

cv2.imshow('Image with Line and Text', image_copy)

cv2.waitKey(0)
cv2.destroyAllWindows()