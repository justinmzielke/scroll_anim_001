from PIL import Image
import base64
from io import BytesIO

# Open first frame
img = Image.open('images_optimized/EarthlyMarkers002_03fusionrender0175.jpg')

# Create low-quality version (very small, 10% size, quality 15)
img_small = img.resize((int(img.width * 0.1), int(img.height * 0.1)), Image.Resampling.LANCZOS)

# Save as JPEG with very low quality
buffer = BytesIO()
img_small.save(buffer, format='JPEG', quality=15)
buffer.seek(0)

# Convert to base64
base64_str = base64.b64encode(buffer.read()).decode()
print(f"data:image/jpeg;base64,{base64_str}")
