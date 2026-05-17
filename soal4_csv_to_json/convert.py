import csv
import json
import argparse
import os

def process_data(input_file, output_file):
    if not os.path.exists(input_file):
        print(f"Error: File {input_file} tidak ditemukan! Jalankan program C terlebih dahulu.")
        return

    data_list = []
    total_nilai = 0
    count = 0

    print(f"\n{'='*45}")
    print(f"{'NAMA':<15} | {'NIM':<10} | {'NILAI':<6} | {'MUTU'}")
    print(f"{'-'*45}")

    try:
        with open(input_file, mode='r', encoding='utf-8') as csvfile:
            # Menggunakan DictReader agar header CSV otomatis jadi key
            reader = csv.DictReader(csvfile)
            
            for row in reader:
                # Konversi nilai ke float untuk perhitungan
                nilai_akhir = float(row['NilaiAkhir'])
                
                # Menampilkan data dengan rapi ke layar
                print(f"{row['Nama']:<15} | {row['NIM']:<10} | {nilai_akhir:<6.2f} | {row['Mutu']}")
                
                # Simpan ke list untuk JSON
                data_list.append({
                    "nama": row['Nama'],
                    "nim": row['NIM'],
                    "nilai_akhir": nilai_akhir,
                    "mutu": row['Mutu']
                })
                
                total_nilai += nilai_akhir
                count += 1

        # Hitung rata-rata
        if count > 0:
            rata_rata = total_nilai / count
            print(f"{'-'*45}")
            print(f"Rata-rata Nilai Akhir: {rata_rata:.2f}")

        # Simpan ke JSON
        with open(output_file, 'w', encoding='utf-8') as jsonfile:
            json.dump(data_list, jsonfile, indent=4)
        
        print(f"\nBerhasil! Data dikonversi ke: {output_file}")

    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Konversi data Mahasiswa dari CSV ke JSON")
    
    # Ubah "data_mahasiswa.csv" menjadi jalur lengkap ke folder C kamu
    # Gunakan r"path" agar Windows tidak bingung dengan backslash
    parser.add_argument("--input", default=r"D:\Tugas Gunawan\Semester 2\Folder_C\data_mahasiswa.csv", help="Nama file CSV input")
    parser.add_argument("--output", default="data_mahasiswa.json", help="Nama file JSON output")
    
    args = parser.parse_args()
    process_data(args.input, args.output)

