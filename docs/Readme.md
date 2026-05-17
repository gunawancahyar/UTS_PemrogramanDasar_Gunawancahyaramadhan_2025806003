# 🧠 UTS Pemrograman Dasar (C & Python)

## 👤 Identitas
- Nama: Gunawan Cahya Ramadhan
- NIM: 2025806003
- Kelas: Teknologi informasi semester 2
- Dosen: Rintis Mardika Sunarto S.KOM,M.KOM.
- Repository: https://github.com/gunawancahyar/UTS_PemrogramanDasar_Gunawancahyaramadhan_2025806003

---

## 📚 Deskripsi
Proyek ini adalah Ujian Tengah Semester (UTS) Pemrograman Dasar, yang menggabungkan konsep C dan Python.  
Mahasiswa diminta membuat beberapa proyek terpisah dengan fitur logika, struktur data, file handling, dan modular programming.

---

## 🧩 Struktur Folder

C/
 ├── soal1_data_mahasiswa/
 └── soal4_csv_json/
 Python/
 ├── soal2_game_guess/
 ├── soal3_text_analyzer/
 └── soal4_csv_to_json/
 docs/

---

## ⚙️ Persiapan Lingkungan

### 🔹 Instalasi C
Gunakan salah satu:
- macOS: `brew install gcc`
- Windows: install **MinGW** lalu tambahkan path ke environment
- Linux: `sudo apt install build-essential`

Cek versi:
```bash
gcc --version

🔹 Instalasi Python
Gunakan Python 3.x:
python3 --version

Jika belum ada, unduh di: https://www.python.org/downloads/
🔹 (Opsional) Buat Virtual Environment
python3 -m venv venv
source venv/bin/activate   # (macOS/Linux)
venv\Scripts\activate      # (Windows)

Instal library tambahan:
pip install colorama


🧠 Soal & Deskripsi Singkat
🧩 Soal 1 – Sistem Data Mahasiswa (C)
Menggunakan struct, pointer, linked list, file CSV


Fitur: tambah, hapus, cari, tampilkan, dan simpan data


🎮 Soal 2 – Game Tebak Angka (Python)
Fitur login pemain, level permainan, dan skor otomatis


Gunakan random, json, dan colorama


🧠 Soal 3 – Analisis Teks (Python)
Baca input.txt, hitung kata, huruf, baris, dan frekuensi kata


Tulis laporan ke report.txt


Buat modul analyzer.py dan utils.py


🔄 Soal 4 – Konversi Data (C ↔ Python)
Gunakan hasil file CSV dari Soal 1


Buat script Python untuk membaca CSV dan mengubah ke JSON



🚀 Cara Menjalankan
▶️ C (contoh Soal 1)
cd C/soal1_data_mahasiswa
gcc main.c linked_list.c -o program
./program

▶️ Python (contoh Soal 3)
cd Python/soal3_text_analyzer
python3 main.py


🧾 Laporan
Semua dokumentasi, screenshot, dan analisis ditaruh di folder /docs


Minimal berisi:


Screenshot hasil running tiap program


Analisis singkat dari tiap soal


File laporan_uts.pdf



🏁 Commit History Contoh
feat: tambah modul struct mahasiswa dan simpan ke CSV
fix: perbaiki bug pointer pada fungsi hapus data
update: tambahkan skor JSON untuk game Python
docs: tambahkan screenshot output di folder docs


📸 Contoh Output

---

## 💡 OPSIONAL: FILE `.gitignore`
Agar repo tetap bersih, buat file `.gitignore` di root:


venv/
 pycache/
 *.exe
 *.o
 *.csv
 *.json
 *.txt
 *.pdf

---
