import matplotlib.pyplot as plt
import cv2

# file paths for all images
image_paths = [
    'C:\\Users\\USER\\PycharmProjects\\Assignment3\\image1\\50.png',
    'C:\\Users\\USER\\PycharmProjects\\Assignment3\\image1\\8.png',
    'C:\\Users\\USER\\PycharmProjects\\Assignment3\\image1\\95.png',
    'C:\\Users\\USER\\PycharmProjects\\Assignment3\\image1\\57.png'
]
# file paths for seg
mask_paths = [
    'C:\\Users\\USER\\PycharmProjects\\Assignment3\\mask\\50_seg.png',
    'C:\\Users\\USER\\PycharmProjects\\Assignment3\\mask\\8_seg.png',
    'C:\\Users\\USER\\PycharmProjects\\Assignment3\\mask\\95_seg.png',
    'C:\\Users\\USER\\PycharmProjects\\Assignment3\\mask\\57_seg.png'
]
# file paths for meta
metadata_paths = [
    'C:\\Users\\USER\\PycharmProjects\\Assignment3\\meta\\50.meta',
    'C:\\Users\\USER\\PycharmProjects\\Assignment3\\meta\\8.meta',
    'C:\\Users\\USER\\PycharmProjects\\Assignment3\\meta\\95.meta',
    'C:\\Users\\USER\\PycharmProjects\\Assignment3\\meta\\57.meta'
]
# Function to extract "Subject disorder status" from metadata file
def extract_subject_status(meta_file):
    with open(meta_file, 'r') as file:
        for line in file:
            if line.startswith("Subject disorder status"):
                return line.split(":")[1].strip()  # Get status after ":"
            elif "Subject disorder status" in line:
                return line.split(":", 1)[1].strip()  # Get status after first ":"
    return "Status not found"  # Default status if not found

# Function to overlay image with mask and display
def overlay_and_display(image_path, mask_path):
    image = cv2.imread(image_path)
    mask = cv2.imread(mask_path)

    # Apply a mask overlay on the image
    overlay = cv2.addWeighted(image, 0.7, mask, 0.3, 0)

    return overlay

# Create subplots to display images with masks and metadata
fig, axes = plt.subplots(2, 2, figsize=(12, 12))

for i, (image_path, mask_path, meta_path) in enumerate(zip(image_paths, mask_paths, metadata_paths)):
    # Load and display image with mask
    overlay_image = overlay_and_display(image_path, mask_path)

    # Extract "Subject disorder status" from metadata
    subject_status = extract_subject_status(meta_path)

    # Display the overlaid image with metadata as the title
    ax = axes[i // 2, i % 2]
    ax.imshow(cv2.cvtColor(overlay_image, cv2.COLOR_BGR2RGB))
    ax.set_title(subject_status)
    ax.axis('off')

plt.tight_layout()
plt.show()
