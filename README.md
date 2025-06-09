# Prompt'tan Logo Üretici

Bu proje, kullanıcının yazdığı kısa bir tanıma (prompt) göre yapay zeka destekli logo varyasyonları üretir. Arayüz Streamlit ile, görsel üretimi ise Stable Diffusion ile sağlanmıştır.

---

## Özellikler

- Tek prompt'tan birden fazla logo varyasyonu üretimi
- Her logonun indirilebilir versiyonu
- Modern ve sade arayüz (özelleştirilmiş CSS)
- Open-source AI modeli (Stable Diffusion) ile lokal çalışır

---

## Kullanılan Teknolojiler

- Python 3.10+
- Streamlit – web arayüzü
- Stable Diffusion (Automatic1111) – görsel üretimi
- Pillow (PIL) – görsel işleme
- requests – API istekleri
- python-dotenv – gizli bilgileri yönetme

---

## Örnek Kullanım

| Prompt | Logo |
|--------|------|
| finance logo | ![Örnek](/examples/finance.png) |
| fitness uygulaması | ![Örnek](/examples/fitness.png) |
| futbol takımı logosu | ![Örnek](/examples/football.png) |

---

## Kurulum

```bash
git clone https://github.com/keremerkengel/prompt2logo.git
cd prompt2logo

pip install -r requirements.txt

streamlit run app.py
```

---

## Klasör Yapısı

```
prompt2logo/
├── app.py
├── README.md
├── requirements.txt       
└── examples/         # örnek logolar
```

---

## Geliştirici

**Kerem Erkengel**  
Yapay zeka destekli içerik üretimi ve arayüz geliştirme alanında çalışan bir geliştirici.  
GitHub: https://github.com/keremerkengel
Website: https://www.keremerkengel.com.tr/
LinkedIn: https://www.linkedin.com/in/keremerkengel/


---

## Lisans

Bu proje açık kaynaklıdır ve dilediğiniz gibi kullanılabilir. Ticari kullanım için lütfen kaynak gösteriniz.
