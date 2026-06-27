import streamlit as st

# Mengatur tampilan halaman agar rapi
st.set_page_config(page_title="Generator Prompt Shopee", page_icon="📝", layout="centered")

st.title("🛍️ Generator Prompt Thumbnail Shopee")
st.write("Masukkan judul dan detail produk untuk merakit teks prompt berkualitas tinggi secara otomatis.")

# Area Input Teks
st.subheader("Data Produk Baru")
judul_produk = st.text_input("Judul Produk", placeholder="Contoh: Kapasitor Bulat Kabel Kapasitor Pompa Air 6uf...")
deskripsi_produk = st.text_area("Deskripsi / Detail Produk", placeholder="Contoh:\nHarga per 1 biji\nTersedia ukuran 6uf, 8uf, dan 10uf\n450v\nBrand Lazaro")

st.write("---")

# Tombol Eksekusi
if st.button("Rakit Teks Prompt", type="primary"):
    if not judul_produk:
        st.warning("Mohon isi Judul Produk terlebih dahulu.")
    else:
        # SUSUNAN PROMPT BARU ANDA SECARA UTUH
        master_prompt_teks = f"""Edit foto produk pada Gambar 1 menjadi thumbnail Shopee yang estetik, profesional, realistis, dan sangat menjual, dengan menggunakan Gambar 2 sebagai referensi konsep utama. Samakan gaya visual, nuansa desain, warna background, pencahayaan, dan komposisinya agar hasil akhir semirip mungkin dengan Gambar 2.

1. Fokus Produk & Sudut Pandang (Angle):
Buat objek produk terlihat lebih nyata, tajam, bersih, detail, presisi, dan menonjol. Ubah sedikit sudut pandang (angle) produk agar tidak persis sama dengan foto asli pada Gambar 1. Buat angle-nya sedikit lebih dinamis (misalnya agak dimiringkan, diputar sedikit, atau diambil dari sudut sedikit menyamping) agar dimensi produk lebih terlihat jelas dan menarik. Meskipun angle diubah, JANGAN mengubah bentuk asli produk, warna asli produk, ukuran proporsional, jumlah kabel, tulisan pada label, maupun detail fisik lainnya. Produk harus menjadi pusat perhatian, terlihat premium, dan meyakinkan.

2. Background & Pencahayaan:
Gunakan background yang clean, modern, cerah, estetik, dan mewah seperti konsep Gambar 2. Terapkan pencahayaan studio (studio lighting) yang lembut namun tegas. Tambahkan bayangan halus (drop shadow) di bawah produk agar terlihat memiliki kedalaman, tidak melayang, dan lebih hidup. Tingkatkan tekstur dan ketajaman agar menyerupai foto studio berkualitas tinggi.

3. Komposisi & Tata Letak:
Buat komposisi yang rapi di mana produk menjadi elemen paling dominan dan berukuran cukup besar di tengah area desain. Elemen visual pendukung boleh ditambahkan secukupnya namun jangan terlalu ramai. Pastikan hasil akhir tetap clean, elegan, dan fokus utama tetap pada produk.

4. Teks Promosi & Watermark:
Tambahkan teks promosi singkat: “BEST QUALITY” dan “READY STOCK”. Gunakan font modern yang mudah dibaca, warna disesuaikan dengan konsep Gambar 2, dan letakkan di posisi yang tepat tanpa menutupi produk utama.
Tambahkan watermark transparan bertuliskan “NAURA ULFA” tepat di area tengah (center) produk. Buat tipis, elegan, dan semi-transparan (opacity rendah) agar menyatu dengan desain. Watermark tidak boleh merusak tampilan produk, namun tetap cukup terbaca sebagai penanda kepemilikan.

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
Hasil yang buram, pecah, gelap, terlalu ramai, warna berlebihan, bentuk/anatomi produk yang berubah atau terdistorsi, desain terlihat murahan, atau tampilan yang terlalu terlihat seperti gambar kartun/render AI yang tidak realistis."""

        st.success("Teks prompt baru berhasil dirakit! Silakan salin kotak di bawah ini:")
        
        # Menampilkan hasil dalam kotak kode agar ada tombol "Click to Copy" otomatis dari Streamlit
        st.code(master_prompt_teks, language="text")
