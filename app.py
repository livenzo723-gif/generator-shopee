import streamlit as st
import requests
import urllib.parse

# Mengatur tampilan halaman
st.set_page_config(page_title="Generator Gambar Shopee Gratis", page_icon="🛍️", layout="wide")

st.title("🛍️ Generator Thumbnail Shopee - Versi Gratis")
st.write("Aplikasi AI versi gratis tanpa tarikan biaya dan tanpa perlu API Key.")

# Area Input Gambar
st.subheader("1. Upload Gambar Anda")
col1, col2 = st.columns(2)

with col1:
    gambar1_file = st.file_uploader("Upload Gambar 1 (Foto Produk Asli)", type=["jpg", "jpeg", "png", "webp"])
    if gambar1_file:
        st.image(gambar1_file, caption="Gambar 1: Produk Asli", width=200)

with col2:
    gambar2_file = st.file_uploader("Upload Gambar 2 (Referensi Konsep)", type=["jpg", "jpeg", "png", "webp"])
    if gambar2_file:
        st.image(gambar2_file, caption="Gambar 2: Referensi Konsep", width=200)

# Area Input Teks
st.subheader("2. Data Produk Anda")
judul_produk = st.text_input("Judul Produk", placeholder="Contoh: Relay Ptc Overload Kulkas Polytron 1 pintu")
deskripsi_produk = st.text_area("Deskripsi / Detail Produk", placeholder="Contoh: Relay Overload 1 Pin...")

# Tombol Eksekusi
if st.button("Generate Gambar Gratis", type="primary"):
    if not judul_produk:
        st.warning("Mohon isi Judul Produk terlebih dahulu.")
    else:
        # Menggunakan Prompt Sukses Anda
        master_prompt_teks = f"""
        Edit foto produk menjadi thumbnail Shopee yang estetik, profesional, realistis, mewah, bersih, modern, cerah.
        Produk utama: {judul_produk}. Detail: {deskripsi_produk}.
        Aturan: Hapus semua teks watermark lama dari toko lain. Tambahkan teks promosi 'BEST QUALITY' dan 'READY STOCK' dengan font modern. Tambahkan watermark transparan bertuliskan 'NAURA ULFA' tepat di bagian tengah produk. Rasio 1:1, sangat tajam, tidak pecah, pencahayaan studio, foto produk premium untuk jualan online, hindari hasil kartun.
        """
        
        st.info("Sedang memproses gambar di server gratis... Mohon tunggu sekitar 10-20 detik.")
        
        try:
            # Mengubah teks prompt menjadi format URL yang aman
            prompt_aman = urllib.parse.quote(master_prompt_teks)
            
            # Memanggil API Generator Gambar Gratis dari Pollinations (Model Flux/Stable Diffusion)
            url_api = f"https://image.pollinations.ai/p/{prompt_aman}?width=1024&height=1024&nologo=true&seed=42"
            
            # Mengambil data gambar dari server gratis
            respons = requests.get(url_api)
            
            if respons.status_code == 200:
                # Menampilkan hasil gambar langsung ke layar
                st.image(respons.content, caption=f"Hasil Gambar Gratis: {judul_produk}", width=300)
                st.success("Berhasil! Gambar siap digunakan tanpa biaya. (Klik Kanan -> Save Image As).")
            else:
                st.error("Gagal mengambil gambar dari server gratis. Coba klik tombol kembali.")
                
        except Exception as e:
            st.error(f"Terjadi kendala sistem: {e}")
