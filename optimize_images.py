import os
from PIL import Image
import sys

# Directories
source_dir = r"Z:\scroll_animation\images"
output_dir = r"Z:\scroll_animation\images_optimized"

# Settings
max_width = 1920
quality = 85  # JPEG quality

# Get all PNG files and sort them
files = sorted([f for f in os.listdir(source_dir) if f.endswith('.png')])
total = len(files)

print(f"Processing {total} images...")
print(f"Resizing to max width: {max_width}px")
print(f"Output quality: {quality}")
print()

for i, filename in enumerate(files, 1):
    try:
        # Open image
        img_path = os.path.join(source_dir, filename)
        img = Image.open(img_path)
        
        # Convert RGBA to RGB if necessary
        if img.mode == 'RGBA':
            rgb_img = Image.new('RGB', img.size, (255, 255, 255))
            rgb_img.paste(img, mask=img.split()[3])
            img = rgb_img
        
        # Calculate new dimensions (maintain aspect ratio)
        if img.width > max_width:
            ratio = max_width / img.width
            new_height = int(img.height * ratio)
            img = img.resize((max_width, new_height), Image.Resampling.LANCZOS)
        
        # Save as JPEG
        output_filename = filename.replace('.png', '.jpg')
        output_path = os.path.join(output_dir, output_filename)
        img.save(output_path, 'JPEG', quality=quality, optimize=True)
        
        # Print progress
        if i % 10 == 0 or i == total:
            print(f"[{i}/{total}] {output_filename}")
    
    except Exception as e:
        print(f"Error processing {filename}: {e}")

print()
print(f"✓ Done! {total} images converted to {output_dir}")
