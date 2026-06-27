import streamlit as st

# Mengatur tampilan halaman agar rapi
st.set_page_config(page_title="Generator Prompt Shopee", page_icon="🛍️", layout="centered")

st.title("🛍️ Generator Prompt Thumbnail Shopee")
st.write("Masukkan data produk dan atur watermark toko untuk merakit teks prompt berkualitas tinggi secara otomatis.")

# --- FITUR RIWAYAT WATERMARK ---
# Memastikan tempat penyimpanan riwayat sudah siap di dalam sistem
if 'riwayat_watermark' not in st.session_state:
    st.session_state['riwayat_watermark'] = ["NAURA ULFA"]

st.write("---")

# Bagian 1: Pengaturan Watermark Toko
st.subheader("1. Pengaturan Watermark Toko")

# Dropdown untuk memilih dari sejarah yang sudah ada
pilihan_sejarah = st.selectbox(
    "Pilih dari Sejarah Watermark (atau pilih opsi paling atas untuk ketik manual):",
    options=["+ Ketik Nama Toko Baru secara Manual..."] + st.session_state['riwayat_watermark']
)

# Jika memilih opsi ketik manual, munculkan kolom input teks
if pilihan_sejarah == "+ Ketik Nama Toko Baru secara Manual...":
    watermark_final = st.text_input("Ketik Nama Watermark / Toko Baru:", placeholder="Contoh: TOKO UTAMA JAYA")
else:
    watermark_final = pilihan_sejarah

st.write("---")

# Bagian 2: Data Produk
st.subheader("2. Data Produk Baru")
judul_produk = st.text_input("Judul Produk", placeholder="Contoh: Kapasitor Bulat Kabel Kapasitor Pompa Air 6uf...")
deskripsi_produk = st.text_area("Deskripsi / Detail Produk", placeholder="Contoh:\nHarga per 1 biji\nTersedia ukuran 6uf, 8uf, dan 10uf\n450v\nBrand Lazaro")

st.write("---")

# Tombol Eksekusi
if st.button("Rakit Teks Prompt", type="primary"):
    if not watermark_final:
        st.warning("Mohon isi atau pilih Nama Watermark terlebih dahulu.")
    elif not judul_produk:
        st.warning("Mohon isi Judul Produk terlebih dahulu.")
    else:
        # OTOMATIS MENYIMPAN NAMA BARU KE SEJARAH (Jika belum pernah ada daftar sebelumnya)
        if pilihan_sejarah == "+ Ketik Nama Toko Baru secara Manual..." and watermark_final not in st.session_state['riwayat_watermark']:
            st.session_state['riwayat_watermark'].append(watermark_final)
            
        # SUSUNAN PROMPT PRESTISIUS BARU ANDA SECARA UTUH
        master_prompt_teks = f"""Edit foto produk pada Gambar 1 menjadi thumbnail Shopee yang estetik, profesional, realistis, dan sangat menjual, dengan menggunakan Gambar 2 sebagai referensi konsep utama. Samakan gaya visual, nuansa desain, warna background, pencahayaan, dan komposisinya agar hasil akhir semirip mungkin dengan Gambar 2.

1. Fokus Produk & Sudut Pandang (Angle):
Buat objek produk terlihat lebih nyata, tajam, bersih, detail, presisi, dan menonjol. Ubah sedikit sudut pandang (angle) produk agar tidak persis sama dengan foto asli pada Gambar 1. Buat angle-nya sedikit lebih dinamis (misalnya agak dimiringkan, diputar sedikit, atau diambil dari sudut sedikit menyamping) agar dimensi produk lebih terlihat jelas dan menarik. Meskipun angle diubah, JANGAN mengubah bentuk asli produk, warna asli produk, ukuran proporsional, jumlah kabel, tulisan pada label, maupun detail fisik lainnya. Produk harus menjadi pusat perhatian, terlihat premium, dan meyakinkan.

2. Background & Pencahayaan:
Gunakan background yang clean, modern, cerah, estetik, dan mewah seperti konsep Gambar 2. Terapkan pencahayaan studio (studio lighting) yang lembut namun tegas. Tambahkan bayangan halus (drop shadow) di bawah produk agar terlihat memiliki kedalaman, tidak melayang, dan lebih hidup. Tingkatkan tekstur dan ketajaman agar menyerupai foto studio berkualitas tinggi.

3. Komposisi & Tata Letak:
Buat komposisi yang rapi di mana produk menjadi elemen paling dominan dan berukuran cukup besar di tengah area desain. Elemen visual pendukung boleh ditambahkan secukupnya namun jangan terlalu ramai. Pastikan hasil akhir tetap clean, elegan, dan fokus utama tetap pada produk.

4. Teks Promosi & Watermark:
Tambahkan teks promosi singkat: “BEST QUALITY” dan “READY STOCK”. Gunakan font modern yang mudah dibaca, warna disesuaikan dengan konsep Gambar 2, dan letakkan di posisi yang tepat tanpa menutupi produk utama.
Tambahkan watermark transparan bertuliskan “{watermark_final}” tepat di area tengah (center) produk. Buat tipis, elegan, dan semi-transparan (opacity rendah) agar menyatu dengan desain. Watermark tidak boleh merusak tampilan produk, namun tetap cukup terbaca sebagai penanda kepemilikan.

5. Referensi Teks Produk (Jika ingin dimasukkan ke dalam desain):
Judul:
[{judul_produk}]

Spesifikasi:
{deskripsi_produk}

6. Spesifikasi Output Akhir:
Rasio: 1:1 (Square, standar thumbnail Shopee).
Resolusi: High Resolution minimal 2K (2048 x 2048 px).
Kualitas: Sangat tajam, realistis, detail sangat jelas, bersih, tidak pecah, dan tidak blur.

7. HINDARI (Negative Prompt):
Hasil yang buram, pecah, gelap, terlalu ramai, warna berlebihan, bentuk/anatomi produk yang berubah atau terdistorsi, desain terlihat murahan, atau tampilan yang terlihat seperti gambar kartun/render AI yang tidak realistis."""

        st.success(f"Teks prompt untuk toko '{watermark_final}' berhasil dirakit! Silakan salin di bawah ini:")
        
        # Menampilkan hasil rakitan teks prompt
        st.code(master_prompt_teks, language="text")
