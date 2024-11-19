import cv2
import os

# Load the image
image_path = r"C:\\Users\chris\Documents\Callan_Puzzle\Samples\small.jpg"
image = cv2.imread(image_path)

# Define grid positions for each piece (assuming uniform grid and sizes)
# These values need to be measured and adjusted based on the exact grid lines
piece_positions = {
    "A1": (600, 1450, 1038, 1800),  # (x1, y1, x2, y2) example values
    "A2": (1100, 1440, 1420, 1856),
    "A3": (1490, 1434, 1910, 1868),
    "B1": (590, 1862, 1000, 2300),
    "B2": (1050, 1866, 1420, 2300),
    "B3": (1480, 1880, 1905, 2300),
}

# Directory to save the cropped pieces
output_dir = 'cropped_pieces'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Loop through the defined positions and crop each piece
for label, (x1, y1, x2, y2) in piece_positions.items():
    cropped_piece = image[y1:y2, x1:x2]  # Crop the image
    output_path = os.path.join(output_dir, f'{label}.jpg')
    cv2.imwrite(output_path, cropped_piece)  # Save the cropped piece
    print(f'Saved {label} at {output_path}')
