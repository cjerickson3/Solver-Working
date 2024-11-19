import sys
puzzle_dir = r"C:\\Users\chris\Documents\Callan_Puzzle\Solver\src"
sys.path.append(puzzle_dir)
from Puzzle.Puzzle import Puzzle
import matplotlib.pyplot as plt
import os

# New function to load images from a directory (based on grid system)
def load_puzzle_images(image_dir):
    images = []
    for filename in sorted(os.listdir(image_dir)):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            image_path = os.path.join(image_dir, filename)
            images.append(image_path)
    return images

# Function to run puzzle-solving logic
def solve_puzzle(image_dir, green_screen=False):
    # Load images (pieces and partial assemblies)
    puzzle_images = load_puzzle_images(image_dir)
    
    # Iterate over the images and process them
    for img_path in puzzle_images:
        print(f"Processing {img_path}")
        # Here we would invoke the Puzzle class with the image
        Puzzle(img_path, green_screen=green_screen)

# Define the image directory
image_dir = r"C:\\Users\chris\Documents\Callan_Puzzle\Nebula_Eye"  # Modify this path to your images

# Call the solve function
solve_puzzle(image_dir)
