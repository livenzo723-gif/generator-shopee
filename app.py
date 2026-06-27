import streamlit as st

# Mengatur tampilan halaman
st.set_page_config(page_title="Generator Gambar Shopee", page_icon="🛍️")

st.title("🛍️ Generator Thumbnail Shopee 8K")
st.write("Aplikasi AI untuk menyulap judul & deskripsi menjadi foto produk estetik dan profesional.")

# Kolom rahasia di samping untuk memasukkan "Kunci Akses" (API Key) nanti
with st.sidebar:
    st.header("Pengaturan AI")
    api_key = st.text_input("Masukkan Google API Key", type="password")
    st.info("Kunci ini akan kita dapatkan di langkah selanjutnya.")

# Area Input untuk Anda jualan
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
        # INI ADALAH MASTER PROMPT RAHASIA ANDA (Tidak perlu diketik ulang lagi)
        master_prompt = f"""
        Edit foto produk menjadi thumbnail Shopee yang estetik, profesional, realistis, dan sangat menjual.
        
        DATA PRODUK:
        - Judul: [{judul_produk}]
        - Detail: {deskripsi_produk}
        
        INSTRUKSI VISUAL:
        Fokus utama adalah produk terlihat lebih nyata, tajam, bersih, detail, presisi, dan menonjol. Produk harus menjadi pusat perhatian, terlihat premium, dan meyakinkan. Jangan mengubah bentuk asli, warna, ukuran, atau detail fisik produk.
        
        Background: clean, modern, cerah, estetik. Pencahayaan studio lembut namun tegas, ada bayangan halus di bawah produk.
        Teks Promosi: "BEST QUALITY" atau "READY STOCK" dengan font modern tanpa menutupi produk utama.
        Watermark: Transparan bertuliskan "NAURA ULFA" di bagian tengah produk, tipis dan elegan.
        
        KUALITAS AKHIR: Rasio 1:1. Resolusi HIGH RESOLUTION minimal 2K (target kualitas 8K). Sangat tajam, tidak pecah, dan terlihat seperti foto produk studio premium.
        """
        
        st.success("Teks berhasil dirakit oleh sistem!")
        st.info("Ini adalah prompt panjang yang akan dikirim otomatis ke AI Google (tersembunyi dari pembeli):")
        st.code(master_prompt)
        st.write("*(Catatan: Gambar akan muncul di sini setelah kita menghubungkan Kunci API Google di tahap akhir!)*")
