# ⚡ Stylized QR Code Generator

[![Contributors](https://img.shields.io/github/contributors/Vania-Dev/qr-generator?style=for-the-badge&logo=github&label=Contributors&labelColor=101010)](https://github.com/Vania-Dev/qr-generator/graphs/contributors)
[![Forks](https://img.shields.io/github/forks/Vania-Dev/qr-generator?style=for-the-badge&logo=github&label=Forks&labelColor=101010)](https://github.com/Vania-Dev/qr-generator/forks)
[![Stars](https://img.shields.io/github/stars/Vania-Dev/qr-generator?style=for-the-badge&logo=github&labelColor=101010)](https://github.com/Vania-Dev/qr-generator/stargazers)
[![Issues](https://img.shields.io/github/issues/Vania-Dev/qr-generator?style=for-the-badge&logo=github&label=Issues&labelColor=101010)](https://github.com/Vania-Dev/qr-generator/issues)
[![License](https://img.shields.io/github/license/Vania-Dev/qr-generator?style=for-the-badge&logo=open-source-initiative&labelColor=101010)](https://github.com/Vania-Dev/qr-generator/blob/main/LICENSE.txt)

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/Vania-Dev">
    <img src="images/vaniadev.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Create your own QR Code</h3>

  <a href="https://www.youtube.com/@vaniadev">
    <img src="images/video.png" alt="Logo" style="height: 60%; width:60%;">
  </a>

  <p align="center">
    <br />
    <br />
    <a href="https://github.com/Vania-Dev/qr-generator">Aditional material</a>
    ·
    <a href="https://github.com/Vania-Dev/qr-generator/issues/new?labels=bug&template=bug-report---.md">Report an Error</a>
    ·
    <a href="https://github.com/Vania-Dev/qr-generator/issues/new?labels=enhancement&template=feature-request---.md">Request an Upgrade</a>
  </p>
</div>

## ✨ About Project

A Python project for creating beautiful, customizable QR codes with various shapes, colors, and center images while maintaining scannability. Now with a stunning dark-mode Streamlit web interface! 🎨

## 🚀 Features

- 🔷 **Multiple Module Shapes**: Square, Diamond, Rounded corners, Hexagon
- 🎨 **Custom Colors**: Set different colors for data modules and finder patterns
- 📤 **Center Images**: Add logos or images to the center of QR codes
- ⚡ **High Quality**: Maintains image quality and QR code scannability
- 🖥️ **Web Interface**: Beautiful Streamlit UI with live preview
- 👁️ **Live Preview**: See your changes in real-time before generating
- 📥 **Easy Download**: One-click download of generated QR codes

## 📦 Installation

1. Clone this repository:
```bash
git clone https://github.com/Vania-Dev/qr-generator.git
cd qr-generator
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## 🎯 Quick Start

### 🖥️ Option 1: Web Interface (Recommended)

Launch the beautiful Streamlit web interface:

```bash
streamlit run app.py
```

Then open your browser at `http://localhost:8501` and enjoy the interactive UI! 🎨

**Features of the Web Interface:**
- 🔷 Click buttons to select module shapes (Square, Diamond, Rounded, Hexagon)
- 🎨 Use color pickers for Fill, Finder, and Background colors
- 👁️ See live previews of your shape and color scheme
- 📤 Upload center logos with drag & drop
- ⚡ Generate QR codes instantly
- 📥 Download with one click

### 💻 Option 2: Python API

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

## 📁 Project Structure

```
qr-generator/
├── 📄 app.py                 # Streamlit web interface
├── 📄 qr_generator.py        # Core QR generator class
├── 📄 main.py                # CLI examples
├── 📄 requirements.txt       # Python dependencies
├── 📄 README.md              # This file
├── 📄 LICENSE.txt            # MIT License
├── 📁 images/                # Sample images and logos
│   ├── vaniadev.png
│   └── video.jpg
└── 📁 output/                # Generated QR codes (auto-created)
    └── qr_code.png
```

## 🎮 How to Use

### Using the Web Interface

1. **Start the app:**
   ```bash
   streamlit run app.py
   ```

2. **Configure your QR:**
   - Enter your URL or text in the input field
   - Click on a shape button (Square, Diamond, Rounded, Hexagon)
   - Pick your colors using the color pickers
   - Watch the live preview update in real-time!

3. **Add a logo (optional):**
   - Click "Browse files" or drag & drop your logo
   - Supported formats: PNG, JPG, JPEG, GIF

4. **Generate & Download:**
   - Click "🚀 Generate QR Code"
   - Your QR appears on the right side
   - Click "⬇️ Download QR Code" to save it

### Using Python Code

```python
from qr_generator import StylizedQRGenerator

# Create generator
generator = StylizedQRGenerator()

# Generate QR code
generator.generate_qr(
    data="https://your-url.com",
    fill_color='#00d9ff',      # Cyan
    finder_color='#7b2ff7',    # Purple
    back_color='#0f0f23',      # Dark background
    center_image="logo.png",   # Your logo
    module_shape='diamond',    # Shape style
    output_path="my_qr.png"    # Output file
)
```

## 🔷 Module Shapes

| Shape | Description | Visual |
|-------|-------------|--------|
| ⬜ **Square** | Standard QR code modules - reliable and widely compatible | Classic |
| ◆ **Diamond** | Rotated squares creating an elegant diamond pattern | Modern |
| ⬭ **Rounded** | Squares with rounded corners for a softer appearance | Smooth |
| ⬡ **Hexagon** | Regular hexagons creating a unique honeycomb pattern | Creative |

## 📚 API Reference

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

## 💡 Code Examples

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

## 🎨 Color Formats

Colors can be specified in several formats:
- Hex codes: `#FF6B6B`, `#1E3A8A`
- Color names: `red`, `blue`, `white`, `black`
- RGB tuples: `(255, 107, 107)`

## 📸 Center Image Guidelines

For best results with center images:
- Use square images (1:1 aspect ratio)
- Recommended size: 200x200 pixels or larger
- Supported formats: PNG, JPG, JPEG, GIF
- Images are automatically resized to 1/5 of QR code size
- A white circular background is added for better contrast

## 🔧 Technical Details

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

## 📦 Dependencies

- `qrcode[pil]` - QR code generation
- `Pillow` - Image processing and drawing
- `streamlit` - Web interface

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is open source. Feel free to use and modify as needed.

Distributed under the MIT license. See the `LICENSE.txt` file for more information.

## 🐛 Troubleshooting

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

## 🎨 Examples Gallery

The generator can create various styles:
- 🏢 Corporate QR codes with company logos
- 🎉 Event QR codes with custom branding
- 📱 Social media QR codes with profile images
- 🛍️ Product QR codes with brand colors
- 🎭 Creative QR codes with unique shapes

## 🌟 Screenshots

### Web Interface
The Streamlit interface features:
- 🌙 Beautiful dark mode design
- 🎨 Intuitive color pickers
- 👁️ Real-time shape and color previews
- 📤 Drag & drop logo upload
- ⚡ Instant QR generation

### Generated QR Codes
Examples of different styles:
- Classic black & white square QR
- Colorful diamond-shaped QR with logo
- Rounded corners with brand colors
- Hexagon pattern with custom finder colors

<!-- CONTACT -->
## 📧 Contacto

[![YouTube](https://img.shields.io/badge/YouTube-vaniadev-FF0000?style=for-the-badge&logo=youtube&logoColor=white&labelColor=101010)](https://youtube.com/@VANIADEV)
[![Instagram](https://img.shields.io/badge/Instagram-@vania_dev_-E4405F?style=for-the-badge&logo=instagram&logoColor=white&labelColor=101010)](https://www.instagram.com/vania_dev_/)
[![TikTok](https://img.shields.io/badge/TikTok-@vania_dev_-69C9D0?style=for-the-badge&logo=tiktok&logoColor=white&labelColor=101010)](https://www.tiktok.com/@vania_dev_)
[![Facebook](https://img.shields.io/badge/Facebook-@vaniadev-1877F2?style=for-the-badge&logo=facebook&logoColor=white&labelColor=101010)](https://www.facebook.com/SMAEMX)
[![Link](https://img.shields.io/badge/Links-vaniadev-39E09B?style=for-the-badge&logo=Linktree&logoColor=white&labelColor=101010)](https://beacons.ai/vaniadev)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Ivan_Castañeda-0077B5?style=for-the-badge&logo=linkedin&logoColor=white&labelColor=101010)](https://www.linkedin.com/in/ivan-castaneda-nazario/)
[![Web](https://img.shields.io/badge/Web-vaniadev-14a1f0?style=for-the-badge&logo=dev.to&logoColor=white&labelColor=101010)](https://vaniadev.super.site/)
[![BuyMeACoffee](https://img.shields.io/badge/Buy_Me_A_Coffee-apoya_mi_trabajo-FFDD00?style=for-the-badge&logo=buy-me-a-coffee&logoColor=white&labelColor=101010)](https://buymeacoffee.com/vania_vaniusha)

---

<div align="center">

**Hazlo con el tipo de ❤️ que deja huellas en el alma**

[⭐ Star this repo](https://github.com/Vania-Dev/qr-generator) • [🐛 Report Bug](https://github.com/Vania-Dev/qr-generator/issues) • [✨ Request Feature](https://github.com/Vania-Dev/qr-generator/issues)

</div>
