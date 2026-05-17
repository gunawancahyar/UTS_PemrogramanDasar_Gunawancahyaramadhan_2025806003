#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void convertCSVtoJSON(const char *csvFile, const char *jsonFile) {
    FILE *fp_csv = fopen("../soal1_data_mahasiswa/data_mahasiswa.csv", "r");
    FILE *fp_json = fopen(jsonFile, "w");

    if (!fp_csv || !fp_json) {
        printf("Gagal membuka file!\n");
        return;
    }

    char line[256];
    char nama[50], nim[20], mutu[5];
    float tugas, uts, uas, na;
    int firstLine = 1;

    fprintf(fp_json, "[\n"); // Awal array JSON

    // Skip header CSV
    fgets(line, sizeof(line), fp_csv);

    while (fgets(line, sizeof(line), fp_csv)) {
        if (!firstLine) fprintf(fp_json, ",\n");
        
        // Parsing data dari CSV (sesuaikan format dengan output program sebelumnya)
        sscanf(line, "%[^,],%[^,],%f,%f,%f,%f,%s", 
               nama, nim, &tugas, &uts, &uas, &na, mutu);

        fprintf(fp_json, "  {\n");
        fprintf(fp_json, "    \"nama\": \"%s\",\n", nama);
        fprintf(fp_json, "    \"nim\": \"%s\",\n", nim);
        fprintf(fp_json, "    \"nilai_akhir\": %.2f,\n", na);
        fprintf(fp_json, "    \"mutu\": \"%s\"\n", mutu);
        fprintf(fp_json, "  }");
        
        firstLine = 0;
    }

    fprintf(fp_json, "\n]\n"); // Akhir array JSON

    fclose(fp_csv);
    fclose(fp_json);
    printf("Konversi berhasil! Cek file %s\n", jsonFile);
}

int main() {
    convertCSVtoJSON("data_mahasiswa.csv", "data_mahasiswa.json");
    return 0;
}