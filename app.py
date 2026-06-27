import streamlit as st

# Mengatur tampilan halaman agar rapi
st.set_page_config(page_title="Generator Prompt Shopee", page_icon="📝", layout="centered")

st.title("🛍️ Generator Prompt Thumbnail Shopee")
st.write("Masukkan data produk dan atur watermark toko untuk merakit teks prompt berkualitas tinggi secara otomatis.")

# --- FITUR RIWAYAT WATERMARK ---
if 'riwayat_watermark' not in st.session_state:
    st.session_state['riwayat_watermark'] = ["NAURA ULFA"]

st.write("---")

# Bagian 1: Pengaturan Watermark Toko
st.subheader("1. Pengaturan Watermark Toko")

pilihan_sejarah = st.selectbox(
    "Pilih dari Riwayat (Opsional):",
    options=["(Ketik Baru)"] + st.session_state['riwayat_watermark']
)

if pilihan_sejarah == "(Ketik Baru)":
    watermark_final = st.text_input("Nama Watermark:", placeholder="Ketik nama toko di sini...")
else:
    watermark_final = st.text_input("Nama Watermark:", value=pilihan_sejarah)

st.write("---")

# Bagian 2: Data Produk Baru
st.subheader("2. Data Produk Baru")
judul_produk = st.text_input("Judul Produk", placeholder="Contoh: Kapasitor Bulat Kabel Kapasitor Pompa Air 6uf...")
deskripsi_produk = st.text_area("Deskripsi / Detail Produk", placeholder="Contoh:\nHarga per 1 biji\nTersedia ukuran 6uf, 8uf, dan 10uf\n450v\nBrand Lazaro")

st.write("---")

# Bagian 3: Efek Visual Tambahan
st.subheader("3. Efek Visual Tambahan (Opsional)")
pilihan_efek = st.selectbox(
    "Pilih efek estetika untuk background foto:",
    options=[
        "Tanpa Efek (Polos/Clean)",
        "Asap putih tipis (wispy white smoke)",
        "Pantulan kaca/air di bawah produk (Glossy reflection)",
        "Cahaya neon halus (Subtle neon glow)",
        "Percikan air segar (Water splashes)",
        "Bayangan daun estetik (Aesthetic leaf shadow/Gobo)",
        "(Ketik Manual Efek Lainnya...)"
    ]
)

if pilihan_efek == "(Ketik Manual Efek Lainnya...)":
    efek_final = st.text_input("Ketik efek visual yang diinginkan:", placeholder="Contoh: Taburan serpihan emas di udara...")
else:
    efek_final = pilihan_efek

# Merakit kalimat efek khusus jika pengguna memilih efek
teks_efek_tambahan = ""
if efek_final != "Tanpa Efek (Polos/Clean)" and efek_final.strip() != "":
    teks_efek_tambahan = f"\nEFEK VISUAL TAMBAHAN:\nTambahkan elemen estetika berupa '{efek_final}'. Aplikasikan efek ini pada area background atau di sekitar produk secara halus, proporsional, dan elegan. Efek ini berfungsi untuk mempercantik suasana (mood) foto TANPA menutupi, mendistraksi, atau merusak detail fisik dari produk utama."

st.write("---")

# Bagian 4: Pilihan Jenis Prompt
st.subheader("4. Pilih Jenis Prompt")
jenis_prompt = st.radio(
    "Mau merakit prompt untuk gambar yang mana?",
    options=[
        "1. Thumbnail Utama (Sudut pandang dinamis & referensi konsep)", 
        "2. Foto Detail Pendukung (Close-up & fokus tekstur)"
    ]
)

st.write("---")

# Tombol Eksekusi
if st.button("Rakit Teks Prompt", type="primary"):
    if not watermark_final:
        st.warning("Mohon isi Nama Watermark terlebih dahulu.")
    elif not judul_produk:
        st.warning("Mohon isi Judul Produk terlebih dahulu.")
    else:
        # Menyimpan nama baru ke riwayat secara otomatis
        if watermark_final not in st.session_state['riwayat_watermark']:
            st.session_state['riwayat_watermark'].append(watermark_final)
            
        if "1. Thumbnail Utama" in jenis_prompt:
            # --- PROMPT 1: THUMBNAIL UTAMA ---
            master_prompt_teks = f"""Edit foto produk pada Gambar 1 menjadi thumbnail Shopee yang estetik, profesional, realistis, dan sangat menjual, dengan menggunakan Gambar 2 sebagai referensi konsep utama. Samakan gaya visual, nuansa desain, warna background, pencahayaan, dan komposisinya agar hasil akhir semirip mungkin dengan Gambar 2.

1. Fokus Produk & Sudut Pandang (Angle):
Buat objek produk terlihat lebih nyata, tajam, bersih, detail, presisi, dan menonjol. Ubah sedikit sudut pandang (angle) produk agar tidak persis sama dengan foto asli pada Gambar 1. Buat angle-nya sedikit lebih dinamis (misalnya agak dimiringkan, diputar sedikit, atau diambil dari sudut sedikit menyamping) agar dimensi produk lebih terlihat jelas dan menarik. Meskipun angle diubah, JANGAN mengubah bentuk asli produk, warna asli produk, ukuran proporsional, jumlah kabel, tulisan pada label, maupun detail fisik lainnya. Produk harus menjadi pusat perhatian, terlihat premium, dan meyakinkan.

2. Background, Pencahayaan & Efek:
Gunakan background yang clean, modern, cerah, estetik, dan mewah seperti konsep Gambar 2. Terapkan pencahayaan studio (studio lighting) yang lembut namun tegas. Tambahkan bayangan halus (drop shadow) di bawah produk agar terlihat memiliki kedalaman, tidak melayang, dan lebih hidup. Tingkatkan tekstur dan ketajaman agar menyerupai foto studio berkualitas tinggi.{teks_efek_tambahan}

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
Hasil yang buram, pecah, gelap, terlalu ramai, warna berlebihan, bentuk/anatomi produk yang berubah atau terdistorsi, desain terlihat murahan, atau tampilan yang terlalu terlihat seperti gambar kartun/render AI yang tidak realistis."""

        else:
            # --- PROMPT 2: FOTO DETAIL PENDUKUNG ---
            master_prompt_teks = f"""Edit foto produk menjadi foto pendukung detail produk untuk Shopee yang realistis, tajam, profesional, bersih, dan tetap satu konsep dengan hasil thumbnail utama sebelumnya.

Gunakan hasil thumbnail utama sebagai referensi gaya visual, termasuk background clean, tone warna modern, pencahayaan studio, bayangan halus, dan tampilan premium. Foto ini harus terlihat masih satu paket dengan foto utama, tetapi fokusnya lebih dekat ke detail produk.

Tonjolkan bagian penting produk secara jelas dan realistis, seperti kabel, lubang baut, as, konektor, gear, body produk, tekstur material, atau bagian lain yang menjadi nilai jual produk. Buat detail produk terlihat tajam, bersih, dan meyakinkan untuk pembeli.

Jangan mengubah bentuk asli produk, warna asli produk, jumlah kabel, posisi lubang baut, ukuran proporsional, panjang as, konektor, maupun detail fisik lainnya. Semua bagian produk harus tetap realistis dan sesuai barang asli.

Gunakan angle close-up yang informatif. Produk boleh ditampilkan lebih dekat, tetapi jangan sampai terlalu terpotong berlebihan. Pastikan bagian detail utama terlihat jelas, rapi, dan mudah dipahami pembeli.

Komposisi harus tetap clean, modern, dan tidak ramai. Background harus serasi dengan hasil thumbnail utama agar seluruh foto produk terlihat profesional dan konsisten dalam satu etalase Shopee. Gunakan pencahayaan studio yang lembut namun tegas untuk memperjelas tekstur dan bentuk produk.{teks_efek_tambahan}

Jika perlu, tambahkan teks kecil sebagai penjelas detail, seperti:
“{judul_produk}”

Teks harus kecil, rapi, modern, tidak menutupi bagian penting produk, dan tetap selaras dengan desain.

Tambahkan watermark transparan bertuliskan “{watermark_final}” secara tipis dan elegan. Watermark harus menyatu dengan desain, tetap terlihat, tetapi tidak mengganggu detail produk.

Detail yang ingin ditonjolkan:
{judul_produk}
{deskripsi_produk}

Hasil akhir harus berupa foto pendukung produk Shopee rasio 1:1, high resolution minimal 2K, sangat tajam, realistis, bersih, tidak blur, tidak pecah, dan cocok sebagai foto kedua, ketiga, atau seterusnya di etalase Shopee.

Hindari hasil yang buram, terlalu gelap, terlalu ramai, warna berlebihan, bentuk produk berubah, detail produk hilang, teks menutupi produk, atau tampilan yang terlihat seperti gambar kartun/AI tidak realistis."""

        st.success(f"Teks prompt berhasil dirakit! Silakan salin di bawah ini:")
        st.code(master_prompt_teks, language="text")
