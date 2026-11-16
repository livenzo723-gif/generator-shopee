import streamlit as st

# Mengatur tampilan halaman agar rapi
st.set_page_config(page_title="Generator Prompt Shopee", page_icon="📝", layout="wide")

st.title("🛍️ Generator Prompt Thumbnail (Arsitektur 3 Gambar)")
st.write("Masukkan data produk, atur efek, dan tentukan detail ide kompetitor untuk merakit teks prompt otomatis.")

# --- FITUR RIWAYAT WATERMARK ---
if 'riwayat_watermark' not in st.session_state:
    st.session_state['riwayat_watermark'] = ["NAURA ULFA"]

st.write("---")

# Bagian 1: Pengaturan Watermark Toko
st.subheader("1. Pengaturan Watermark Toko")
opsi_watermark = st.radio(
    "Apakah Anda ingin menambahkan watermark teks buatan AI pada gambar?",
    options=[
        "Pakai watermark teks transparan", 
        "Tanpa watermark"
    ]
)

pakai_watermark = opsi_watermark == "Pakai watermark teks transparan"
watermark_final = ""
if pakai_watermark:
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

# Bagian 3: Analisis Gambar 2
st.subheader("3. Analisis Gambar 2 (Foto Kompetitor)")
st.caption("Boleh dikosongkan. AI akan menganalisis Gambar 2 dan memilih detail visual yang cocok untuk produk Anda.")
ide_gambar2 = st.text_area(
    "Catatan khusus untuk AI (opsional)",
    placeholder="Contoh: Utamakan cara foto menonjolkan tekstur produk."
).strip()

instruksi_gambar2 = (
    "Analisis GAMBAR 2 dan pilih sendiri detail visual yang membantu pembeli memahami produk, "
    "misalnya bagian yang ditonjolkan, cara menata produk, atau cara memperlihatkan tekstur. "
    "Gunakan hanya ide yang sesuai dengan produk di GAMBAR 1 dan pilihan angle. "
    "Gunakan data produk yang diberikan untuk klaim ukuran, spesifikasi, dan kompatibilitas. "
    "Jangan menyalin logo, watermark, teks promosi, atau komponen fisik dari foto kompetitor."
)
if ide_gambar2:
    instruksi_gambar2 += f'\nPertimbangkan catatan pengguna saat memilih detail: "{ide_gambar2}"'

st.write("---")

# Bagian 4: Efek Visual Tambahan
st.subheader("4. Efek Visual Tambahan (Opsional)")
pilihan_efek = st.multiselect(
    "Centang efek estetika untuk background foto (bisa pilih lebih dari satu):",
    options=[
        "Asap putih tipis (wispy white smoke)",
        "Pantulan kaca/air di bawah produk (Glossy reflection)",
        "Cahaya neon halus (Subtle neon glow)",
        "Percikan air segar (Water splashes)",
        "Bayangan daun estetik (Aesthetic leaf shadow/Gobo)"
    ]
)

efek_manual = st.text_input("Atau ketik manual efek lainnya:", placeholder="Contoh: Taburan serpihan emas di udara...")

semua_efek = pilihan_efek.copy()
if efek_manual.strip() != "":
    semua_efek.append(efek_manual.strip())

teks_efek_tambahan = ""
if len(semua_efek) > 0:
    gabungan_efek = ", ".join(semua_efek)
    teks_efek_tambahan = f"\n\nEFEK VISUAL TAMBAHAN:\nTambahkan elemen estetika berupa: {gabungan_efek}. Aplikasikan efek ini pada area background atau di sekitar produk secara halus, proporsional, dan elegan. Efek ini berfungsi untuk mempercantik suasana (mood) foto TANPA menutupi, mendistraksi, atau merusak detail fisik dari produk utama."

st.write("---")

# Bagian 5: Opsi Sudut Pandang (Angle)
st.subheader("5. Opsi Sudut Pandang (Angle) Produk")
pilihan_angle = st.radio(
    "Pilih perlakuan angle untuk produk Anda:",
    options=[
        "A. Gunakan Angle Asli (Paling Aman, anti berubah bentuk)", 
        "B. Ubah Angle Dinamis (Beresiko, cocok untuk bentuk sederhana)"
    ]
)

if "Gunakan Angle Asli" in pilihan_angle:
    teks_angle_instruksi = "Pertahankan sudut pandang (angle) produk PERSIS SAMA seperti pada Gambar 1. JANGAN memutar, memiringkan, atau mengubah perspektif produk sedikit pun untuk menghindari distorsi bentuk."
else:
    teks_angle_instruksi = "Ubah sedikit sudut pandang (angle) produk agar lebih dinamis (misalnya agak dimiringkan atau diputar sedikit) dengan mengikuti tata letak dari Gambar 2. PERINGATAN KERAS: Saat mengubah angle, Anda WAJIB mempertahankan geometri 3D, anatomi, dan bentuk asli produk secara mutlak seperti pada Gambar 1. JANGAN menambah atau mengurangi komponen fisik apa pun. Jika perubahan angle memicu distorsi bentuk, prioritaskan keaslian bentuk daripada angle."

st.write("---")

# Bagian 6: Pilihan Jenis Prompt
st.subheader("6. Pilih Jenis Prompt")
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
    # Validasi input
    if pakai_watermark and not watermark_final:
        st.warning("Mohon isi Nama Watermark terlebih dahulu.")
    elif not judul_produk:
        st.warning("Mohon isi Judul Produk terlebih dahulu.")
    else:
        # Menyimpan nama baru ke riwayat secara otomatis jika menggunakan watermark
        if pakai_watermark and watermark_final not in st.session_state['riwayat_watermark']:
            st.session_state['riwayat_watermark'].append(watermark_final)
            
        # --- PERSIAPAN LOGIKA WATERMARK ---
        if pakai_watermark:
            teks_watermark_prompt1 = f"""4. Watermark:
Tambahkan watermark transparan bertuliskan “{watermark_final}” tepat di area tengah (center) produk. Buat tipis, elegan, dan semi-transparan (opacity rendah) agar menyatu dengan desain. Watermark tidak boleh merusak tampilan produk, namun tetap cukup terbaca sebagai penanda kepemilikan."""
            
            teks_watermark_prompt2 = f"""Tambahkan watermark transparan bertuliskan “{watermark_final}” secara tipis dan elegan di area tengah produk. Watermark harus menyatu dengan desain, tetap terlihat, tetapi tidak mengganggu detail produk."""
        else:
            teks_watermark_prompt1 = """4. Watermark:
Hasilkan gambar tanpa watermark tambahan di area mana pun. Pertahankan logo atau label fisik yang memang ada pada produk di GAMBAR 1."""
            
            teks_watermark_prompt2 = """Hasilkan gambar tanpa watermark tambahan di area mana pun. Pertahankan logo atau label fisik yang memang ada pada produk di GAMBAR 1."""

        # --- PERAKITAN PROMPT ---
        if "1. Thumbnail Utama" in jenis_prompt:
            master_prompt_teks = f"""Edit foto produk menjadi thumbnail Shopee yang estetik, profesional, realistis, dan sangat menjual dengan aturan 3 Gambar berikut:
- GAMBAR 1 (BAHAN FISIK): Jadikan referensi mutlak untuk anatomi, bentuk, dan detail fisik produk.
- GAMBAR 2 (IDE KOMPOSISI & REFERENSI DETAIL): Jadikan referensi untuk tata letak (layout) dan mengambil detail spesifik tertentu.
- GAMBAR 3 (DNA TOKO): Jadikan referensi mutlak untuk gaya visual, nuansa desain, warna background, dan pencahayaan.

1. Fokus Produk, Sudut Pandang (Angle), & Peningkatan Detail Warna Hitam:
Buat objek produk (dari Gambar 1) terlihat lebih nyata, tajam, bersih, detail, presisi, dan menonjol. {teks_angle_instruksi} PENTING: Khusus untuk produk atau bagian produk yang berwarna HITAM, tingkatkan kecerahan (brightness/exposure) dan perjelas detail teksturnya agar lekukan, bentuk, dan materialnya terlihat sangat cerah, jelas, dan tidak gelap/tenggelam. JANGAN mengubah bentuk asli produk, ukuran proporsional, jumlah kabel, tulisan pada label, maupun detail fisik lainnya dari Gambar 1.

2. Background, Pencahayaan & Efek:
Gunakan background yang clean, modern, cerah, estetik, dan mewah dengan mengikuti warna dan nuansa GAMBAR 3 dengan pembagian warna panggung sesuai Bagian 8. Terapkan pencahayaan studio (studio lighting) yang lembut namun tegas, dengan fill light tambahan yang mengarah ke area produk yang berwarna gelap/hitam. Tambahkan bayangan halus (drop shadow) di bawah produk agar terlihat memiliki kedalaman, tidak melayang, dan lebih hidup.{teks_efek_tambahan}

3. Komposisi & Penerapan Ide Spesifik dari Gambar 2:
Gunakan GAMBAR 2 sebagai referensi komposisi dengan tata letak akhir mengikuti Bagian 8. {instruksi_gambar2}
Terapkan ide tersebut dengan rapi, realistis, dan logis pada produk utama. Pastikan hasil akhir tetap clean, elegan, dan fokus utama tetap pada produk.

{teks_watermark_prompt1}

5. Referensi Teks Produk untuk judul dan panel informasi:
Judul: 
[{judul_produk}]
Spesifikasi: 
{deskripsi_produk}

6. Spesifikasi Output Akhir:
Rasio: 1:1 (Square, standar thumbnail e-commerce).
Resolusi: High Resolution minimal 2K (2048 x 2048 px).
Kualitas: Sangat tajam, realistis, detail sangat jelas, bersih, tidak pecah, dan tidak blur.

7. HINDARI (Negative Prompt):
Hasil yang buram, pecah, gelap, produk berwarna hitam yang detailnya mati/hilang karena kurang cahaya, terlalu ramai, warna berlebihan, bentuk/anatomi produk yang berubah atau terdistorsi, desain terlihat murahan, atau tampilan yang terlalu terlihat seperti gambar kartun/render AI yang tidak realistis.

8. INSTRUKSI SPESIFIKASI TATA LETAK & GAYA VISUAL TAMBAHAN (PRIORITAS EKSEKUSI):

Terapkan tata letak e-commerce profesional yang rapi, bersih, dan terorganisir dengan pembagian area visual berikut. Gunakan bagian ini sebagai acuan utama untuk posisi judul, produk, badge, dan panel bawah. Pertahankan bentuk asli produk dari Gambar 1 serta pilihan angle yang sudah ditetapkan.

- Latar Belakang & Panggung Produk: Gunakan latar belakang bagian atas sesuai warna DNA toko (Gambar 3), dengan gradasi studio halus yang menyatu dengan permukaan lantai atau meja berwarna netral terang (krem muda atau putih hangat) di bagian tengah hingga bawah. Posisikan produk utama dari Gambar 1 di area tengah dengan bayangan kontak yang halus dan realistis di atas permukaan panggung.

- Pojok Kiri Atas (Branding): Tempatkan tab putih bersudut melengkung yang menyatu dengan tepi atas dan kiri. Gunakan logo atau identitas toko yang terlihat pada Gambar 3.

- Bagian Atas (Judul Utama): Tampilkan judul sesuai nama produk pada Referensi Teks. Gunakan huruf sans-serif ekstra tebal berwarna putih dengan garis tepi hitam tebal dan bayangan halus agar judul mudah dibaca.

- Area Kanan Tengah (Badge Informasi): Susun dua badge berbentuk kapsul secara vertikal di ruang kosong sebelah kanan produk. Gunakan latar putih, garis tepi hitam atau biru gelap, dan teks tebal berwarna gelap. Isi badge atas dengan “BEST QUALITY” atau “ISI 1 PCS” jika produk memang dijual satuan. Isi badge bawah dengan “READY STOCK!”. Sisakan jarak agar badge tidak menutupi produk.

- Bagian Bawah (Panel Kompatibilitas / Spesifikasi): Buat panel horizontal putih bersudut membulat dengan garis tepi hitam atau biru gelap. Bagi panel menjadi dua kolom dengan satu garis vertikal tipis.
  * Kolom kiri: Tampilkan foto atau ilustrasi perangkat yang kompatibel secara berdampingan, tajam, dan proporsional. Gunakan Gambar 2 sebagai referensi visual perangkat.
