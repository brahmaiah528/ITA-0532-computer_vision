import cv2

# Read image
image = cv2.imread(r"C:\Users\brami\OneDrive\Desktop\shiva.jpg")

# Check image loaded or not
if image is None:
    print("Image not found")
else:
    # Show original image
    cv2.imshow("Original", image)
    cv2.waitKey(0)

    # Convert to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Show grayscale image
    cv2.imshow("Grayscale", gray_image)
    cv2.waitKey(0)

    cv2.destroyAllWindows()