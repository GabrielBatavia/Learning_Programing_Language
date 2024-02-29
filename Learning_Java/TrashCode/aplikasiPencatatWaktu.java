import java.util.Scanner;
import java.util.Timer;
import java.util.TimerTask;

/**
 * aplikasiPencatatWaktu
 */
public class aplikasiPencatatWaktu {

    public static void main(String[] args) {
        
        Scanner scanner = new Scanner(System.in);
        Timer timer = new Timer();

        System.out.println(); //kosongan
        System.out.println("Halo Selamat Datang");
        System.out.println("Selamat menikmati fitur aplikasi ini");

        System.out.println(); //kosongan

        System.out.println("Beberapa fitur yang bisa kamu pakai");
        System.out.println("1. Olahraga Indoor");
        System.out.println("2. Olahraga Outdoor");
        System.out.println("3. Tidur");
        System.out.println("4. Hitung mundur");
        System.out.println("5. Riwayat aktivitas");

        int choice = scanner.nextInt();
        switch (choice) {
            case 1:
            System.out.println("Silahkan pilih olahraga yang diinginkan");
            System.out.println("1. Angkat beban");
            System.out.println("2. Push up");
            System.out.println("3. Sit Up");
            System.out.println("4. Pull up");

            int Indoor = scanner.nextInt();

            scanner.nextLine(); // Konsumsi karakter baru setelah membaca pilihan olahraga

            System.out.println("Silahkan tekan enter untuk memulai latihan anda");
            scanner.nextLine(); // Menunggu pengguna menekan Enter

            TimerTask task1 = new TimerTask() {
                private int seconds = 0;

                @Override
                public void run() {
                    System.out.println("Waktu berjalan : " + seconds + "detik");
                    seconds++;
                }
            };


            // Mengeksekusi task setiap detik
            timer.scheduleAtFixedRate(task1, 0, 1000); // 1000 milliseconds = 1 detik

            // Tambahkan ini agar perhitungan waktu berhenti saat pengguna selesai
            System.out.println("Tekan Enter untuk menghentikan perhitungan waktu.");
            scanner.nextLine(); // Membuang karakter baru dari input sebelumnya
            scanner.nextLine(); // Menunggu pengguna untuk menekan Enter setelah selesai

             // Menghentikan perhitungan waktu
             task1.cancel();
             timer.purge();
                break;

            case 2:
            System.out.println("Silahkan pilih olahraga yang diinginkan");
            System.out.println("1. Berlari");
            System.out.println("2. Berjalan");
            System.out.println("3. Bersepeda");
            System.out.println("4. Senam");

            int Outdoor = scanner.nextInt();

            scanner.nextLine(); // Konsumsi karakter baru setelah membaca pilihan olahraga

            System.out.println("Silahkan tekan enter untuk memulai latihan anda");
            scanner.nextLine(); // Menunggu pengguna menekan Enter

            TimerTask task2 = new TimerTask() {
                private int seconds = 0;

                @Override
                public void run() {
                    System.out.println("Waktu berjalan : " + seconds + "detik");
                    seconds++;
                }
            };


            // Mengeksekusi task setiap detik
            timer.scheduleAtFixedRate(task2, 0, 1000); // 1000 milliseconds = 1 detik

            // Tambahkan ini agar perhitungan waktu berhenti saat pengguna selesai
            System.out.println("Tekan Enter untuk menghentikan perhitungan waktu.");
            scanner.nextLine(); // Membuang karakter baru dari input sebelumnya
            scanner.nextLine(); // Menunggu pengguna untuk menekan Enter setelah selesai

             // Menghentikan perhitungan waktu
             task2.cancel();
             timer.purge();
                break;

            case 3:
            scanner.nextLine(); // Konsumsi karakter baru setelah membaca pilihan olahraga

            System.out.println("Silahkan tekan enter untuk memulai perhitungan waktu tidur anda");

            scanner.nextLine(); // Menunggu pengguna menekan Enter

            TimerTask task3 = new TimerTask() {
                private int seconds = 0;

                @Override
                public void run() {
                    System.out.println("Waktu berjalan : " + seconds + "detik");
                    seconds++;
                }
            };


            // Mengeksekusi task setiap detik
            timer.scheduleAtFixedRate(task3, 0, 1000); // 1000 milliseconds = 1 detik

            // Tambahkan ini agar perhitungan waktu berhenti saat pengguna selesai
            System.out.println("Tekan Enter untuk menghentikan perhitungan waktu.");
            scanner.nextLine(); // Membuang karakter baru dari input sebelumnya
            scanner.nextLine(); // Menunggu pengguna untuk menekan Enter setelah selesai

             // Menghentikan perhitungan waktu
             task3.cancel();
             timer.purge();



                break;
            
            case 4:
                scanner.nextLine();
            
                System.out.println("Pilih berapa lama waktu mundur anda (dalam detik):");
                int secondsmundur = scanner.nextInt();
                
                System.out.println("Silahkan tekan enter untuk memulai perhitungan mundur");
                scanner.nextLine(); // Mengonsumsi karakter baru (newline) setelah membaca input integer
                scanner.nextLine(); // Menunggu pengguna menekan Enter
            
                TimerTask task4 = new TimerTask() {
                    private int seconds = secondsmundur; // Menggunakan nilai input pengguna
            
                    @Override
                    public void run() {
                        if (seconds >= 0) {
                            System.out.println("Waktu berjalan: " + seconds + " detik");
                            seconds--;
                        } else {
                            // Menghentikan perhitungan waktu setelah waktu mundur habis
                            System.out.println("Waktu mundur telah selesai.");
                            cancel();
                            timer.purge();
                        }
                    }
                };
            
                // Mengeksekusi task setiap detik
                timer.scheduleAtFixedRate(task4, 0, 1000); // 1000 milliseconds = 1 detik
            
                // Tambahkan ini agar perhitungan waktu berhenti saat pengguna selesai
                System.out.println("Tekan Enter untuk menghentikan perhitungan waktu.");
                scanner.nextLine(); // Menunggu pengguna untuk menekan Enter untuk menghentikan perhitungan waktu
            
                // Menghentikan perhitungan waktu
                task4.cancel();
                timer.purge();
                break;
            
            
            case 5:


                break;
            
            default:
                break;
        }
    }
}