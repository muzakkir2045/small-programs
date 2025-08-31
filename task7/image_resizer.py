

import os
from PIL import Image

# Configuration
input_folder = "images"         # Folder where your original images are stored
output_folder = "resized"       # Folder where resized images will be saved
new_size = (800, 800)           # Target size (width, height)
output_format = "JPEG"          # Change to "PNG", "WEBP", etc. if needed
quality = 85                    # JPEG/WebP quality (1-100)

# Create output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Supported extensions
valid_extensions = ['.jpg', '.jpeg', '.png', '.webp', '.bmp']

# Resize & convert images
for filename in os.listdir(input_folder):
    ext = os.path.splitext(filename)[1].lower()
    if ext in valid_extensions:
        try:
            with Image.open(os.path.join(input_folder, filename)) as img:
                img = img.convert("RGB")  # Ensure compatibility
                img = img.resize(new_size, Image.LANCZOS)
                output_path = os.path.join(output_folder, os.path.splitext(filename)[0] + '.' + output_format.lower())
                img.save(output_path, output_format, quality=quality)
                print(f"✔ Resized: {filename} → {output_path}")
        except Exception as e:
            print(f" Failed: {filename} → {e}")

print("✅ All images processed.")
