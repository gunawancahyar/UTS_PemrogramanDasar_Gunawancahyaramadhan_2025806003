#include <stdio.h>
#include <string.h>
#include "linked_list.h"

int main() {
    Mahasiswa *listDosen = NULL;
    int pilihan;
    char nama[50], nim[15];
    float t, uts, uas;

    do {
        printf("\n--- SISTEM DATA MAHASISWA ---");
        printf("\n1. Tambah Mahasiswa\n2. Tampilkan Semua\n3. Hapus (NIM)\n4. Simpan ke CSV\n5. Keluar\nPilihan: ");
        scanf("%d", &pilihan);
        getchar(); // clear buffer

        switch(pilihan) {
            case 1:
                printf("Nama: "); fgets(nama, 50, stdin); nama[strcspn(nama, "\n")] = 0;
                printf("NIM: "); scanf("%s", nim);
                printf("Nilai Tugas, UTS, UAS (pisahkan spasi): ");
                scanf("%f %f %f", &t, &uts, &uas);
                tambahMahasiswa(&listDosen, nama, nim, t, uts, uas);
                break;
            case 2:
                tampilkanTabel(listDosen);
                break;
            case 3:
                printf("Masukkan NIM yang akan dihapus: ");
                scanf("%s", nim);
                hapusMahasiswa(&listDosen, nim);
                break;
            case 4:
                simpanKeCSV(listDosen, "data_mahasiswa.csv");
                break;
        }
    } while (pilihan != 5);

    bersihkanMemori(&listDosen);
    return 0;
}