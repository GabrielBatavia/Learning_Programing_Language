//Anda akan membuat aplikasi berbasis Command Line Interface (CLI) 
//untuk manajemen tugas sederhana. Aplikasi ini akan memungkinkan pengguna untuk menambahkan tugas baru, melihat daftar tugas, 
//menandai tugas sebagai selesai, dan keluar dari aplikasi.

/**
 * LatihanAplikasiManajemenTugas
 */


import java.util.ArrayList;
import java.util.Scanner;

public class LatihanAplikasiManajemenTugas {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        ArrayList<String> daftarTugas = new ArrayList<>();

        boolean exit = false;
        while (!exit) {
            System.out.println("\nPilih tindakan:");
            System.out.println("1. Tambah tugas");
            System.out.println("2. Lihat daftar tugas");
            System.out.println("3. Tandai selesai");
            System.out.println("4. Keluar");

            int choice = scanner.nextInt();
            scanner.nextLine(); // Membersihkan newline setelah membaca pilihan.

            switch (choice) {
                case 1:
                    System.out.print("Masukkan judul tugas: ");
                    String judulTugas = scanner.nextLine();
                    daftarTugas.add(judulTugas);
                    System.out.println("Tugas '" + judulTugas + "' telah ditambahkan.");
                    break;
                case 2:
                    System.out.println("Daftar tugas Anda:");
                    for (int i = 0; i < daftarTugas.size(); i++) {
                        System.out.println((i + 1) + ". " + daftarTugas.get(i));
                    }
                    break;
                case 3:
                    System.out.print("Masukkan nomor tugas yang selesai: ");
                    int nomorTugasSelesai = scanner.nextInt();
                    scanner.nextLine(); // Membersihkan newline setelah membaca nomor.
                    if (nomorTugasSelesai > 0 && nomorTugasSelesai <= daftarTugas.size()) {
                        daftarTugas.remove(nomorTugasSelesai - 1);
                        System.out.println("Tugas nomor " + nomorTugasSelesai + " telah ditandai sebagai selesai.");
                    } else {
                        System.out.println("Nomor tugas tidak valid.");
                    }
                    break;
                case 4:
                    exit = true;
                    System.out.println("Terima kasih telah menggunakan Aplikasi Manajemen Tugas. Selamat tinggal!");
                    break;
                default:
                    System.out.println("Pilihan tidak valid. Silakan pilih kembali.");
            }
        }

        scanner.close();
    }
}
