# Stylized QR Code Generator

A Python project for creating beautiful, customizable QR codes with various shapes, colors, and center images while maintaining scannability.

## Features

- **Multiple Module Shapes**: Square, Diamond, Rounded corners, Hexagon
- **Custom Colors**: Set different colors for data modules and finder patterns
- **Center Images**: Add logos or images to the center of QR codes
- **High Quality**: Maintains image quality and QR code scannability
- **Easy to Use**: Simple API with sensible defaults

## Installation

1. Clone this repository:
```bash
git clone https://github.com/Vania-Dev/qr-generator.git
cd qr-generator
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Quick Start

```python
from qr_generator import StylizedQRGenerator

# Create generator instance
generator = StylizedQRGenerator()

# Generate a basic QR code
generator.generate_qr("https://example.com", output_path="my_qr.png")

# Generate a stylized QR code with diamond shapes
generator.generate_qr(
    data="https://example.com",
    fill_color='#1E3A8A',           # Blue diamonds
    finder_color='#DC2626',         # Red corner squares
    back_color='white',             # White background
    center_image="logo.png",        # Your logo
    module_shape='diamond',         # Diamond-shaped modules
    output_path="stylized_qr.png"
)
```

## Module Shapes

### Square (Default)
Standard QR code modules - reliable and widely compatible.

### Diamond
Rotated squares that create an elegant diamond pattern while maintaining scannability.

### Rounded
Squares with rounded corners for a softer, modern appearance.

### Hexagon
Regular hexagons that create a unique honeycomb pattern.

## API Reference

### `generate_qr(data, **options)`

Generate a QR code with custom styling.

**Parameters:**
- `data` (str): The data to encode (URL, text, etc.)
- `fill_color` (str, optional): Color for data modules. Default: 'black'
- `back_color` (str, optional): Background color. Default: 'white'
- `center_image` (str, optional): Path to center image file
- `output_path` (str, optional): Output file path. Default: 'qr_code.png'
- `module_shape` (str, optional): Shape of modules ('square', 'diamond', 'rounded', 'hexagon'). Default: 'square'
- `finder_color` (str, optional): Color for corner finder patterns. Default: same as fill_color

**Returns:**
- `str`: Path to the generated QR code image

## Examples

### Basic QR Code
```python
generator.generate_qr("https://example.com")
```

### Colored QR Code
```python
generator.generate_qr(
    "https://example.com",
    fill_color='#FF6B6B',
    back_color='#4ECDC4'
)
```

### QR Code with Logo
```python
generator.generate_qr(
    "https://example.com",
    center_image="logo.png",
    output_path="branded_qr.png"
)
```

### Diamond QR Code
```python
generator.generate_qr(
    "https://example.com",
    module_shape='diamond',
    fill_color='#1E3A8A',
    finder_color='#DC2626'
)
```

### Hexagon QR Code
```python
generator.generate_qr(
    "https://example.com",
    module_shape='hexagon',
    fill_color='#059669',
    back_color='#F0F9FF'
)
```

## Color Formats

Colors can be specified in several formats:
- Hex codes: `#FF6B6B`, `#1E3A8A`
- Color names: `red`, `blue`, `white`, `black`
- RGB tuples: `(255, 107, 107)`

## Center Image Guidelines

For best results with center images:
- Use square images (1:1 aspect ratio)
- Recommended size: 200x200 pixels or larger
- Supported formats: PNG, JPG, JPEG, GIF
- Images are automatically resized to 1/5 of QR code size
- A white circular background is added for better contrast

## Technical Details

### QR Code Structure
- **Finder Patterns**: The three corner squares that help scanners locate the code
- **Data Modules**: The individual squares that encode the actual data
- **Quiet Zone**: The white border around the QR code

### Customization Areas
- Data modules can use any of the four available shapes
- Finder patterns are always drawn as rounded rectangles for optimal scanning
- Colors can be set independently for data modules and finder patterns

### Quality Considerations
- All shapes are designed to maintain QR code scannability
- Center images are limited to 1/5 of total size to preserve data integrity
- High-quality image resampling preserves visual clarity

## Dependencies

- `qrcode[pil]`: QR code generation
- `Pillow`: Image processing and drawing

## File Structure

```
qr-generator/
├── qr_generator.py      # Main QR generator class
├── requirements.txt     # Python dependencies
├── README.md           # This file
└── images/             # Directory for center images (optional)
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is open source. Feel free to use and modify as needed.

## Troubleshooting

### QR Code Not Scanning
- Ensure sufficient contrast between fill_color and back_color
- Avoid center images larger than recommended size
- Test with multiple QR code readers

### Image Quality Issues
- Use high-resolution center images
- Ensure center images are square for best results
- Check that image files exist and are accessible

### Color Issues
- Verify color format (hex codes should start with #)
- Ensure sufficient contrast for scanning
- Test colors with actual QR code readers

## Examples Gallery

The generator can create various styles:
- Corporate QR codes with company logos
- Event QR codes with custom branding
- Social media QR codes with profile images
- Product QR codes with brand colors
- Creative QR codes with unique shapes

For more examples and advanced usage, see the example code in `qr_generator.py`.

Craft it with the kind of ❤️ that leaves fingerprints on the soul.