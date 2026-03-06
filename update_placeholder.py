from PIL import Image
import base64
from io import BytesIO

# Open first frame
img = Image.open('images_optimized/EarthlyMarkers002_03fusionrender0175.jpg')

# Create low-quality version (small and compressed)
img_small = img.resize((int(img.width * 0.1), int(img.height * 0.1)), Image.Resampling.LANCZOS)

# Save as JPEG with very low quality
buffer = BytesIO()
img_small.save(buffer, format='JPEG', quality=15)
buffer.seek(0)

# Convert to base64
base64_str = base64.b64encode(buffer.read()).decode()

# Read the HTML file
with open('scrollviewer.html', 'r') as f:
    html = f.read()

# Replace the src with complete base64
new_html = html.replace(
    '<img id="frame" src="data:image/jpeg;base64,',
    f'<img id="frame" src="data:image/jpeg;base64,{base64_str}\n<!--'
).replace(
    ' style="display: block;">',
    '--> <img id="frame2" style="display: block;">'
)

# Actually, let's do this properly - just update the src
placeholder_url = f"data:image/jpeg;base64,{base64_str}"
new_html = html.split('<img id="frame" src="')[0] + f'<img id="frame" src="{placeholder_url}" style="display: block;">' + '</div>' + html.split('</div>')[2]

with open('scrollviewer.html', 'w') as f:
    f.write(new_html)

print("Updated scrollviewer.html with complete base64 image")
