import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class PercobaanProjectLogin {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        Map<String, String> credentials = new HashMap<>();

        // Tambahkan data nama pengguna dan kata sandi oleh pemilik program
        credentials.put("user1", "password1");
        credentials.put("user2", "password2");

        System.out.print("Masukkan nama pengguna: ");
        String username = input.nextLine();

        System.out.print("Masukkan kata sandi: ");
        String password = input.nextLine();

        // Di sini kita memeriksa apakah nama pengguna ada dalam `credentials` HashMap.
        if (credentials.containsKey(username)) {
            // Jika nama pengguna ada, periksa kata sandi
            if (credentials.get(username).equals(password)) {
                System.out.println("Selamat datang, " + username + "!");
            } else {
                System.out.println("Kata sandi salah. Akses ditolak.");
            }
        } else {
            // Jika nama pengguna tidak ada dalam `credentials` HashMap,
            // periksa apakah kata sandi yang dimasukkan adalah "password1".
            if (password.equals("password1")) {
                System.out.println("Selamat datang, " + username + "!");
            } else {
                System.out.println("Nama pengguna atau kata sandi salah. Akses ditolak.");
            }
        }

        double numbers1, numbers2, choice, result = 0;
        System.out.println("Program Kalkulator Sederhana");
        System.out.println("1. Penjumlahan");
        System.out.println("2. Pengurangan");
        System.out.println("3. Pembagian");
        System.out.println("4. Perkalian");
        System.out.println("5. Sisa Bagi");
        System.out.println("............");

        // Input data
        System.out.println("Masukkan angka pertama : ");
        numbers1 = input.nextDouble();
        System.out.println("Masukkan angka kedua : ");
        numbers2 = input.nextDouble();

        // Pilihan Operasi
        System.out.println("Masukkan Operasi: ");
        choice = input.nextDouble();

        switch ((int) choice) {
            case 1:
                result = numbers1 + numbers2;
                break;

            case 2:
                result = numbers1 - numbers2;
                break;

            case 3:
                if (numbers2 != 0) {
                    result = numbers1 / numbers2;
                } else {
                    System.out.println("Pembagian oleh nol tidak diizinkan");
                }
                break;

            case 4:
                result = numbers1 * numbers2;
                break;

            case 5:
                if (numbers2 != 0) {
                    result = numbers1 % numbers2;
                } else {
                    System.out.println("Modulus oleh nol tidak diizinkan");
                }
                break;

            default:
                System.out.println("Salah memasukkan. Silakan lihat menu");
        }

        System.out.println("Hasil : " + result);

        // Tutup Scanner setelah penggunaan

        input.close();

    }
}


