import os
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# Define your image directory
image_dir = r"C:\\Users\chris\Documents\Callan_Puzzle\Nebula_Eye"  # Modify this path to your images
# Get the list of images in the directory
images = [f for f in os.listdir(image_dir) if f.endswith(('.png', '.JPG', '.jpeg'))]

# Load the first image
if images:
    image_path = os.path.join(image_dir, images[0])
    img = mpimg.imread(image_path)
    
    # Display the image
    plt.imshow(img)
    plt.axis('off')  # Hide the axes for a cleaner display
    plt.show()
else:
    print("No images found in the directory")
