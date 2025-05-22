from PIL import Image
import os

# Path to the images folder
image_folder = "/Users/kiahvaidya/Desktop/MemoryGame/images"

# Target size for memory game tiles
target_size = (80, 80)

# Loop through all .jpeg files in the folder
for filename in os.listdir(image_folder):
    if filename.endswith(".jpeg") or filename.endswith(".jpg"):
        # Open image
        img_path = os.path.join(image_folder, filename)
        img = Image.open(img_path)

        # Resize image
        img = img.resize(target_size, Image.LANCZOS)

        # Convert filename to .png
        base_name = os.path.splitext(filename)[0]
        new_filename = base_name + ".png"
        new_path = os.path.join(image_folder, new_filename)

        # Save as .png
        img.save(new_path, "PNG")
        print(f"Converted and resized: {filename} -> {new_filename}")
