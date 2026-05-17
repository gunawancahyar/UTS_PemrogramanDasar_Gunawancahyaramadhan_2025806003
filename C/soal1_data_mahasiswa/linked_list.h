#ifndef LINKED_LIST_H
#define LINKED_LIST_H

typedef struct Mahasiswa {
    char nama[50];
    char nim[15];
    float tugas, uts, uas, nilaiAkhir;
    char mutu;
    struct Mahasiswa *next;
} Mahasiswa;

// Prototipe Fungsi
Mahasiswa* buatNode(char nama[], char nim[], float tugas, float uts, float uas);
void tambahMahasiswa(Mahasiswa **head, char nama[], char nim[], float tugas, float uts, float uas);
void hapusMahasiswa(Mahasiswa **head, char nim[]);
Mahasiswa* cariMahasiswa(Mahasiswa *head, char nim[]);
void tampilkanTabel(Mahasiswa *head);
void simpanKeCSV(Mahasiswa *head, char namaFile[]);
void bersihkanMemori(Mahasiswa **head);

#endif