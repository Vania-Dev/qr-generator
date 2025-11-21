# Import required libraries
import qrcode  # QR code generation library
from PIL import Image, ImageDraw  # Image processing and drawing
import os  # File system operations
import math  # Mathematical functions for shape calculations

class StylizedQRGenerator:
    """A QR code generator with custom styling options.
    
    This class provides functionality to create QR codes with:
    - Custom module shapes (square, diamond, rounded, hexagon)
    - Custom colors for modules and finder patterns
    - Center logo/image embedding
    - High-quality output with proper contrast
    
    The generated QR codes maintain scannability while providing
    enhanced visual appeal for branding and design purposes.
    """
    
    def __init__(self):
        """Initialize the QR generator with default settings."""
        # Configure QR code parameters:
        # version=1: Smallest QR code (21x21 modules)
        # box_size=10: Each module is 10x10 pixels
        # border=4: 4-module border around the QR code
        self.qr = qrcode.QRCode(version=1, box_size=10, border=4)
    
    def generate_qr(self, data, fill_color='black', back_color='white', 
                   center_image=None, output_path='qr_code.png', module_shape='square', finder_color=None):
        """Generate QR code with custom styling and optional center image.
        
        Args:
            data (str): The data to encode in the QR code (URL, text, etc.)
            fill_color (str): Color for QR modules (hex code or color name)
            back_color (str): Background color (hex code or color name)
            center_image (str): Path to image file to place in center
            output_path (str): Where to save the generated QR code
            module_shape (str): Shape of data modules ('square', 'diamond', 'rounded', 'hexagon')
            finder_color (str): Color for corner finder patterns (defaults to fill_color)
            
        Returns:
            str: Path to the generated QR code image
        """
        # Clear any previous data and add new data
        self.qr.clear()
        self.qr.add_data(data)
        self.qr.make(fit=True)  # Automatically adjust QR version if needed
        
        # Generate QR image based on shape preference
        if module_shape == 'square':
            # Use built-in square modules for standard QR codes
            qr_img = self.qr.make_image(fill_color=fill_color, back_color=back_color)
        else:
            # Create custom QR with special shapes
            qr_img = self._create_custom_qr(fill_color, back_color, module_shape, finder_color or fill_color)
        
        # Add center image if provided
        if center_image:
            qr_img = self._add_center_image(qr_img, center_image)
        
        # Save the final QR code
        qr_img.save(output_path)
        return output_path
    
    def _add_center_image(self, qr_img, center_image_path):
        """Add a logo or image to the center of the QR code.
        
        Args:
            qr_img (PIL.Image): The QR code image
            center_image_path (str): Path to the center image file
            
        Returns:
            PIL.Image: QR code with center image added
        """
        # Check if image file exists
        if not os.path.exists(center_image_path):
            return qr_img
            
        # Convert QR to RGBA mode for better transparency handling
        qr_img = qr_img.convert('RGBA')
        
        # Load and prepare center image
        center_img = Image.open(center_image_path).convert('RGBA')
        qr_width, qr_height = qr_img.size
        
        # Calculate center image size (1/5 of QR code size for optimal scanning)
        center_size = min(qr_width, qr_height) // 5
        center_img = center_img.resize((center_size, center_size), Image.Resampling.LANCZOS)
        
        # Create white circular background for better contrast and readability
        background = Image.new('RGBA', (center_size + 20, center_size + 20), (255, 255, 255, 255))
        bg_mask = Image.new('L', (center_size + 20, center_size + 20), 0)
        bg_draw = ImageDraw.Draw(bg_mask)
        bg_draw.ellipse((0, 0, center_size + 20, center_size + 20), fill=255)
        
        # Position and paste the white background circle
        bg_pos = ((qr_width - center_size - 20) // 2, (qr_height - center_size - 20) // 2)
        qr_img.paste(background, bg_pos, bg_mask)
        
        # Position and paste the center image on top
        pos = ((qr_width - center_size) // 2, (qr_height - center_size) // 2)
        qr_img.paste(center_img, pos, center_img)
        
        return qr_img
    
    def _create_custom_qr(self, fill_color, back_color, shape, finder_color):
        """Create QR code with custom module shapes and finder patterns.
        
        Args:
            fill_color (str): Color for data modules
            back_color (str): Background color
            shape (str): Shape type for data modules
            finder_color (str): Color for finder patterns
            
        Returns:
            PIL.Image: Custom styled QR code image
        """
        # Get QR code data and dimensions
        modules = self.qr.modules  # 2D array of True/False for each module
        box_size = self.qr.box_size  # Size of each module in pixels
        border = self.qr.border  # Border size in modules
        module_count = len(modules)  # Number of modules per side
        
        # Calculate total image size including border
        size = (module_count + border * 2) * box_size
        img = Image.new('RGB', (size, size), back_color)
        draw = ImageDraw.Draw(img)
        
        # Draw finder patterns first (the three corner squares)
        self._draw_custom_finder_patterns(draw, modules, box_size, border, finder_color, back_color)
        
        # Draw data modules with custom shapes
        for r, row in enumerate(modules):
            for c, module in enumerate(row):
                # Only draw if module is active and not part of finder pattern
                if module and not self._is_finder_pattern(r, c, module_count):
                    # Calculate pixel position
                    x = (c + border) * box_size
                    y = (r + border) * box_size
                    
                    # Draw appropriate shape
                    if shape == 'diamond':
                        self._draw_diamond(draw, x, y, box_size, fill_color)
                    elif shape == 'rounded':
                        self._draw_rounded_square(draw, x, y, box_size, fill_color)
                    elif shape == 'hexagon':
                        self._draw_hexagon(draw, x, y, box_size, fill_color)
        
        return img
    
    def _draw_custom_finder_patterns(self, draw, modules, box_size, border, finder_color, back_color):
        """Draw the three corner finder patterns with rounded rectangles.
        
        Finder patterns are the large squares in QR code corners that help scanners
        locate and orient the code. Each has a 7x7 outer square, 5x5 inner white area,
        and 3x3 center square.
        
        Args:
            draw (ImageDraw): PIL drawing context
            modules (list): QR code module matrix
            box_size (int): Size of each module in pixels
            border (int): Border size in modules
            finder_color (str): Color for finder pattern elements
            back_color (str): Background color for inner areas
        """
        module_count = len(modules)
        
        # Define positions for the three finder patterns
        # Top-left, top-right, and bottom-left corners
        positions = [(0, 0), (0, module_count - 7), (module_count - 7, 0)]
        
        for start_r, start_c in positions:
            # Calculate pixel coordinates
            x = (start_c + border) * box_size
            y = (start_r + border) * box_size
            
            # Draw outer rounded square (7x7 modules)
            outer_size = 7 * box_size
            draw.rounded_rectangle([x, y, x + outer_size, y + outer_size], 
                                 radius=box_size, fill=finder_color)
            
            # Draw inner white area (5x5 modules)
            inner_x = x + box_size
            inner_y = y + box_size
            inner_size = 5 * box_size
            draw.rounded_rectangle([inner_x, inner_y, inner_x + inner_size, inner_y + inner_size], 
                                 radius=box_size//2, fill=back_color)
            
            # Draw center square (3x3 modules)
            center_x = x + 2 * box_size
            center_y = y + 2 * box_size
            center_size = 3 * box_size
            draw.rounded_rectangle([center_x, center_y, center_x + center_size, center_y + center_size], 
                                 radius=box_size//3, fill=finder_color)
    
    def _is_finder_pattern(self, r, c, module_count):
        """Check if a module position is part of a finder pattern.
        
        Args:
            r (int): Row position in module matrix
            c (int): Column position in module matrix
            module_count (int): Total modules per side
            
        Returns:
            bool: True if position is within any finder pattern area
        """
        # Top-left finder pattern (7x7 area)
        if r < 7 and c < 7:
            return True
        # Top-right finder pattern (7x7 area)
        if r < 7 and c >= module_count - 7:
            return True
        # Bottom-left finder pattern (7x7 area)
        if r >= module_count - 7 and c < 7:
            return True
        return False
    
    def _draw_diamond(self, draw, x, y, size, color):
        """Draw a diamond shape (rotated square).
        
        Args:
            draw (ImageDraw): PIL drawing context
            x, y (int): Top-left corner of module area
            size (int): Size of module area
            color (str): Fill color for the diamond
        """
        # Calculate center point of the module
        cx, cy = x + size // 2, y + size // 2
        # Diamond extends to 50% of module size from center
        half_size = size * 0.5
        
        # Define diamond points (top, right, bottom, left)
        points = [
            (cx, cy - half_size),  # Top point
            (cx + half_size, cy),  # Right point
            (cx, cy + half_size),  # Bottom point
            (cx - half_size, cy)   # Left point
        ]
        draw.polygon(points, fill=color)
    
    def _draw_rounded_square(self, draw, x, y, size, color):
        """Draw a square with rounded corners.
        
        Args:
            draw (ImageDraw): PIL drawing context
            x, y (int): Top-left corner of module area
            size (int): Size of module area
            color (str): Fill color for the rounded square
        """
        # Corner radius is 1/4 of the module size
        radius = size // 4
        # Draw with 1-pixel margin to prevent overlap
        draw.rounded_rectangle([x + 1, y + 1, x + size - 1, y + size - 1], 
                              radius=radius, fill=color)
    
    def _draw_hexagon(self, draw, x, y, size, color):
        """Draw a regular hexagon shape.
        
        Args:
            draw (ImageDraw): PIL drawing context
            x, y (int): Top-left corner of module area
            size (int): Size of module area
            color (str): Fill color for the hexagon
        """
        # Calculate center point of the module
        cx, cy = x + size // 2, y + size // 2
        # Hexagon radius is 50% of module size
        radius = size * 0.4
        
        # Calculate hexagon vertices
        points = []
        for i in range(6):
            # Each vertex is 60 degrees apart, rotated 30 degrees for flat top
            angle = math.pi / 3 * i - math.pi / 6
            px = cx + radius * math.cos(angle)
            py = cy + radius * math.sin(angle)
            points.append((px, py))
        
        draw.polygon(points, fill=color)

# Example usage and demonstrations
if __name__ == "__main__":
    # Create generator instance
    generator = StylizedQRGenerator()
    
    # Example 1: Basic QR code with default square modules
    # generator.generate_qr("https://example.com", output_path="basic_qr.png")
    
    # Example 2: Colored QR code with custom colors
    # generator.generate_qr("https://example.com", fill_color='#FF6B6B', 
    #                     back_color='#4ECDC4', output_path="colored_qr.png")
    
    # Example 3: Diamond-shaped modules with red finder patterns
    generator.generate_qr("https://ivancastaneda.super.site", 
                         fill_color='#1E3A8A',        # Blue diamonds
                         back_color='white',           # White background
                         center_image="images/VaniaDev.png",  # Logo in center
                         module_shape='diamond',       # Diamond-shaped data modules
                         finder_color='#DC2626',       # Red corner squares
                         output_path="VaniaDev_QR.png")
    
    # Example 4: Hexagon-shaped modules with contrasting colors
    generator.generate_qr("https://pythoncdmx.org", 
                         fill_color='#059669',         # Green hexagons
                         back_color='black',           # Black background
                         center_image="images/pythoncdmx.png",  # Logo in center
                         module_shape='hexagon',       # Hexagon-shaped data modules
                         finder_color='#DC2626',       # Red corner squares
                         output_path="PythonCDMX_QR.png")
    
    # Example 5: Rounded-shaped modules with contrasting colors
    generator.generate_qr("https://github.com/Vania-Dev/AWS-Exam-Qustons-AI-Local", 
                         fill_color='black',         # black rounded
                         back_color='white',           # White background
                         center_image="images/github.png",  # Logo in center
                         module_shape='rounded',       # Rounded-shaped data modules
                         finder_color='#DC2626',       # Red corner squares
                         output_path="MyRepo_QR.png")
    
    print("QR codes generated successfully!")