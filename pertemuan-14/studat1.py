import streamlit as st
# Mengimport class backend dari file studat2.py
from studat2 import SistemParkirBackend

# 1. Konfigurasi Halaman
st.set_page_config(page_title="Sistem Antrean Parkir Gacoan", page_icon="🚗", layout="wide")

# 2. Inisialisasi Backend ke dalam Session State Streamlit
if 'backend' not in st.session_state:
    st.session_state.backend = SistemParkirBackend()

# Mempersingkat pemanggilan object backend
parkir_engine = st.session_state.backend

# 3. SIDEBAR (Samping Kiri) - Menampilkan Antrean Saat Ini
with st.sidebar:
    st.header("📋 Antrean Saat Ini")
    daftar_antrean = parkir_engine.antrean_parkir
    
    if not daftar_antrean:
        st.write("Area parkir masih kosong euy.")
    else:
        for index, mbl in enumerate(daftar_antrean):
            st.info(f"**Antrean ke-{index + 1}**\n\n🚗 {mbl['Plat']} ({mbl['Jenis']})\n\n🕒 {mbl['Waktu']}")
            st.divider()

# 4. MAIN CONTENT (Tengah)
st.title("🚗 Kontrol Sistem Parkir Gacoan")

col_input, col_control = st.columns(2)

# --- Kolom Masuk ---
with col_input:
    st.subheader("📥 Masuk Antrean")
    with st.form("form_masuk", clear_on_submit=True):
        plat = st.text_input("Nomor Plat Kendaraan").upper() # Otomatis jadikan huruf kapital
        jenis = st.selectbox("Jenis", ["Mobil", "Motor"])
        submit = st.form_submit_button("Daftarkan Kendaraan")
        
        if submit:
            if plat.strip() == "":
                st.warning("Plat nomor tidak boleh kosong!")
            else:
                # Memanggil fungsi tambah kendaraan dari backend
                sukses, pesan = parkir_engine.tambah_kendaraan(plat, jenis)
                if sukses:
                    st.success(pesan)
                    st.rerun()
                else:
                    st.warning(pesan)

# --- Kolom Kontrol Keluar (Fitur Pilih Mobil) ---
with col_control:
    st.subheader("🏁 Kontrol Pintu Keluar")
    daftar_antrean = parkir_engine.antrean_parkir
    
    if daftar_antrean:
        st.write("Pilih kendaraan yang ingin dikeluarkan:")
        
        # Membuat opsi tampilan teks untuk selectbox
        pilihan_teks = [f"{mbl['Plat']} ({mbl['Jenis']})" for mbl in daftar_antrean]
        
        # Dropdown memilih berdasarkan indeks elemen list
        pilihan_terpilih = st.selectbox(
            "Daftar Kendaraan di Dalam", 
            options=range(len(pilihan_teks)), 
            format_func=lambda x: pilihan_teks[x]
        )
        
        kendaraan_pilihan = daftar_antrean[pilihan_terpilih]
        st.error(f"👉 Kendaraan Terpilih: {kendaraan_pilihan['Plat']} ({kendaraan_pilihan['Jenis']})")
        
        if st.button("Keluarkan Kendaraan Sekarang", use_container_width=True):
            # Memanggil fungsi hapus dari backend menggunakan indeks terpilih
            sukses, hasil = parkir_engine.keluarkan_kendaraan_by_index(pilihan_terpilih)
            if sukses:
                st.rerun()
    else:
        st.write("Tidak ada kendaraan untuk dikeluarkan.")

st.divider()

# 5. RIWAYAT (Bawah)
st.subheader("🕒 Riwayat Keluar")
if parkir_engine.log_keluar:
    # Menggunakan st.dataframe agar visualisasi tabel bawaan streamlit lebih interaktif
    st.dataframe(parkir_engine.log_keluar, use_container_width=True)