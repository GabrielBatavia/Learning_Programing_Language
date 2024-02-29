import java.util.Scanner;

public class Nested1 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        // Array 2 dimensi untuk menyimpan informasi pemesanan kamar
        String[][] bookings = new String[4][7]; // Maksimal 4 pengguna, dan 7 informasi pemesanan per pengguna
        String[] usernames = {"User1", "Gabriel", "Mera", "Chika"};
        String statusPemesanan = "BelumDipesan";
        String statusCheckIn = "belum";

        // Deklarasikan stok kamar untuk setiap tipe kamar
        int[] stokKamar = {10, 5, 3}; // Misalnya: 10 Studio, 5 Duplex, 3 Triplex

        System.out.println("=====Selamat Datang Di Sistem Booking Apart=====");
        System.out.println("Silahkan login terlebih dahulu");
        System.out.println("================================================");
        System.out.print("Masukkan Username: ");
        String key = input.nextLine();

        boolean found = false;
        int userIndex = -1; // Indeks pengguna yang sedang login
        for (int i = 0; i < usernames.length; i++) {
            if (usernames[i].equals(key)) {
                found = true;
                userIndex = i;
                break;
            }
        }

        if (found) {
            System.out.print("Masukkan password anda: ");
            String password = input.nextLine();

            if ((key.equals("User1") || key.equals("Gabriel") || key.equals("Mera")) && password.equals("123")) {
                System.out.println("Selamat masuk ke sistem");
            } else {
                System.out.println("Peringatan password anda salah!");
                return;
            }
        } else {
            System.out.println("Peringatan username anda salah!");
            return;
        }

        boolean selesai = false;
        while (!selesai) {
            System.out.println();
            System.out.println("Silahkan memilih tindakan Anda:");
            System.out.println("1. Pemesanan Kamar");
            System.out.println("2. Check-in");
            System.out.println("3. Check-out");
            System.out.println("4. Selesai");

            System.out.print("Pilih tindakan (1/2/3/4): ");
            int choice = input.nextInt();

            switch (choice) {
                case 1:
                    // Pemesanan Kamar
                    if (statusPemesanan.equals("Dipesan")) {
                        System.out.println("Anda sudah memesan kamar. Silakan check-in atau check-out terlebih dahulu.");
                        break;
                    }

                    System.out.print("Masukkan jumlah kamar yang ingin dipesan: ");
                    int jumlahKamar = input.nextInt();

                    for (int i = 0; i < jumlahKamar; i++) {
                        int hargapermalam = 0, jmlmalam, biayatambahan, totalbiaya;

                        System.out.println();
                        System.out.println("Tipe Kamar");
                        System.out.println("1 : Studio (Rp.100000)");
                        System.out.println("2 : Duplex (Rp.150000)");
                        System.out.println("3 : Triplex (Rp.200000)");

                        System.out.print("Masukkan tipe kamar yang diinginkan untuk kamar ke-" + (i + 1) + ": ");
                        int tipekamar = input.nextInt();

                        if (tipekamar >= 1 && tipekamar <= stokKamar.length && stokKamar[tipekamar - 1] > 0) {
                            // Ada stok kamar yang tersedia, izinkan pemesanan
                            stokKamar[tipekamar - 1]--; // Kurangi stok kamar yang dipesan
                        } else {
                            System.out.println("Maaf, kamar tipe ini sudah habis atau tipe kamar tidak valid.");
                            return;
                        }

                        System.out.print("Masukkan jumlah malam yang diinginkan untuk kamar ke-" + (i + 1) + ": ");
                        while (true) {
                            if (input.hasNextInt()) {
                                jmlmalam = input.nextInt();
                                if (jmlmalam > 0) {
                                    break; // Keluar dari perulangan jika input valid
                                } else {
                                    System.out.println("Jumlah malam harus lebih dari 0. Silakan coba lagi.");
                                }
                            } else {
                                System.out.print("Masukkan angka yang valid: ");
                                input.next(); // Hapus token tidak valid dari input
                            }
                        }

                        // Menghitung total biaya berdasarkan tipe kamar
                        switch (tipekamar) {
                            case 1:
                                bookings[userIndex][0 + (i * 7)] = "Kamar Tipe Studio";
                                hargapermalam = 100000;
                                break;
                            case 2:
                                bookings[userIndex][0 + (i * 7)] = "Kamar Tipe Duplex";
                                hargapermalam = 150000;
                                break;
                            case 3:
                                bookings[userIndex][0 + (i * 7)] = "Kamar Tipe Triplex";
                                hargapermalam = 200000;
                                break;
                            default:
                                System.out.println("Tipe kamar tidak valid.");
                                return;
                        }

                        bookings[userIndex][1] = "Jumlah Malam: " + jmlmalam;

                        totalbiaya = jmlmalam * hargapermalam;

                        bookings[userIndex][1 + (i * 7)] = "Tipe Kamar: " + bookings[userIndex][0 + (i * 7)];
                        bookings[userIndex][2 + (i * 7)] = "Jumlah Malam: " + jmlmalam;
                        bookings[userIndex][3 + (i * 7)] = "Harga per Malam: Rp." + hargapermalam;
                        bookings[userIndex][4 + (i * 7)] = "Total Biaya: Rp." + totalbiaya;

                        // Memproses tambahan fasilitas
                        System.out.print("Ingin tambahan fasilitas (1: Laundry, 2: Sarapan, 3: Tidak ada) untuk kamar ke-" + (i + 1) + "? ");
                        int tambahan = input.nextInt();
                        if (tambahan == 1) {
                            biayatambahan = 20000 * jmlmalam; // Biaya laundry
                            totalbiaya += biayatambahan;
                            bookings[userIndex][2 + (i * 7)] = "Biaya laundry: Rp." + biayatambahan;
                        } else if (tambahan == 2) {
                            biayatambahan = 25000 * jmlmalam; // Biaya sarapan
                            totalbiaya += biayatambahan;
                            bookings[userIndex][2 + (i * 7)] = "Biaya sarapan: Rp." + biayatambahan;
                        } else if (tambahan != 3) {
                            System.out.println("Tambahan fasilitas tidak valid.");
                            return;
                        }

                        System.out.println("Harga yang harus dibayarkan untuk kamar ke-" + (i + 1) + " adalah " + totalbiaya);

                        System.out.println("Pilih Opsi Pembayaran:");
                        System.out.println("1. Cash");
                        System.out.println("2. Transfer Bank");
                        System.out.print("Masukkan Pilihan Pembayaran untuk kamar ke-" + (i + 1) + ": ");
                        int paymentChoice = input.nextInt();
                        input.nextLine();

                        switch (paymentChoice) {
                            case 1:
                                bookings[userIndex][5 + (i * 7)] = "Pembayaran: Cash";
                                break;
                            case 2:
                                bookings[userIndex][5 + (i * 7)] = "Pembayaran: Transfer Bank";
                                break;
                            default:
                                System.out.println("Pilihan Pembayaran tidak valid.");
                                return;
                        }

                        // Lanjutkan dengan kode promo
                        boolean promoAktif = false;
                        while (true) {
                            System.out.print("Apakah Anda ingin mengaktifkan promo untuk kamar ke-" + (i + 1) + "? (Ya/Tidak): ");
                            String promoChoice = input.next();
                            if (promoChoice.equalsIgnoreCase("Ya") || promoChoice.equalsIgnoreCase("Tidak")) {
                                if (promoChoice.equalsIgnoreCase("Ya")) {
                                    System.out.print("Berapa jumlah malam yang Anda pesan untuk kamar ke-" + (i + 1) + "? ");
                                    int jmlMalam = input.nextInt();
                                    if (jmlMalam >= 3) {
                                        double diskon = 0.1; // 10% diskon
                                        totalbiaya -= (totalbiaya * diskon);
                                        System.out.println("Anda mendapatkan diskon sebesar 10%.");
                                    }
                                    promoAktif = true;
                                    break;
                                } else {
                                    break;
                                }
                            } else {
                                System.out.println("Masukkan pilihan yang valid (Ya/Tidak).");
                            }
                        }

                        if (promoAktif) {
                            bookings[userIndex][6 + (i * 7)] = "Total biaya setelah promo: Rp." + totalbiaya;
                        }

                        System.out.println("Harga yang harus dibayarkan untuk kamar ke-" + (i + 1) + " adalah " + totalbiaya);

                        statusPemesanan = "Dipesan";
                    }
                    break;
                case 2:
                    // Check-in
                    if (statusPemesanan.equals("Dipesan") && statusCheckIn.equals("belum")) {
                        System.out.println();
                        System.out.println("Selamat Datang Tamu yang terhormat");
                        System.out.println("Status Anda sudah memesan kamar");
                        System.out.println();
                        System.out.println("Username: " + usernames[userIndex]);
                        System.out.println("Tipe Kamar: " + bookings[userIndex][0]);
                        System.out.println(bookings[userIndex][1]);
                        System.out.println(bookings[userIndex][2]);
                        System.out.println(bookings[userIndex][5]);
                        System.out.println("Status Pemesanan: " + statusPemesanan);

                        statusCheckIn = "sudah";
                    } else if (statusPemesanan.equals("BelumDipesan")) {
                        System.out.println("Anda belum memesan kamar. Silakan pesan terlebih dahulu.");
                    } else {
                        System.out.println("Anda sudah check-in atau status pemesanan belum tersedia.");
                    }
                    break;
                case 3:
                    // Check-out
                    if (statusPemesanan.equals("Dipesan") && statusCheckIn.equals("belum")) {
                        System.out.println("Anda belum check-in. Silakan check-in terlebih dahulu.");
                    } else if (statusPemesanan.equals("Dipesan") && statusCheckIn.equals("sudah")) {
                        System.out.println();
                        System.out.println("Anda sudah check-out. Terima kasih!");
                        System.out.println("Bagaimana Pengalamanan anda memakai aplikasi kami?");
                        System.out.print("Beri rating (1-5): ");
                        int rating = input.nextInt();
                        if (rating >= 1 && rating <= 5) {
                            bookings[userIndex][6 + (i * 7)] = "Rating: " + rating;
                            input.nextLine(); // Menghapus karakter newline dari input sebelumnya
                            System.out.print("Tulis ulasan: ");
                            String ulasan = input.nextLine();
                            bookings[userIndex][6 + (i * 7)] = "Ulasan: " + ulasan;

                            statusPemesanan = "BelumDipesan";
                            statusCheckIn = "belum";
                        } else {
                            System.out.println("Rating tidak valid.");
                            return;
                        }
                    } else if (statusPemesanan.equals("BelumDipesan")) {
                        System.out.println("Anda belum memesan kamar. Silakan pesan terlebih dahulu.");
                    } else {
                        System.out.println("Anda belum check-in atau status pemesanan belum tersedia.");
                    }
                    break;
                case 4:
                    selesai = true;
                    break;
                default:
                    System.out.println("Pilihan tidak valid. Silakan pilih kembali.");
            }
        }
    }
}
