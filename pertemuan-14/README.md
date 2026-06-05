# 🚗 Sistem Antrean Parkir Gacoan

Aplikasi manajemen antrean parkir berbasis web yang dibangun dengan **Streamlit**, dilengkapi fitur pengumuman suara otomatis menggunakan **gTTS** dan **pygame**.

---

## 📋 Fitur Utama

- **Pendaftaran Kendaraan Masuk** — Input nomor plat dan jenis kendaraan (Mobil/Motor) secara mudah.
- **Pengeluaran Kendaraan Fleksibel (Non-FIFO)** — Pilih kendaraan mana saja yang ingin dikeluarkan, tidak harus berurutan.
- **Pengumuman Suara Otomatis** — Sistem akan membacakan pengumuman dalam Bahasa Indonesia saat kendaraan masuk maupun keluar.
- **Sidebar Antrean Real-time** — Menampilkan daftar kendaraan yang sedang berada di area parkir secara langsung.
- **Riwayat Keluar** — Mencatat semua kendaraan yang telah keluar beserta waktu masuk dan keluar.

---

## 🗂️ Struktur File

```
.
├── studat1.py   # Frontend — Tampilan antarmuka Streamlit
├── studat2.py   # Backend — Logika bisnis, manajemen data, dan audio
└── README.md
```

### `studat1.py` — Frontend (UI)
Menangani seluruh tampilan antarmuka pengguna:
- Konfigurasi halaman Streamlit
- Sidebar untuk menampilkan antrean saat ini
- Form input kendaraan masuk
- Dropdown pemilihan kendaraan untuk dikeluarkan
- Tabel riwayat kendaraan keluar

### `studat2.py` — Backend (Logika)
Berisi class `SistemParkirBackend` yang mengelola:
- `antrean_parkir` — List data kendaraan yang sedang parkir
- `log_keluar` — Riwayat kendaraan yang telah keluar
- `tambah_kendaraan(plat, jenis)` — Validasi dan penambahan kendaraan ke antrean
- `keluarkan_kendaraan_by_index(indeks)` — Pengeluaran kendaraan berdasarkan pilihan
- `speak(text)` — Pengumuman suara menggunakan gTTS + pygame

---

## ⚙️ Instalasi & Menjalankan

### 1. Clone / Unduh Repository
```bash
git clone <url-repository>
cd <nama-folder>
```

### 2. Install Dependencies
```bash
pip install streamlit gtts pygame
```

### 3. Jalankan Aplikasi
```bash
streamlit run studat1.py
```

Aplikasi akan terbuka otomatis di browser pada `http://localhost:8501`.

---

## 📦 Dependencies

| Library      | Kegunaan                                      |
|--------------|-----------------------------------------------|
| `streamlit`  | Framework UI aplikasi web                     |
| `gtts`       | Text-to-Speech (Google Text-to-Speech)        |
| `pygame`     | Memutar audio pengumuman                      |
| `datetime`   | Pencatatan waktu masuk dan keluar (bawaan Python) |

---

## 🚀 Cara Penggunaan

1. **Daftarkan kendaraan masuk** — Isi nomor plat dan pilih jenis kendaraan, lalu klik **"Daftarkan Kendaraan"**. Sistem akan mengumumkan kendaraan masuk secara otomatis.
2. **Lihat antrean** — Sidebar di sebelah kiri menampilkan semua kendaraan yang sedang parkir beserta waktu masuknya.
3. **Keluarkan kendaraan** — Pilih kendaraan dari dropdown di kolom **"Kontrol Pintu Keluar"**, lalu klik **"Keluarkan Kendaraan Sekarang"**. Sistem akan mengumumkan kendaraan keluar.
4. **Cek riwayat** — Tabel riwayat di bagian bawah halaman mencatat semua kendaraan yang sudah keluar.

---

## 📝 Catatan

- Data antrean bersifat **sementara di memori** (tidak tersimpan ke database). Data akan hilang saat aplikasi di-restart.
- Fitur suara membutuhkan **koneksi internet** untuk gTTS dan perangkat dengan output audio yang berfungsi.
- Nomor plat akan otomatis dikonversi menjadi **huruf kapital**.
