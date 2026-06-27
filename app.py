import streamlit as st
from google import genai
from google.genai import types

# Mengatur tampilan halaman
st.set_page_config(page_title="Generator Gambar Shopee", page_icon="🛍️")

st.title("🛍️ Generator Thumbnail Shopee 8K")
st.write("Aplikasi AI untuk menyulap judul & deskripsi menjadi foto produk estetik dan profesional.")

# Kolom di samping untuk Kunci Akses (API Key)
with st.sidebar:
    st.header("Pengaturan AI")
    api_key = st.text_input("Masukkan Google API Key", type="password")

# Area Input Produk
st.subheader("Data Produk Anda")
judul_produk = st.text_input("Judul Produk", placeholder="Contoh: Relay Ptc Overload Kulkas...")
deskripsi_produk = st.text_area("Deskripsi / Detail Produk", placeholder="Contoh: Model kulkas 1 pintu, 1 SET...")

# Tombol Eksekusi
if st.button("Generate Gambar 8K", type="primary"):
    if not api_key:
        st.error("Gagal: Anda belum memasukkan API Key di menu sebelah kiri.")
    elif not judul_produk:
        st.warning("Mohon isi minimal Judul Produk terlebih dahulu.")
    else:
        # Master Prompt Rahasia Anda
        master_prompt = f"""
        Edit foto produk menjadi thumbnail Shopee yang estetik, profesional, realistis, dan sangat menjual.
        
        DATA PRODUK:
        - Judul: [{judul_produk}]
        - Detail: {deskripsi_produk}
        
        INSTRUKSI VISUAL:
        Fokus utama adalah produk terlihat lebih nyata, tajam, bersih, detail, presisi, dan menonjol. 
        Background: clean, modern, cerah, estetik. Pencahayaan studio lembut namun tegas.
        Teks Promosi: "BEST QUALITY" atau "READY STOCK". 
        Watermark: Transparan bertuliskan "NAURA ULFA" di bagian tengah produk.
        
        KUALITAS AKHIR: Rasio 1:1. Resolusi tinggi. Sangat tajam, tidak pecah, seperti foto produk studio premium.
        """
        
        st.info("Mengirim instruksi ke AI Google... Mohon tunggu sebentar (bisa memakan waktu 10-30 detik).")
        
        # Proses Menghubungi Google AI menggunakan library terbaru (google-genai)
        try:
            client = genai.Client(api_key=api_key)
            response = client.models.generate_images(
                model='imagen-3.0-generate-001',
                prompt=master_prompt,
                config=types.GenerateImagesConfig(
                    number_of_images=1,
                    aspect_ratio="1:1"
                )
            )
            
            for generated_image in response.generated_images:
                # Streamlit langsung membaca data gambar (raw bytes) dari Google
                st.image(generated_image.image.image_bytes, caption=f"Hasil Generate: {judul_produk}")
                st.success("Berhasil! Gambar siap digunakan. (Klik Kanan pada gambar -> Save Image As).")
                
        except Exception as e:
            st.error(f"Terjadi kendala saat menghubungi AI: {e}")
