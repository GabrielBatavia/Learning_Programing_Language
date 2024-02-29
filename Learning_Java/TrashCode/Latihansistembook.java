import java.text.NumberFormat;
import java.util.Locale;
import java.util.Scanner;

public class Latihansistembook {

    public static void main(String[] args) {
        
        Scanner scanner =  new Scanner(System.in);

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
