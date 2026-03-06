# Scroll Animation Viewer

A minimalist scroll-controlled image sequence viewer with momentum physics.

## Features

- **Smooth scrolling**: Scroll to advance through a 100-frame image sequence
- **Momentum physics**: Scrolling applies exponential decay momentum for fluid animation trails
- **Vertical orientation**: Fixed 1080x1920 viewport (portrait mode)
- **No UI chrome**: Clean, minimal design—just the images and scroll interaction
- **Optimized images**: 100 JPEG frames (~30MB total) for fast loading

## How It Works

`embed.html` - The main viewer
- Loads and preloads all 100 optimized image frames
- Responds to scroll input with physics-based momentum
- Fixed viewport ensures consistent display across devices

`images_optimized/` - Image sequence directory
- 100 frames (EarthlyMarkers002_03fusionrender0175.jpg → 0274.jpg)
- Pre-optimized JPEGs at ~300KB per image
- RGBA converted to RGB (white background)

## Usage

### Standalone
Open `embed.html` in a browser. Scroll to animate the image sequence.

### Embed in Website (iframe)
```html
<iframe 
  src="https://cdn.jsdelivr.net/gh/yourusername/scroll_animation@main/embed.html" 
  width="1080" 
  height="1920" 
  style="border: none;">
</iframe>
```

Or use raw GitHub URL:
```html
<iframe 
  src="https://raw.githubusercontent.com/yourusername/scroll_animation/main/embed.html" 
  width="1080" 
  height="1920" 
  style="border: none;">
</iframe>
```

## Physics Parameters

Adjust these in `embed.html` to customize behavior:
- **Momentum decay**: `velocity *= 0.85` (higher = longer trails, lower = quicker stop)
- **Frame rate**: `FRAME_INTERVAL = 1000/12` (currently 12fps)
- **Scroll sensitivity**: `scrollAccumulator * 0.6` (higher = more responsive)

## Files

- `embed.html` - Production viewer (no UI elements)
- `scroll-viewer.html` - Development version (includes frame counter)
- `optimize_images.py` - Python script for batch converting image sequences
- `test.html` - Diagnostic page for image loading verification
