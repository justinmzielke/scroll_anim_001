from PIL import Image
import os

# Open the first frame
img = Image.open("images_optimized/EarthlyMarkers002_03fusionrender0175.jpg")

# Resize to small placeholder (25% size)
new_size = (int(img.width * 0.25), int(img.height * 0.25))
img_small = img.resize(new_size, Image.Resampling.LANCZOS)

# Save as placeholder.jpg with quality 55
img_small.save("placeholder.jpg", quality=55)

print(f"Created placeholder.jpg: {os.path.getsize('placeholder.jpg')} bytes")
