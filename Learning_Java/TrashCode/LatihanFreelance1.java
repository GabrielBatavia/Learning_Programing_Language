import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
/**
 * LatihanFreelance1
 */
public class LatihanFreelance1 {

    public static void main(String[] args) {
        
        Scanner scanner = new Scanner(System.in);
        List<String> daftarTugas = new ArrayList<>(); // Mendeklarasikan dan menginisialisasi daftar tugas menggunakan ArrayList.

        System.out.println(); // kosongan agar ada jarak
        System.out.println("Selamat datang di aplikasi");
        System.out.println(); // kosongan agar ada jarak

        boolean exit = false;
        while (!exit) {
            
            System.out.println("Main Menu (Silahkan pilih tindakan Anda :)");
            System.out.println("1. Tambah tugas");
            System.out.println("2. Lihat daftar tugas");
            System.out.println("3. Hapus Tugas");
            System.out.println("4. Tandai selesai");
            System.out.println("5. Keluar");
        
            int choice = scanner.nextInt();
            scanner.nextLine(); // Membersihkan newline setelah membaca pilihan.

            switch (choice) {
                case 1:
                    System.out.println("Masukkan Judul Tugas : ");
                    String judulTugas = scanner.nextLine();
                    daftarTugas.add(judulTugas);
                    System.out.println("Tugas '" + judulTugas + "' telah ditambahkan.");
                    System.out.println("Terimakasih sudah menambahkan Tugas");
                    System.out.println(); // kosongan agar output berjarak
                    break;
            

                case 2:
                System.out.println("Daftar Tugas Anda: ");
                for (int i = 0; i < daftarTugas.size(); i++) {
                    System.out.println((i + 1) + ". " + daftarTugas.get(i));
                }
                System.out.println(); // kosongan agar output berjarak
                break;

                case 3:
                System.out.println("Masukkan nomor tugas yang ingin dihapus: ");
                int nomorTugasHapus = scanner.nextInt();
                scanner.nextLine(); // Membersihkan newline setelah membaca nomor

                // Validasi nomor tugas
                if (nomorTugasHapus > 0 && nomorTugasHapus <= daftarTugas.size()) {
                    String judulTugasHapus = daftarTugas.get(nomorTugasHapus - 1);
                    if (judulTugasHapus.trim().isEmpty()) {
                        System.out.println("Judul tugas kosong, tidak dapat dihapus.");
                    } else {
                        daftarTugas.remove(nomorTugasHapus - 1);
                        System.out.println("Tugas '" + judulTugasHapus + "' telah dihapus.");
                        System.out.println("Terimakasih sudah menghapus Tugas");
                    }
                } else {
                    System.out.println("Nomor tugas tidak valid.");
                    System.out.println("Silahkan masukkan kembali nomor tugas yang benar");
                }
                System.out.println(); // Baris kosong ditambahkan setelah menampilkan hasil penghapusan.
                break;


                case 4:
                System.out.print("Masukkan nomor tugas yang selesai: ");
                int nomorTugasSelesai = scanner.nextInt();
                scanner.nextLine(); // Membersihkan newline setelah membaca nomor.
                if (nomorTugasSelesai > 0 && nomorTugasSelesai <= daftarTugas.size()) {
                    daftarTugas.remove(nomorTugasSelesai - 1);
                    System.out.println("Tugas nomor " + nomorTugasSelesai + " telah ditandai sebagai selesai.");
                    System.out.println("Terimakasih sudah menyelesaikan Tugas Anda");
                } else {
                    System.out.println("Nomor tugas tidak valid.");
                }
                System.out.println(); // kosongan agar output berjarak
                break;

                case 5:
                exit = true;
                System.out.println("Terima kasih telah menggunakan Aplikasi Manajemen Tugas. Selamat tinggal!");
                break;

                default:
                    System.out.println("Pilihan tidak valid silahkan pilih lagi");
                    System.out.println();
                    break;
            }



        }
        
        scanner.close();
    }
}