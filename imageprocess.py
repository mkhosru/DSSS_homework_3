import matplotlib.pyplot as plt
import numpy as np
import cv2

# Load the RGB image
image_path = r'C:\Users\USER\PycharmProjects\Assignment3\image\leaves.jpg'
image = cv2.imread(image_path)
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Convert to grayscale using different methods
def rgb_to_gray_lightness(image):
    gray = np.zeros_like(image)
    gray[:, :, 0] = (np.max(image, axis=2) + np.min(image, axis=2)) / 2
    gray[:, :, 1] = (np.max(image, axis=2) + np.min(image, axis=2)) / 2
    gray[:, :, 2] = (np.max(image, axis=2) + np.min(image, axis=2)) / 2
    return gray

def rgb_to_gray_average(image):
    gray = np.mean(image, axis=2).astype(np.uint8)
    gray = np.stack((gray, gray, gray), axis=-1)
    return gray

def rgb_to_gray_luminosity(image):
    gray = np.zeros_like(image)
    gray[:, :, 0] = 0.21 * image[:, :, 0] + 0.72 * image[:, :, 1] + 0.07 * image[:, :, 2]
    gray[:, :, 1] = 0.21 * image[:, :, 0] + 0.72 * image[:, :, 1] + 0.07 * image[:, :, 2]
    gray[:, :, 2] = 0.21 * image[:, :, 0] + 0.72 * image[:, :, 1] + 0.07 * image[:, :, 2]
    return gray

# Convert the image using different methods
gray_lightness = rgb_to_gray_lightness(image)
gray_average = rgb_to_gray_average(image)
gray_luminosity = rgb_to_gray_luminosity(image)

# Plotting the three variants side by side
fig, axes = plt.subplots(1, 4, figsize=(15, 5))

# Plot the original image
axes[0].imshow(image)
axes[0].set_title('Original Image')
axes[0].axis('off')

# Plot grayscale images using different methods
axes[1].imshow(gray_lightness, cmap='gray')
axes[1].set_title('Lightness Method')
axes[1].axis('off')

axes[2].imshow(gray_average, cmap='gray')
axes[2].set_title('Average Method')
axes[2].axis('off')

axes[3].imshow(gray_luminosity, cmap='gray')
axes[3].set_title('Luminosity Method')
axes[3].axis('off')

plt.tight_layout()
plt.show()
