import streamlit as st
from google import genai
from google.genai import types
from PIL import Image

# Mengatur tampilan halaman
st.set_page_config(page_title="Generator Gambar Shopee", page_icon="🛍️", layout="wide")

st.title("🛍️ Generator Thumbnail Shopee 8K")
st.write("Aplikasi AI Multimodal: Gabungkan foto produk asli dengan referensi gaya visual.")

# Kolom di samping untuk Kunci Akses (API Key)
with st.sidebar:
    st.header("Pengaturan AI")
    api_key = st.text_input("Masukkan Google API Key", type="password")
    st.info("Pastikan Billing (Penagihan) Anda sudah aktif di Google AI Studio.")

# Area Input Gambar (Membagi layar jadi 2 kolom)
st.subheader("1. Upload Gambar Anda")
col1, col2 = st.columns(2)

with col1:
    # PERUBAHAN ADA DI SINI: Menambahkan "webp" ke dalam daftar format yang didukung
    gambar1_file = st.file_uploader("Upload Gambar 1 (Foto Produk Asli)", type=["jpg", "jpeg", "png", "webp"])
    if gambar1_file:
        img1 = Image.open(gambar1_file)
        st.image(img1, caption="Gambar 1: Produk Asli", use_column_width=True)

with col2:
    # PERUBAHAN ADA DI SINI: Menambahkan "webp" ke dalam daftar format yang didukung
    gambar2_file = st.file_uploader("Upload Gambar 2 (Referensi Konsep)", type=["jpg", "jpeg", "png", "webp"])
    if gambar2_file:
        img2 = Image.open(gambar2_file)
        st.image(img2, caption="Gambar 2: Referensi Konsep", use_column_width=True)

# Area Input Teks
st.subheader("2. Data Produk Anda")
judul_produk = st.text_input("Judul Produk", placeholder="Contoh: Relay Ptc Overload Kulkas...")
deskripsi_produk = st.text_area("Deskripsi / Detail Produk", placeholder="Contoh: Model kulkas 1 pintu, 1 SET...")

# Tombol Eksekusi
if st.button("Generate Gambar 8K", type="primary"):
    if not api_key:
        st.error("Gagal: Anda belum memasukkan API Key di menu sebelah kiri.")
    elif not gambar1_file or not gambar2_file:
        st.warning("Mohon upload Gambar 1 dan Gambar 2 terlebih dahulu.")
    elif not judul_produk:
        st.warning("Mohon isi Judul Produk terlebih dahulu.")
    else:
        # Master Prompt Sesuai Instruksi Anda
        master_prompt_teks = f"""
        Edit foto produk pada Gambar 1 menjadi thumbnail Shopee yang estetik, profesional, realistis, dan sangat menjual. 
        Gunakan Gambar 2 sebagai referensi konsep utama. Samakan gaya visual, nuansa desain, warna background, pencahayaan, komposisi, dan tata letak agar hasil akhir seragam dan semirip mungkin dengan konsep pada Gambar 2.

        DATA PRODUK:
        - Judul: [{judul_produk}]
        - Detail: {deskripsi_produk}
        
        INSTRUKSI VISUAL TAMBAHAN:
        Fokus utama adalah produk pada Gambar 1. Buat objek produk terlihat lebih nyata, tajam, bersih, detail, presisi, dan lebih menonjol. Produk harus menjadi pusat perhatian, terlihat premium, rapi, dan meyakinkan. Jangan mengubah bentuk asli produk, warna asli produk, ukuran proporsional, maupun detail fisik lainnya.

        Teks Promosi: Tambahkan teks "BEST QUALITY" atau "READY STOCK" dengan font modern tanpa menutupi produk utama. 
        Watermark: Tambahkan watermark transparan bertuliskan "NAURA ULFA" tepat di bagian tengah produk. Watermark tipis, elegan, opacity rendah.
        
        KUALITAS AKHIR: Rasio 1:1. Resolusi sangat tinggi. Sangat tajam, tidak pecah, seperti foto produk studio premium.
        """
        
        st.info("Menganalisis gambar dan mengirim instruksi ke AI Google... Mohon tunggu (bisa memakan waktu 20-40 detik).")
        
        try:
            client = genai.Client(api_key=api_key)
            
            # Kita mengirimkan Teks dan 2 Gambar sekaligus ke AI
            isi_konten = [
                "Ini adalah Gambar 1 (Foto Produk Asli):", img1,
                "Ini adalah Gambar 2 (Referensi Konsep):", img2,
                master_prompt_teks
            ]
            
            response = client.models.generate_content(
                model='gemini-2.5-flash-image',
                contents=isi_konten,
                config=types.GenerateContentConfig(
                    response_modalities=["IMAGE"],
                    image_config=types.ImageConfig(
                        aspect_ratio="1:1"
                    )
                )
            )
            
            for part in response.parts:
                if part.inline_data:
                    st.image(part.inline_data.data, caption=f"Hasil Generate: {judul_produk}", use_column_width=True)
                    st.success("Berhasil! Gambar siap digunakan. (Klik Kanan pada gambar -> Save Image As).")
                
        except Exception as e:
            st.error(f"Terjadi kendala saat menghubungi AI: {e}")
            st.write("Pastikan API Key Anda aktif dan Billing Anda sudah diatur.")
