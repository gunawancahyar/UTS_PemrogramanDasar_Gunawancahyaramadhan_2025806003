#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "linked_list.h"

char hitungMutu(float na) {
    if (na >= 80) return 'A';
    if (na >= 70) return 'B';
    if (na >= 60) return 'C';
    if (na >= 50) return 'D';
    return 'E';
}

Mahasiswa* buatNode(char nama[], char nim[], float tugas, float uts, float uas) {
    Mahasiswa *baru = (Mahasiswa*)malloc(sizeof(Mahasiswa));
    if (!baru) return NULL;

    strcpy(baru->nama, nama);
    strcpy(baru->nim, nim);
    baru->tugas = tugas;
    baru->uts = uts;
    baru->uas = uas;
    
    // Hitung Nilai Akhir: 30% Tugas, 30% UTS, 40% UAS
    baru->nilaiAkhir = (0.3 * tugas) + (0.3 * uts) + (0.4 * uas);
    baru->mutu = hitungMutu(baru->nilaiAkhir);
    baru->next = NULL;
    
    return baru;
}

void tambahMahasiswa(Mahasiswa **head, char nama[], char nim[], float tugas, float uts, float uas) {
    Mahasiswa *baru = buatNode(nama, nim, tugas, uts, uas);
    baru->next = *head;
    *head = baru;
}

void hapusMahasiswa(Mahasiswa **head, char nim[]) {
    Mahasiswa *temp = *head, *prev = NULL;

    if (temp != NULL && strcmp(temp->nim, nim) == 0) {
        *head = temp->next;
        free(temp);
        printf("Data NIM %s berhasil dihapus.\n", nim);
        return;
    }

    while (temp != NULL && strcmp(temp->nim, nim) != 0) {
        prev = temp;
        temp = temp->next;
    }

    if (temp == NULL) {
        printf("NIM %s tidak ditemukan.\n", nim);
        return;
    }

    prev->next = temp->next;
    free(temp);
    printf("Data NIM %s berhasil dihapus.\n", nim);
}

void tampilkanTabel(Mahasiswa *head) {
    printf("\n%-20s | %-10s | %-5s | %-5s | %-5s | %-5s | %-4s\n", 
           "Nama", "NIM", "Tgs", "UTS", "UAS", "NA", "Mutu");
    printf("---------------------------------------------------------------------------\n");
    while (head != NULL) {
        printf("%-20s | %-10s | %-5.1f | %-5.1f | %-5.1f | %-5.1f | %-4c\n",
               head->nama, head->nim, head->tugas, head->uts, head->uas, head->nilaiAkhir, head->mutu);
        head = head->next;
    }
}

void simpanKeCSV(Mahasiswa *head, char namaFile[]) {
    FILE *f = fopen(namaFile, "w");
    if (!f) return;

    fprintf(f, "Nama,NIM,Tugas,UTS,UAS,NilaiAkhir,Mutu\n");
    while (head != NULL) {
        fprintf(f, "%s,%s,%.1f,%.1f,%.1f,%.1f,%c\n",
                head->nama, head->nim, head->tugas, head->uts, head->uas, head->nilaiAkhir, head->mutu);
        head = head->next;
    }
    fclose(f);
    printf("\nData berhasil disimpan ke %s\n", namaFile);
}

void bersihkanMemori(Mahasiswa **head) {
    Mahasiswa *curr = *head;
    while (curr != NULL) {
        Mahasiswa *next = curr->next;
        free(curr);
        curr = next;
    }
    *head = NULL;
}