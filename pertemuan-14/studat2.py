import datetime
import time
from io import BytesIO
from gtts import gTTS
import pygame

class SistemParkirBackend:
    def __init__(self):
        # State/database sementara di memori backend
        self.antrean_parkir = []
        self.log_keluar = []
        pygame.mixer.init()

    def speak(self, text):
        """Menghasilkan suara pengumuman menggunakan gTTS dan pygame"""
        if not text:
            return
        try:
            tts = gTTS(text=text, lang='id')
            fp = BytesIO()
            tts.write_to_fp(fp)
            fp.seek(0)
            
            pygame.mixer.music.load(fp, "mp3")
            pygame.mixer.music.play()
            time.sleep(0.1)  # Jeda pendek agar stream audio stabil
        except Exception as e:
            print(f"Error audio: {e}")

    def tambah_kendaraan(self, plat, jenis):
        """Logika validasi dan input kendaraan masuk"""
        if not plat:
            return False, "Plat nomor tidak boleh kosong!"
            
        plat_bersih = plat.strip().upper()
        waktu_masuk = datetime.datetime.now().strftime("%H:%M:%S")
        
        data = {"Plat": plat_bersih, "Jenis": jenis, "Waktu": waktu_masuk}
        self.antrean_parkir.append(data)
        
        # Trigger suara masuk
        self.speak(f"Kendaraan {jenis} {plat_bersih} silahkan masuk.")
        return True, f"Sukses mendaftarkan {plat_bersih}"

    def keluarkan_kendaraan_by_index(self, indeks):
        """Logika mengeluarkan kendaraan berdasarkan pilihan indeks (Non-FIFO)"""
        if not self.antrean_parkir:
            return False, "Antrean kosong!"
            
        if indeks < 0 or indeks >= len(self.antrean_parkir):
            return False, "Pilihan kendaraan tidak valid!"
            
        # Proses hapus dari antrean
        keluar = self.antrean_parkir.pop(indeks)
        keluar["Waktu Keluar"] = datetime.datetime.now().strftime("%H:%M:%S")
        self.log_keluar.append(keluar)
        
        # Trigger suara keluar
        self.speak(f"Kendaraan dengan plat nomor {keluar['Plat']} silakan keluar. Terima kasih.")
        return True, keluar