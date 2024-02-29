import java.text.NumberFormat;
import java.util.Locale;
import java.util.Scanner;

public class latihanSistemApart {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        boolean loggedIn = false;
        String username = null;
        String password = null;
        boolean firstLogin = true;

        while (!loggedIn) {
            System.out.println("Selamat datang di aplikasi pemesanan apartemen!");

            if (firstLogin) {
                System.out.println("Buat username dan password baru");
                System.out.print("Buat username : ");
                username = scanner.nextLine();
                System.out.print("Buat password Anda : ");
                password = scanner.nextLine();
                firstLogin = false;
            } else {
                System.out.print("Masukkan username : ");
                String inputUsername = scanner.nextLine();
                System.out.print("Masukkan password : ");
                String inputPassword = scanner.nextLine();

                // Anda dapat menambahkan logika autentikasi di sini, misalnya, dengan memeriksa basis data pengguna.
                // Untuk tujuan demonstrasi, kita akan membandingkan dengan kredensial yang telah dibuat sebelumnya.
                if (inputUsername.equals(username) && inputPassword.equals(password)) {
                    loggedIn = true;
                    System.out.println("Login berhasil!");
                } else {
                    System.out.println("Login gagal. Coba lagi.");
                }
            }
        }

        int jmlh_malam, tipe_kamar;

        System.out.println();
        System.out.println("Selamat Datang di App");
        System.out.println();

        System.out.println("Berikut adalah daftar tipe kamar di apartemen kami");
        System.out.println("1. Tipe Kamar Studio");
        System.out.println("2. Tipe kamar Duplex");
        System.out.println("3. Tipe Kamar Triplex");
        System.out.println();

        System.out.println("Berapa lama kamu akan menginap?");
        jmlh_malam = scanner.nextInt();
        System.out.println();

        System.out.println("Silahkan pilih tipe kamar yang anda inginkan");
        tipe_kamar = scanner.nextInt();

        int a = 150000;
        int b = 300000;
        int c = 500000;
        
        int totalBiaya = 0;

        switch (tipe_kamar) {
            case 1:
                System.out.println("Harga Kamar tipe Studio permalam adalah 150k");
                totalBiaya = jmlh_malam * a;
                break;
        
            case 2:
                System.out.println("Harga Kamar tipe Duplex permalam adalah 300k");
                totalBiaya = jmlh_malam * b;
                break;

            case 3:
                System.out.println("Harga Kamar tipe Triplex permalam adalah 500k");
                totalBiaya = jmlh_malam * c;
                break;
                
            default:
                System.out.println("Tipe kamar invalid, silahkan masukkan nomor tipe kamar yang tersedia");
                break;
        }

        // Format totalBiaya sebagai mata uang
        NumberFormat formatRupiah = NumberFormat.getCurrencyInstance(new Locale("id", "ID"));
        String totalBiayaFormatted = formatRupiah.format(totalBiaya);

        System.out.println("Total biaya yang harus anda bayar adalah : " + totalBiayaFormatted);
        System.out.println();

        scanner.close();
    }
}

