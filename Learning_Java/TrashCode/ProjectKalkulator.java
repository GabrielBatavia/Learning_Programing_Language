import java.util.Scanner;

/**
 * ProjectKalkulator
 */
public class ProjectKalkulator {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        String password = "sandiAnda"; // Gantilah dengan sandi Anda sendiri

        boolean loggedIn = false;

        while (!loggedIn) {
            System.out.println("Masukkan sandi untuk mengakses kalkulator:");
            String userPassword = input.nextLine();

            if (userPassword.equals(password)) {
                System.out.println("Selamat datang! Silakan gunakan kalkulator:");
                loggedIn = true; // Sandi benar, masuk ke kalkulator
            } else {
                System.out.println("Sandi salah. Coba lagi.");
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
