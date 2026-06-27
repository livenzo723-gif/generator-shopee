import streamlit as st

# Mengatur tampilan halaman agar rapi
st.set_page_config(page_title="Generator Prompt Shopee", page_icon="📝", layout="centered")

st.title("🛍️ Generator Prompt Thumbnail Shopee")
st.write("Masukkan judul dan detail produk untuk merakit teks prompt berkualitas tinggi secara otomatis.")

# Area Input Teks (Sangat bersih, tanpa menu upload foto, tanpa API Key)
st.subheader("Data Produk Baru")
judul_produk = st.text_input("Judul Produk", placeholder="Contoh: Relay Ptc Overload Kulkas Polytron 1 pintu")
deskripsi_produk = st.text_area("Deskripsi / Detail Produk", placeholder="Contoh:\nRelay Overload Compresor kulkas Polytron\nModel kulkas 1 pintu\n1 SET")

st.write("---")

# Tombol Eksekusi
if st.button("Rakit Teks Prompt", type="primary"):
    if not judul_produk:
        st.warning("Mohon isi Judul Produk terlebih dahulu.")
    else:
        # SUSUNAN PROMPT SUKSES ANDA SECARA UTUH
        master_prompt_teks = f"""Edit foto produk pada Gambar 1 menjadi thumbnail Shopee yang estetik, profesional, realistis, dan sangat menjual. Gunakan Gambar 2 sebagai referensi konsep utama. Samakan gaya visual, nuansa desain, warna background, pencahayaan, komposisi, dan tata letak agar hasil akhir seragam dan semirip mungkin dengan konsep pada Gambar 2.

Fokus utama adalah produk pada Gambar 1. Buat objek produk terlihat lebih nyata, tajam, bersih, detail, presisi, dan lebih menonjol. Produk harus menjadi pusat perhatian, terlihat premium, rapi, dan meyakinkan untuk pembeli Shopee. Jangan mengubah bentuk asli produk, warna asli produk, ukuran proporsional, jumlah kabel, lubang baut, maupun detail fisik lainnya. Pertahankan keaslian produk agar tetap realistis dan sesuai barang asli.

Buat tampilan thumbnail menjadi lebih mewah dan profesional dengan background seperti konsep pada Gambar 2: clean, modern, cerah, estetik, dan cocok untuk marketplace. Gunakan pencahayaan studio yang lembut namun tegas, tambahkan bayangan halus di bawah produk agar terlihat berdimensi, tidak melayang, dan lebih hidup. Tingkatkan tekstur, ketajaman, dan detail produk agar terlihat seperti foto studio berkualitas tinggi.

Buat komposisi yang rapi dan menarik untuk thumbnail Shopee. Produk harus dibuat lebih dominan, lebih besar, dan lebih menonjol di area utama desain. Elemen visual pendukung boleh ditambahkan secukupnya tetapi jangan terlalu ramai. Pastikan hasil akhir tetap clean, elegan, dan fokus pada produk.

Tambahkan teks promosi yang singkat, tegas, dan menarik, dengan font modern yang mudah dibaca, tanpa menutupi produk utama. Sesuaikan warna teks dengan konsep desain pada Gambar 2. Teks promosi yang bisa ditampilkan:
- “BEST QUALITY”
- “READY STOCK”

Tambahkan watermark transparan bertuliskan “NAURA ULFA” tepat di bagian tengah produk. Watermark harus tetap jelas terbaca, tetapi dibuat tipis, elegan, dan menyatu dengan desain. Gunakan opacity rendah / semi transparan agar tidak merusak tampilan utama produk, namun tetap cukup terlihat sebagai penanda. Posisi watermark harus berada di center produk.

Judul produk:
[{judul_produk}]

Detail produk:
{deskripsi_produk}

Hasil akhir harus berupa thumbnail Shopee rasio 1:1, sangat tajam, realistis, estetik, profesional, dan sangat menarik secara visual. Pastikan kualitas gambar HIGH RESOLUTION dengan minimal 2K (minimal 2048 x 2048), detail sangat jelas, bersih, tidak pecah, tidak blur, dan terlihat seperti foto produk premium untuk kebutuhan jualan online.

Hindari hasil yang buram, pecah, gelap, terlalu ramai, warna berlebihan, produk berubah bentuk, desain murahan, atau tampilan yang terlihat seperti gambar kartun/AI yang tidak realistis."""

        st.success("Teks prompt berhasil dirakit! Silakan salin kotak di bawah ini:")
        
        # Menampilkan hasil dalam kotak kode agar ada tombol "Click to Copy" otomatis dari Streamlit
        st.code(master_prompt_teks, language="text")
