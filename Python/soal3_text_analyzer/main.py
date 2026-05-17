import analyzer
import utils
import os

def main():
    input_file = "input.txt"
    output_file = "report.txt"

    if not os.path.exists(input_file):
        print(f"Error: {input_file} tidak ditemukan!")
        return

    # 1. Read Input
    with open(input_file, "r", encoding="utf-8") as f:
        lines = f.readlines()
    
    full_content = "".join(lines)
    
    # 2. Analyze
    stats = analyzer.get_statistics(lines)
    v_count, c_count = utils.count_vowels_consonants(full_content)
    
    # 3. Generate Report Content
    report = []
    report.append("=== LAPORAN ANALISIS TEKS ===")
    report.append(f"Jumlah Baris          : {stats['total_lines']}")
    report.append(f"Jumlah Kata           : {stats['total_words']}")
    report.append(f"Jumlah Huruf Vokal    : {v_count}")
    report.append(f"Jumlah Huruf Konsonan : {c_count}")
    report.append("\n--- GRAFIK FREKUENSI KATA ---")
    
    for word, count in stats['top_5']:
        graph = analyzer.generate_ascii_bar(word, count)
        report.append(graph)

    # 4. Write to File & Screen
    final_report = "\n".join(report)
    print(final_report)
    
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(final_report)
    
    print(f"\nLaporan telah disimpan di {output_file}")

if __name__ == "__main__":
    main()