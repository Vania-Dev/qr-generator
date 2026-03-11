import streamlit as st
from qr_generator import StylizedQRGenerator
import os
from PIL import Image, ImageDraw
import io

st.set_page_config(page_title="QR Code Generator", page_icon="📱", layout="wide")

# Custom CSS for dark mode styling
st.markdown("""
<style>
    .main {
        background: #0f0f23;
    }
    .stApp {
        background: #0f0f23;
    }
    div[data-testid="stVerticalBlock"] > div:has(div.stButton) {
        display: flex;
        gap: 10px;
    }
    .stButton > button {
        background: #1a1a2e;
        color: #00d9ff;
        border: 2px solid #00d9ff;
        border-radius: 12px;
        font-weight: 600;
        transition: all 0.3s;
        height: 80px;
        font-size: 16px;
    }
    .stButton > button:hover {
        background: #00d9ff;
        color: #0f0f23;
        transform: translateY(-2px);
        box-shadow: 0 5px 20px rgba(0, 217, 255, 0.4);
    }
    .stButton > button[kind="primary"] {
        background: linear-gradient(135deg, #00d9ff 0%, #7b2ff7 100%);
        color: white;
        border: none;
        font-size: 18px;
        height: 50px;
    }
    .stButton > button[kind="primary"]:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(0, 217, 255, 0.5);
    }
    .stTextInput > div > div > input {
        background: #1a1a2e;
        color: #ffffff;
        border-radius: 10px;
        border: 2px solid #2d2d44;
        padding: 12px;
    }
    .stTextInput > div > div > input:focus {
        border-color: #00d9ff;
    }
    .stTextInput > label, .stFileUploader > label {
        color: #00d9ff !important;
        font-weight: 600;
        font-size: 16px;
    }
    h1 {
        color: #00d9ff;
        text-align: center;
        font-size: 3.5rem;
        margin-bottom: 0;
        text-shadow: 0 0 20px rgba(0, 217, 255, 0.5);
        font-weight: 800;
    }
    h3 {
        color: #00d9ff;
        font-weight: 700;
    }
    h4 {
        color: #7b2ff7;
        font-weight: 600;
    }
    .subtitle {
        color: #a0a0c0;
        text-align: center;
        font-size: 1.3rem;
        margin-bottom: 1rem;
    }
    div[data-testid="stImage"] {
        display: flex;
        justify-content: center;
    }
    .preview-box {
        background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
        border-radius: 20px;
        padding: 30px;
        box-shadow: 0 10px 40px rgba(0, 0, 0, 0.5);
        border: 1px solid #2d2d44;
        min-height: 600px;
    }
    .config-box {
        background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
        border-radius: 20px;
        padding: 30px;
        box-shadow: 0 10px 40px rgba(0, 0, 0, 0.5);
        border: 1px solid #2d2d44;
    }
    .preview-label {
        color: #a0a0c0;
        font-weight: 600;
        font-size: 14px;
        margin-bottom: 8px;
    }
    .stFileUploader {
        background: #1a1a2e;
        border-radius: 10px;
        padding: 10px;
        border: 2px dashed #2d2d44;
    }
    .stFileUploader:hover {
        border-color: #00d9ff;
    }
    .feature-card {
        background: #1a1a2e;
        border-radius: 15px;
        padding: 20px;
        margin: 10px 0;
        border: 1px solid #2d2d44;
        text-align: center;
    }
    .feature-icon {
        font-size: 2.5rem;
        margin-bottom: 10px;
    }
    .feature-text {
        color: #a0a0c0;
        font-size: 1rem;
        font-weight: 500;
    }
    div[data-testid="stColorPicker"] > label {
        color: #a0a0c0 !important;
        font-size: 14px;
    }
</style>
""", unsafe_allow_html=True)

def create_shape_preview(shape, color):
    """Create a small preview image of the selected shape"""
    size = 100
    img = Image.new('RGB', (size, size), 'white')
    draw = ImageDraw.Draw(img)
    
    if shape == "square":
        draw.rectangle([20, 20, 80, 80], fill=color)
    elif shape == "diamond":
        draw.polygon([(50, 10), (90, 50), (50, 90), (10, 50)], fill=color)
    elif shape == "rounded":
        draw.rounded_rectangle([20, 20, 80, 80], radius=15, fill=color)
    elif shape == "hexagon":
        import math
        cx, cy, radius = 50, 50, 35
        points = [(cx + radius * math.cos(math.pi / 3 * i - math.pi / 6),
                   cy + radius * math.sin(math.pi / 3 * i - math.pi / 6)) for i in range(6)]
        draw.polygon(points, fill=color)
    
    return img

def create_color_preview(fill_color, finder_color, back_color, module_shape):
    """Create a preview showing the color scheme with selected module shape"""
    import math
    size = 150
    img = Image.new('RGB', (size, size), back_color)
    draw = ImageDraw.Draw(img)
    
    # Finder pattern preview (corner)
    draw.rounded_rectangle([10, 10, 50, 50], radius=5, fill=finder_color)
    draw.rounded_rectangle([18, 18, 42, 42], radius=3, fill=back_color)
    draw.rounded_rectangle([23, 23, 37, 37], radius=2, fill=finder_color)
    
    # Data modules preview with selected shape
    for i in range(3):
        for j in range(3):
            x, y = 70 + i * 25, 20 + j * 25
            
            if module_shape == "square":
                draw.rectangle([x, y, x + 18, y + 18], fill=fill_color)
            elif module_shape == "diamond":
                cx, cy = x + 9, y + 9
                draw.polygon([(cx, cy - 9), (cx + 9, cy), (cx, cy + 9), (cx - 9, cy)], fill=fill_color)
            elif module_shape == "rounded":
                draw.rounded_rectangle([x, y, x + 18, y + 18], radius=4, fill=fill_color)
            elif module_shape == "hexagon":
                cx, cy, radius = x + 9, y + 9, 8
                points = [(cx + radius * math.cos(math.pi / 3 * k - math.pi / 6),
                           cy + radius * math.sin(math.pi / 3 * k - math.pi / 6)) for k in range(6)]
                draw.polygon(points, fill=fill_color)
    
    return img

st.title("⚡ QR Code Generator")
st.markdown('<p class="subtitle">Create stunning QR codes with custom shapes and colors</p>', unsafe_allow_html=True)

col1, col2 = st.columns([1, 1])

with col1:
    #st.markdown('<div class="config-box">', unsafe_allow_html=True)
    st.markdown("### ⚙️ Configuration")
    
    data = st.text_input("🔗 Enter URL or Text", placeholder="https://example.com", label_visibility="visible")
    
    st.markdown("#### 🔷 Choose Module Shape")
    col_shape1, col_shape2, col_shape3, col_shape4 = st.columns(4)
    
    with col_shape1:
        if st.button("⬜\n\nSquare", width="stretch", key="square"):
            st.session_state.module_shape = "square"
    with col_shape2:
        if st.button("◆\n\nDiamond", width="stretch", key="diamond"):
            st.session_state.module_shape = "diamond"
    with col_shape3:
        if st.button("⬭\n\nRounded", width="stretch", key="rounded"):
            st.session_state.module_shape = "rounded"
    with col_shape4:
        if st.button("⬡\n\nHexagon", width="stretch", key="hexagon"):
            st.session_state.module_shape = "hexagon"
    
    if 'module_shape' not in st.session_state:
        st.session_state.module_shape = "square"
    if 'generated_qr' not in st.session_state:
        st.session_state.generated_qr = None
    if 'qr_filename' not in st.session_state:
        st.session_state.qr_filename = None
    
    st.markdown("#### 🎨 Customize Colors")
    
    col_a, col_b, col_c = st.columns(3)
    with col_a:
        fill_color = st.color_picker("Fill Color", "#000000")
    with col_b:
        finder_color = st.color_picker("Finder Color", "#000000")
    with col_c:
        back_color = st.color_picker("Background", "#FFFFFF")
    
    st.markdown("#### 👁️ Live Preview")
    col_prev1, col_prev2 = st.columns(2)
    
    with col_prev1:
        st.markdown('<p class="preview-label">Shape Preview</p>', unsafe_allow_html=True)
        shape_preview = create_shape_preview(st.session_state.module_shape, fill_color)
        st.image(shape_preview, width=100)
    
    with col_prev2:
        st.markdown('<p class="preview-label">Color Scheme</p>', unsafe_allow_html=True)
        color_preview = create_color_preview(fill_color, finder_color, back_color, st.session_state.module_shape)
        st.image(color_preview, width=150)
    
    uploaded_file = st.file_uploader("📤 Upload Center Logo (Optional)", type=['png', 'jpg', 'jpeg', 'gif'])
    
    filename = st.text_input("📄 Filename", "qr_code.png")
    
    generate_btn = st.button("🚀 Generate QR Code", type="primary", width="stretch")
    
    if generate_btn:
        if not data:
            st.error("⚠️ Please enter data to encode")
        else:
            with st.spinner("Generating QR code..."):
                output_folder = "output"
                os.makedirs(output_folder, exist_ok=True)
                
                center_image_path = None
                if uploaded_file:
                    temp_path = os.path.join(output_folder, "temp_logo.png")
                    with open(temp_path, "wb") as f:
                        f.write(uploaded_file.getbuffer())
                    center_image_path = temp_path
                
                output_path = os.path.join(output_folder, filename)
                
                shape_map = {
                    "square": "square",
                    "diamond": "diamond",
                    "rounded": "rounded",
                    "hexagon": "hexagon"
                }
                
                generator = StylizedQRGenerator()
                generator.generate_qr(
                    data=data,
                    fill_color=fill_color,
                    back_color=back_color,
                    center_image=center_image_path,
                    output_path=output_path,
                    module_shape=shape_map[st.session_state.module_shape],
                    finder_color=finder_color
                )
                
                st.session_state.generated_qr = output_path
                st.session_state.qr_filename = filename
                
                if center_image_path and os.path.exists(temp_path):
                    os.remove(temp_path)
    
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    #st.markdown('<div class="preview-box">', unsafe_allow_html=True)
    st.markdown("### 🖼️ Your QR Code")
    
    if st.session_state.generated_qr and os.path.exists(st.session_state.generated_qr):
        st.success(f"✅ QR code generated successfully!")
        
        qr_image = Image.open(st.session_state.generated_qr)
        st.image(qr_image, width="stretch")
        
        with open(st.session_state.generated_qr, "rb") as file:
            st.download_button(
                label="⬇️ Download QR Code",
                data=file,
                file_name=st.session_state.qr_filename,
                mime="image/png",
                width="stretch"
            )
    else:
        st.markdown("""
        <div style='text-align: center; margin-top: 50px;'>
            <p style='color: #a0a0c0; font-size: 1.2rem; margin-bottom: 40px;'>👈 Configure your settings and generate your QR</p>
        </div>
        """, unsafe_allow_html=True)
        
        col_f1, col_f2 = st.columns(2)
        with col_f1:
            st.markdown("""
            <div class='feature-card'>
                <div class='feature-icon'>🔷</div>
                <div class='feature-text'>Multiple Shapes<br/>Square, Diamond, Rounded, Hexagon</div>
            </div>
            """, unsafe_allow_html=True)
            st.markdown("""
            <div class='feature-card'>
                <div class='feature-icon'>📤</div>
                <div class='feature-text'>Logo Support<br/>Add your brand to the center</div>
            </div>
            """, unsafe_allow_html=True)
        
        with col_f2:
            st.markdown("""
            <div class='feature-card'>
                <div class='feature-icon'>🎨</div>
                <div class='feature-text'>Custom Colors<br/>Personalize every detail</div>
            </div>
            """, unsafe_allow_html=True)
            st.markdown("""
            <div class='feature-card'>
                <div class='feature-icon'>⚡</div>
                <div class='feature-text'>Instant Generation<br/>Fast and high quality</div>
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("""
<div style='text-align: center; color: #a0a0c0; padding: 20px; margin-top: 30px;'>
    <p style='font-size: 0.9rem;'>Made with ❤️ | Craft it with the kind of ❤️ that leaves fingerprints on the soul</p>
</div>
""", unsafe_allow_html=True)
