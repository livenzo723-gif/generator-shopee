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

teks_efek_tambahan = ""
if efek_final != "Tanpa Efek (Polos/Clean)" and efek_final.strip() != "":
    teks_efek_tambahan = f"\nEFEK VISUAL TAMBAHAN:\nTambahkan elemen estetika berupa '{efek_final}'. Aplikasikan efek ini pada area background atau di sekitar produk secara halus, proporsional, dan elegan. Efek ini berfungsi untuk mempercantik suasana (mood) foto TANPA menutupi, mendistraksi, atau merusak detail fisik dari produk utama."

st.write("---")

# Bagian 4: Opsi Sudut Pandang (Angle)
st.subheader("4. Opsi Sudut Pandang (Angle) Produk")
pilihan_angle = st.radio(
    "Pilih perlakuan angle untuk produk Anda:",
    options=[
        "A. Gunakan Angle Asli (Paling Aman, anti berubah bentuk)", 
        "B. Ubah Angle Dinamis (Beresiko, cocok untuk bentuk sederhana)"
    ]
)

# Merumuskan teks instruksi angle berdasarkan pilihan
if "Gunakan Angle Asli" in pilihan_angle:
    teks_angle_instruksi = "Pertahankan sudut pandang (angle) PERSIS SAMA seperti foto asli pada Gambar 1. JANGAN memutar, memiringkan, atau mengubah perspektif produk sedikit pun untuk menghindari distorsi bentuk."
else:
    teks_angle_instruksi = "Ubah sedikit sudut pandang (angle) produk agar lebih dinamis (misalnya agak dimiringkan atau diputar sedikit). PERINGATAN KERAS: Saat mengubah angle, Anda WAJIB mempertahankan geometri 3D, anatomi, dan bentuk asli produk secara mutlak. JANGAN menambah atau mengurangi komponen fisik apa pun. Jika perubahan angle memicu distorsi bentuk, prioritaskan keaslian bentuk daripada angle."

st.write("---")

# Bagian 5: Pilihan Jenis Prompt
st.subheader("5. Pilih Jenis Prompt")
jenis_prompt = st.radio(
    "Mau merakit prompt untuk gambar yang mana?",
    options=[
        "1. Thumbnail Utama", 
        "2. Foto Detail Pendukung (Close-up)"
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

1. Fokus Produk, Sudut Pandang (Angle), & Peningkatan Detail Warna Hitam:
Buat objek produk terlihat lebih nyata, tajam, bersih, detail, presisi, dan menonjol. {teks_angle_instruksi} PENTING: Khusus untuk produk atau bagian produk yang berwarna HITAM, tingkatkan kecerahan (brightness/exposure) dan perjelas detail teksturnya agar lekukan, bentuk, dan materialnya terlihat sangat cerah, jelas, dan tidak gelap/tenggelam. JANGAN mengubah bentuk asli produk, ukuran proporsional, jumlah kabel, tulisan pada label, maupun detail fisik lainnya. Produk harus menjadi pusat perhatian, terlihat premium, dan meyakinkan.

2. Background, Pencahayaan & Efek:
Gunakan background yang clean, modern, cerah, estetik, dan mewah seperti konsep Gambar 2. Terapkan pencahayaan studio (studio lighting) yang lembut namun tegas, dengan fill light tambahan yang mengarah ke area produk yang berwarna gelap/hitam. Tambahkan bayangan halus (drop shadow) di bawah produk agar terlihat memiliki kedalaman, tidak melayang, dan lebih hidup. Tingkatkan tekstur dan ketajaman agar menyerupai foto studio berkualitas tinggi.{teks_efek_tambahan}

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
Hasil yang buram, pecah, gelap, produk berwarna hitam yang detailnya mati/hilang karena kurang cahaya, terlalu ramai, warna berlebihan, bentuk/anatomi produk yang berubah atau terdistorsi, desain terlihat murahan, atau tampilan yang terlalu terlihat seperti gambar kartun/render AI yang tidak realistis."""

        else:
            # --- PROMPT 2: FOTO DETAIL PENDUKUNG ---
            master_prompt_teks = f"""Edit foto produk menjadi foto pendukung detail produk untuk Shopee yang realistis, tajam, profesional, bersih, dan tetap satu konsep dengan hasil thumbnail utama sebelumnya.

Gunakan hasil thumbnail utama sebagai referensi gaya visual, termasuk background clean, tone warna modern, pencahayaan studio, bayangan halus, dan tampilan premium. Foto ini harus terlihat masih satu paket dengan foto utama, tetapi fokusnya lebih dekat ke detail produk.

Tonjolkan bagian penting produk secara jelas dan realistis, seperti kabel, lubang baut, as, konektor, gear, body produk, tekstur material, atau bagian lain yang menjadi nilai jual produk. Khusus untuk area berwarna hitam/gelap, tingkatkan kecerahan agar teksturnya tetap terlihat sangat jelas. Buat detail produk terlihat tajam, bersih, dan meyakinkan untuk pembeli.

{teks_angle_instruksi} Gunakan angle close-up yang informatif. Produk boleh ditampilkan lebih dekat, tetapi jangan sampai terlalu terpotong berlebihan. Pastikan bagian detail utama terlihat jelas, rapi, dan mudah dipahami pembeli.

Jangan mengubah bentuk asli produk, warna asli produk, jumlah kabel, posisi lubang baut, ukuran proporsional, panjang as, konektor, maupun detail fisik lainnya. Semua bagian produk harus tetap mutlak realistis dan sesuai barang asli.

Komposisi harus tetap clean, modern, dan tidak ramai. Background harus serasi dengan hasil thumbnail utama agar seluruh foto produk terlihat profesional dan konsisten dalam satu etalase Shopee. Gunakan pencahayaan studio yang lembut namun tegas untuk memperjelas tekstur dan bentuk produk.{teks_efek_tambahan}

Jika perlu, tambahkan teks kecil sebagai penjelas detail, seperti:
“{judul_produk}”

Teks harus kecil, rapi, modern, tidak menutupi bagian penting produk, dan tetap selaras dengan desain.

Tambahkan watermark transparan bertuliskan “{watermark_final}” secara tipis dan elegan. Watermark harus menyatu dengan desain, tetap terlihat, tetapi tidak mengganggu detail produk.

Detail yang ingin ditonjolkan:
{judul_produk}
{deskripsi_produk}

Hasil akhir harus berupa foto pendukung produk Shopee rasio 1:1, high resolution minimal 2K, sangat tajam, realistis, bersih, tidak blur, tidak pecah, dan cocok sebagai foto kedua, ketiga, atau seterusnya di etalase Shopee.

7. HINDARI (Negative Prompt):
Hasil yang buram, pecah, gelap, produk berwarna hitam yang detailnya mati/hilang karena kurang cahaya, terlalu ramai, warna berlebihan, bentuk/anatomi produk yang berubah atau terdistorsi, desain terlihat murahan, atau tampilan yang terlalu terlihat seperti gambar kartun/render AI yang tidak realistis."""

        st.success(f"Teks prompt berhasil dirakit! Silakan salin di bawah ini:")
        st.code(master_prompt_teks, language="text")
