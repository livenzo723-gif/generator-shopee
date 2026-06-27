import streamlit as st
from google import genai
from google.genai import types
from PIL import Image

# Mengatur tampilan halaman
st.set_page_config(page_title="Generator Gambar Shopee", page_icon="🛍️", layout="wide")

st.title("🛍️ Generator Thumbnail Shopee 8K")
st.write("Aplikasi AI Multimodal: Otomatisasi pembuatan foto produk premium sesuai standar sukses Anda.")

# Kolom di samping untuk Kunci Akses (API Key)
with st.sidebar:
    st.header("Pengaturan AI")
    api_key = st.text_input("Masukkan Google API Key", type="password")
    st.info("Pastikan Billing (Penagihan) Anda sudah aktif di Google AI Studio.")

# Area Input Gambar
st.subheader("1. Upload Gambar Anda")
col1, col2 = st.columns(2)

with col1:
    gambar1_file = st.file_uploader("Upload Gambar 1 (Foto Produk Asli)", type=["jpg", "jpeg", "png", "webp"])
    if gambar1_file:
        img1 = Image.open(gambar1_file)
        st.image(img1, caption="Gambar 1: Produk Asli", use_column_width=True)

with col2:
    gambar2_file = st.file_uploader("Upload Gambar 2 (Referensi Konsep)", type=["jpg", "jpeg", "png", "webp"])
    if gambar2_file:
        img2 = Image.open(gambar2_file)
        st.image(img2, caption="Gambar 2: Referensi Konsep", use_column_width=True)

# Area Input Teks (Otomatis masuk ke dalam susunan prompt sukses Anda)
st.subheader("2. Data Produk Anda")
judul_produk = st.text_input("Judul Produk", placeholder="Contoh: Relay Ptc Overload Kulkas Polytron 1 pintu")
deskripsi_produk = st.text_area("Deskripsi / Detail Produk", placeholder="Contoh:\nRelay Overload Compresor kulkas Polytron\nModel kulkas 1 pintu\nRelay 1 pin kanan + Overloud\n1 SET")

# Tombol Eksekusi
if st.button("Generate Gambar 8K", type="primary"):
    if not api_key:
        st.error("Gagal: Anda belum memasukkan API Key di menu sebelah kiri.")
    elif not gambar1_file or not gambar2_file:
        st.warning("Mohon upload Gambar 1 dan Gambar 2 terlebih dahulu.")
    elif not judul_produk:
        st.warning("Mohon isi Judul Produk terlebih dahulu.")
    else:
        
        # PROMPT UTUH DAN SUKSES ANDA YANG SUDAH DIINTEGRASIKAN KE SISTEM
        master_prompt_teks = f"""
        Edit foto produk pada Gambar 1 menjadi thumbnail Shopee yang estetik, profesional, realistis, dan sangat menjual. Gunakan Gambar 2 sebagai referensi konsep utama. Samakan gaya visual, nuansa desain, warna background, pencahayaan, komposisi, dan tata letak agar hasil akhir seragam dan semirip mungkin dengan konsep pada Gambar 2.

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

        Hindari hasil yang buram, pecah, gelap, terlalu ramai, warna berlebihan, produk berubah bentuk, desain murahan, atau tampilan yang terlihat seperti gambar kartun/AI yang tidak realistis.
        """
        
        st.info("Mengirim instruksi premium ke AI Google... Mohon tunggu sebentar.")
        
        try:
            client = genai.Client(api_key=api_key)
            
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
                    st.image(part.inline_data.data, caption=f"Hasil Premium: {judul_produk}", use_column_width=True)
                    st.success("Berhasil! Gambar berkualitas tinggi siap digunakan. (Klik Kanan -> Save Image As).")
                
        except Exception as e:
            st.error(f"Terjadi kendala saat menghubungi AI: {e}")
