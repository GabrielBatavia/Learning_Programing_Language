#include <stdio.h>
#include <stdbool.h>
#include <string.h>

int main () {

    char nama[] = "Gabriel Batavia Xaverius";
    char nama2[] = "Shalom Velicia";
    char nama3[] = "Rayhan";
    char nama4[] = "Farrel Nandito";
    char kendaraan[] = "Motor";
    char kendaraan2[] = "Mobil";

    if (strcmp(nama, "Gabriel Batavia Xaverius") == 0 && strcmp(kendaraan, "Motor") == 0) {
        printf("nama ku adalah : %s\n", nama);
        printf("Aku suka dan hanya punya %s untuk saat ini\n", kendaraan);
    } else if (strcmp(nama,"Gabriel Batavia Xaverius") == 0 && strcmp(nama2, "Shalom Velicia") == 0) {
        printf("nama ku adalah : %s\n", nama2);
        printf("Aku berteman baik dengan %s namun saat ini kami berpisah ", nama);
    } else {
        printf("nama ku adalah : %s\n", nama3);
        printf("nama ku adalah : %s\n", nama4);
    }

}