import java.util.Scanner;

public class Investasi_Tugas3_Daspro14 {

    public static void main(String[] args) {
        // Deklarasi variabel
        double uangAwal;
        double keuntunganPersen = 0.117; // Keuntungan tetap 11,7%
        int jumlahTahun;

        // Input uang awal
        System.out.print("Masukkan uang awal: ");
        Scanner scanner = new Scanner(System.in);
        uangAwal = scanner.nextDouble();

        // Input jumlah tahun
        System.out.print("Masukkan jumlah tahun: ");
        jumlahTahun = scanner.nextInt();

        // Hitung hasil investasi
        double hasilInvestasi = hitungInvestasi(uangAwal, keuntunganPersen, jumlahTahun);

        // Tampilkan hasil investasi
        System.out.println("Hasil investasi emas batang: Rp" + hasilInvestasi);

        // Tutup scanner untuk mencegah resource leak
        scanner.close();
    }

    // Metode rekursif untuk menghitung hasil investasi
    private static double hitungInvestasi(double uangAwal, double keuntunganPersen, int tahun) {
        // Basis dari rekursi: jika sudah mencapai tahun 0, mengembalikan uang awal
        if (tahun == 0) {
            return uangAwal;
        } else {
            // Panggil diri sendiri untuk tahun sebelumnya, kemudian tambahkan keuntungan
            return hitungInvestasi(uangAwal, keuntunganPersen, tahun - 1) * (1 + keuntunganPersen);
        }
    }
}