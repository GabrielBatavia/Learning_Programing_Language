public static void bubbleSort(persiapan_uts_smstr2[] array) {
    boolean swapped;
    for (int i = 0; i < array.length - 1; i++) {
        swapped = false;
        for (int j = 0; j < array.length - i - 1; j++) {
            if (array[j].age > array[j + 1].age) {
                // Tukar elemen jika elemen saat ini lebih besar dari elemen berikutnya
                persiapan_uts_smstr2 temp = array[j];
                array[j] = array[j + 1];
                array[j + 1] = temp;
                swapped = true;
            }
        }
        // Jika tidak ada tukaran yang terjadi dalam satu putaran penuh, array sudah terurut
        if (!swapped) break;
    }
}


z
public static void selectionSort(persiapan_uts_smstr2[] array) {
    // Loop luar mengiterasi melalui setiap elemen array kecuali yang terakhir
    for (int i = 0; i < array.length - 1; i++) {
        // Inisialisasi indeks minimum dengan nilai i saat ini
        int minIndex = i;  
        
        // Loop dalam mencari elemen terkecil dalam segmen array yang belum diurutkan
        for (int j = i + 1; j < array.length; j++) {
            // Bandingkan elemen pada indeks j dengan elemen pada indeks minimum saat ini
            if (array[j].age < array[minIndex].age) {
                // Jika elemen pada j lebih kecil, perbarui minIndex dengan j
                minIndex = j;  
            }
        }
        
        // Setelah menemukan indeks minimum, tukar elemen pada indeks i dengan elemen pada indeks minimum
        persiapan_uts_smstr2 temp = array[minIndex];
        array[minIndex] = array[i];
        array[i] = temp;
    }
}


public static void insertionSort(persiapan_uts_smstr2[] array) {
    // Loop melalui setiap elemen dalam array mulai dari yang kedua
    for (int i = 1; i < array.length; i++) {
        // Key menyimpan objek yang akan diposisikan
        persiapan_uts_smstr2 key = array[i];
        // J menyimpan indeks akhir dari segmen yang sudah diurutkan
        int j = i - 1;

        // Pindah ke kiri array, cari posisi yang tepat untuk key
        // Bandingkan usia dari key dengan elemen di segmen yang sudah diurutkan
        while (j >= 0 && array[j].age > key.age) {
            // Geser elemen yang lebih besar dari key satu posisi ke kanan
            array[j + 1] = array[j];
            j = j - 1; // terus bergerak ke kiri
        }
        // Tempatkan key di posisi yang benar dalam segmen yang sudah diurutkan
        array[j + 1] = key;
    }
}



public static int sequentialSearch(persiapan_uts_smstr2[] array, String targetName) {
    // Loop melalui setiap elemen dalam array
    for (int i = 0; i < array.length; i++) {
        // Periksa apakah nama elemen saat ini cocok dengan nama yang dicari
        if (array[i].name.equals(targetName)) {
            // Jika ditemukan, kembalikan indeks elemen tersebut
            return i;
        }
    }
    // Jika tidak ditemukan, kembalikan -1
    return -1;
}

