import streamlit as st
from PIL import Image
import requests
import io
import base64
import random

# Sayfa yapılandırması
st.set_page_config(
    page_title="Logo Üretici", 
    layout="wide"
)

# Minimal CSS
st.markdown("""
<style>
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
        color: white !important;
        border: none;
        border-radius: 8px;
        padding: 12px 32px;
        font-size: 16px;
        font-weight: 600;
        width: 100%;
    }
    
    .stButton > button:hover {
        color: white !important;
    }
    
    .download-button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white !important;
        padding: 25px 245px;
        border-radius: 8px;
        text-decoration: none;
        font-weight: 600;
        display: inline-block;
        margin-top: 12px;
        text-align: center;
        width: auto;
        font-size: 14px;
    }
    
    .download-button:hover {
        text-decoration: none;
        color: white !important;
    }
    
    .download-button:visited {
        color: white !important;
    }
    
    .developer-info {
        text-align: center;
        margin-top: 50px;
        padding: 20px;
        border-top: 1px solid #e0e0e0;
    }
    
    .developer-link {
        color: #667eea;
        text-decoration: none;
        font-weight: 600;
    }
    
    .developer-link:hover {
        color: #764ba2;
        text-decoration: underline;
    }
</style>
""", unsafe_allow_html=True)

st.title("Logo Üretici")
st.write("Yazdığınız tanıma göre otomatik logo varyasyonları oluşturun")

prompt = st.text_input("Logo Tanımı", placeholder="Örnek: minimalist, doğa temalı bir yoga uygulaması")

if st.button("Logo Varyasyonları Oluştur"):
    if prompt.strip() == "":
        st.warning("Lütfen bir logo tanımı girin.")
    else:
        with st.spinner("Logo varyasyonları oluşturuluyor..."):
            num_variations = 3
            positive_prompt = f"{prompt}, logo design, minimalist, vector, white background"
            negative_prompt = "text, watermark, signature, blurry, low quality"
            url = "http://127.0.0.1:7860/sdapi/v1/txt2img"
            
            cols = st.columns(3)
            
            for i in range(num_variations):
                seed = random.randint(1, 99999999)
                
                payload = {
                    "prompt": positive_prompt,
                    "negative_prompt": negative_prompt,
                    "steps": 25,
                    "cfg_scale": 7,
                    "width": 512,
                    "height": 512,
                    "sampler_index": "Euler",
                    "seed": seed
                }
                
                try:
                    response = requests.post(url, json=payload)
                    r = response.json()
                    image_base64 = r.get('images', [None])[0]
                    
                    if image_base64:
                        image_bytes = base64.b64decode(image_base64)
                        image = Image.open(io.BytesIO(image_bytes))
                        
                        with cols[i]:
                            st.image(image, caption=f"Varyasyon {i+1}")
                            
                            # İndirme butonu
                            buffered = io.BytesIO()
                            image.save(buffered, format="PNG")
                            b64 = base64.b64encode(buffered.getvalue()).decode()
                            href = f'<a href="data:image/png;base64,{b64}" download="logo_varyasyon_{i+1}.png" class="download-button">İndir</a>'
                            st.markdown(href, unsafe_allow_html=True)
                    else:
                        with cols[i]:
                            st.error(f"Varyasyon {i+1} üretilemedi.")
                            
                except Exception as e:
                    with cols[i]:
                        st.error(f"Hata (Varyasyon {i+1}): {e}")

# Geliştirici bilgisi
st.markdown("""
<div class="developer-info">
    <p>Geliştirici: <a href="https://www.linkedin.com/in/keremerkengel/" target="_blank" class="developer-link">Kerem Erkengel</a></p>
</div>
""", unsafe_allow_html=True)