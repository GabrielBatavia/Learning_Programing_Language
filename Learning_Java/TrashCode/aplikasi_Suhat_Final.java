import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Scanner;
import java.util.Calendar;
import java.util.Random;
import java.util.Date;
import java.util.HashMap;
import java.util.InputMismatchException;
import java.util.Map;

class User {
    String namaPengguna;
    String sandi;
    Booking booking;
    String namaLengkap;
    String alamat;
    Date tanggalLahir;
    String nik; // Nomor Induk Kependudukan
    Membership membership;

    Date membershipActivationDate;
    Date membershipExpirationDate;

    public void activateMembership() {
        Calendar calendar = Calendar.getInstance();
        this.membershipActivationDate = calendar.getTime(); // tanggal sekarang
        calendar.add(Calendar.MONTH, 1); // tambah 1 bulan
        this.membershipExpirationDate = calendar.getTime();
        this.membership.isActive = true;
    }

    public boolean isMembershipActive() {
        Date currentDate = new Date();
        return this.membership.isActive && currentDate.before(this.membershipExpirationDate);
    }



    User(String namaPengguna, String sandi, String namaLengkap, String alamat, Date tanggalLahir, String nik) {
        this.namaPengguna = namaPengguna;
        this.sandi = sandi;
        this.namaLengkap = namaLengkap;
        this.alamat = alamat;
        this.tanggalLahir = tanggalLahir;
        this.nik = nik;
        this.membership = new Membership(false, 0.1); // Diskon 10% untuk member
    }

}

class Booking {
    String tipeKamar;
    int jumlahMalam;
    String hariReservasi;
    String fasilitasTambahan;
    String metodePembayaran;
    String promo;
    int totalPembayaran;

    int nilai;
    String ulasan;
    String kritik;

    Booking(String tipeKamar, int jumlahMalam, String hariReservasi, String fasilitasTambahan, String metodePembayaran, int totalPembayaran, int nilai, String ulasan, String kritik) {
        this.tipeKamar = tipeKamar;
        this.jumlahMalam = jumlahMalam;
        this.hariReservasi = hariReservasi;
        this.fasilitasTambahan = fasilitasTambahan;
        this.metodePembayaran = metodePembayaran;
        this.totalPembayaran = totalPembayaran;
    }
}

class Membership {
    boolean isActive;
    double discountRate;

    Membership(boolean isActive, double discountRate) {
        this.isActive = isActive;
        this.discountRate = discountRate;
    }

    public boolean isActive() {
        return isActive;
    }

    public double getDiscountRate() {
        return discountRate;
    }
}

public class aplikasi_Suhat_Final  {
    private static final String ANSI_RESET = "\u001B[0m";
    private static final String ANSI_RED = "\u001B[31m";
    private static final String ANSI_GREEN = "\u001B[32m";
    private static final String ANSI_YELLOW = "\u001B[33m";
    private static final String ANSI_CYAN = "\u001B[36m";
    private static final String ANSI_BOLD = "\u001B[1m";
    private static final String ANSI_BLACK = "\u001B[30m";
    private static final String ANSI_BLUE = "\u001B[34m";
    private static final String ANSI_PURPLE = "\u001B[35m";
    private static final String ANSI_WHITE = "\u001B[37m";
    
    // Tambahkan informasi akun admin
    private static final String ADMIN_namaPengguna = "admin";
    private static final String ADMIN_Sandi = "admin123";

    private static final String STATUS_PENDING_CHECKIN = "pending check-in";
    private static final String STATUS_APPROVED_CHECKIN = "approved check-in";
    private static final String STATUS_PENDING_CHECKOUT = "pending checkout";
    private static final String STATUS_APPROVED_CHECKOUT = "approved checkout";
    
    private static ArrayList<String> registerednamaPengguna = new ArrayList<>();
    private static String[][] bookings = new String[11][6]; // Contoh: 10 pemesanan, dengan 5 informasi per pemesanan

    private static ArrayList<String> unavailableDates = new ArrayList<>();


    private static void initializeUnavailableDates() {
        Calendar calendar = Calendar.getInstance();
        int currentYear = calendar.get(Calendar.YEAR);
    
        // Loop melalui 12 bulan
        for (int month = 0; month < 12; month++) {
            String date = String.format("%02d/%02d/%04d", 25, month + 1, currentYear);
            unavailableDates.add(date);
        }
    }
  

    private static int authenticateUser(ArrayList<String> namaPengguna, ArrayList<String> sandi, String namaPenggunaInput, String SandiInput) {
        if (namaPengguna.contains(namaPenggunaInput)) {
            int userIndex = namaPengguna.indexOf(namaPenggunaInput);
            if (sandi.get(userIndex).equals(SandiInput)) {
                System.out.println("Selamat datang, " + namaPenggunaInput + "!");
                return userIndex;
            }
        }
        System.out.println(ANSI_RED + "Nama Pengguna atau sandi salah. Silakan coba lagi." + ANSI_RESET);
        return -1;
    }

    private static boolean isValidDate(String dateStr) {
        SimpleDateFormat sdf = new SimpleDateFormat("dd/MM/yyyy");
        sdf.setLenient(false);
    
        try {
            Date date = sdf.parse(dateStr); // Parse the input date
            Date currentDate = new Date(); // Get the current date
    
            // Check if the date is in the past or more than 2 years in the future
            if (date.before(currentDate)) {
                System.out.println(ANSI_RED + "Tanggal tidak bisa sebelum hari ini." + ANSI_RESET);
                return false;
            }
    
            Calendar calendar = Calendar.getInstance();
            calendar.setTime(currentDate);
            calendar.add(Calendar.YEAR, 2); // Add 2 years to the current date
            Date twoYearsLater = calendar.getTime();
    
            if (date.after(twoYearsLater)) {
                System.out.println(ANSI_RED + "Tanggal tidak bisa lebih dari 2 tahun dari sekarang." + ANSI_RESET);
                return false;
            }
    
            return true; // Date is valid
        } catch (ParseException e) {
            return false; // Date is invalid
        }
    }

    

    private static void registerUser(ArrayList<String> namaPengguna, ArrayList<String> sandi, ArrayList<User> users, Scanner input) {
        System.out.println("════════════════════════════════════════════════════════");
        System.out.print("Masukkan Nama Lengkap               : ");
        String namaLengkap = input.nextLine();
        System.out.print("Masukkan Alamat                     : ");
        String alamat = input.nextLine();
        System.out.print("Masukkan Tanggal Lahir (dd/MM/yyyy) : ");
        String birthDateString = input.nextLine();
        SimpleDateFormat sdf = new SimpleDateFormat("dd/MM/yyyy");
        Date tanggalLahir = null;
        try {
            tanggalLahir = sdf.parse(birthDateString); // Mengonversi string ke objek Date
        } catch (ParseException e) {
            System.out.println("Format tanggal salah. Gunakan format dd/MM/yyyy.");
            return; // Keluar dari metode jika parsing gagal
        }
        System.out.print("Masukkan NIK                        : ");
        String nik = input.nextLine();
        System.out.println("════════════════════════════════════════════════════════");

        // Validasi NIK
        if (nik.length() != 16 || !nik.matches("\\d+")) {
            System.out.println("NIK harus berupa 16 digit angka. Silakan coba lagi.");
            return; // Keluar dari metode jika NIK tidak valid
        }
    
        System.out.print("Masukkan Nama Pengguna  : ");
        String namaPenggunabaru = input.nextLine();
        
        if (namaPenggunabaru.contains(namaPenggunabaru)) {
            System.out.print("Masukkan Sandi          : ");
            String sandiBaru = input.nextLine();
        
            // Enkripsi atau hash Sandi dan NIK di sini
    
            namaPengguna.add(namaPenggunabaru);
            sandi.add(sandiBaru);
    
            users.add(new User(namaPenggunabaru, sandiBaru, namaLengkap, alamat, tanggalLahir, nik)); // Tambahkan user baru dengan informasi lengkap
        
            System.out.println(ANSI_GREEN + "Data Anda aman dan dilindungi. Akun berhasil dibuat! Silakan login."+ ANSI_RESET);
        } else {
            System.out.println(ANSI_RED + "Nama Pengguna sudah digunakan. Silakan pilih Nama Pengguna lain." + ANSI_RESET);
        }
    }

    public static void approveCheckIn(String namaPengguna) {
        // Mencari pengguna dengan namaPengguna
        for (String[] booking : bookings) {
            if (booking[0].equals(namaPengguna) && booking[9].equals("pending")) {
                booking[9] = "sudah"; // Menyetujui check-in
                System.out.println("Check-In untuk " + namaPengguna + " telah disetujui.");
            }
        }
    }

    public static void approveCheckOut(String namaPengguna) {
        // Mencari pengguna dengan namaPengguna
        for (String[] booking : bookings) {
            if (booking != null && booking[0] != null && booking[0].equals(namaPengguna) && booking[9].equals("pending checkout")) {
                booking[9] = "telah check-out"; // Menyetujui check-out
                System.out.println("Check-Out untuk " + namaPengguna + " telah disetujui.");
            }
        }
    }


    public static String makeBooking(ArrayList<User> users, int[] stockRooms, String[][] bookings, int userIndex, Scanner input) {
        int hargapermalam = 0, jmlmalam, biayatambahan, totalbiaya;

        String statusReservasi = "gagal";

        // Stylized banner for selecting room type
        System.out.println("╔═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗");
        System.out.println(  "║"+ANSI_CYAN+"                               ░█▀█░▀█▀░█░░░▀█▀░█░█░█▀█░█▀█░░░▀█▀░▀█▀░█▀█░█▀▀░░░█░█░█▀█░█▄█░█▀█░█▀▄                            "+ANSI_RESET+"║");
        System.out.println(  "║"+ANSI_CYAN+"                               ░█▀▀░░█░░█░░░░█░░█▀█░█▀█░█░█░░░░█░░░█░░█▀▀░█▀▀░░░█▀▄░█▀█░█░█░█▀█░█▀▄                            "+ANSI_RESET+"║");        
        System.out.println(  "║"+ANSI_CYAN+"                               ░▀░░░▀▀▀░▀▀▀░▀▀▀░▀░▀░▀░▀░▀░▀░░░░▀░░▀▀▀░▀░░░▀▀▀░░░▀░▀░▀░▀░▀░▀░▀░▀░▀░▀                            "+ANSI_RESET+"║");
        System.out.println("║═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════║");
        System.out.println(  "║"+ANSI_BOLD+"   1 : Studio (Rp.100000)                                                                                                      ║");                                         
        System.out.println("║    -------------------------------                                                                                            ║");
        System.out.println("║       Spesifikasi: Single bed, TV, AC                                                                                         ║");
        System.out.println("║       Fasilitas   : Free Wi-Fi, Toiletries                                                                                    ║");
        System.out.println("║   2 : Duplex (Rp.150000)                                                                                                      ║");
        System.out.println("║    -------------------------------                                                                                            ║");
        System.out.println("║       Spesifikasi: Double bed, TV, AC, Mini Kitchen                                                                           ║");
        System.out.println("║       Fasilitas   : Free Wi-Fi, Toiletries, Room Service                                                                      ║"); 
        System.out.println("║   3 : Triplex (Rp.200000)                                                                                                     ║");
        System.out.println("║    -------------------------------                                                                                            ║");
        System.out.println("║       Spesifikasi: Queen bed, TV, AC, Kitchen, Jacuzzi                                                                        ║");
        System.out.println(  "║       Fasilitas   : Free Wi-Fi, Toiletries, Room Service, Spa Access                                                          "+ANSI_RESET+"║");
        System.out.println("╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝");

        System.out.println(ANSI_CYAN + "Pilihan Tipe Kamar dan Ketersediaan:" + ANSI_RESET);
        System.out.println("1 : Studio  (Tersedia : " + stockRooms[0] + ")");
        System.out.println("2 : Duplex  (Tersedia : " + stockRooms[1] + ")");
        System.out.println("3 : Triplex (Tersedia : " + stockRooms[2] + ")");

        System.out.print("Masukkan tipe kamar yang diinginkan : ");
        int tipekamar = input.nextInt();

        // Pilihan berapa jumlah kamar
        System.out.println("╔═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗"); 
        System.out.println(  "║"+ANSI_CYAN+"           ░█▀█░▀█▀░█░░░▀█▀░█░█░█▀█░█▀█░░░▀▀█░█░█░█▄█░█░░░█▀█░█░█░░░█▀▄░█▀█░█▀█░█░█░▀█▀░█▀█░█▀▀░░░█░█░█▀█░█▄█░█▀█░█▀▄          "+ANSI_RESET+"║");
        System.out.println(  "║"+ANSI_CYAN+"           ░█▀▀░░█░░█░░░░█░░█▀█░█▀█░█░█░░░░░█░█░█░█░█░█░░░█▀█░█▀█░░░█▀▄░█░█░█░█░█▀▄░░█░░█░█░█░█░░░█▀▄░█▀█░█░█░█▀█░█▀▄          "+ANSI_RESET+"║");
        System.out.println(  "║"+ANSI_CYAN+"           ░▀░░░▀▀▀░▀▀▀░▀▀▀░▀░▀░▀░▀░▀░▀░░░▀▀░░▀▀▀░▀░▀░▀▀▀░▀░▀░▀░▀░░░▀▀░░▀▀▀░▀▀▀░▀░▀░▀▀▀░▀░▀░▀▀▀░░░▀░▀░▀░▀░▀░▀░▀░▀░▀░           "+ANSI_RESET+"║");
        System.out.println("╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝");

        System.out.print("Berapa banyak Kamar yang anda Inginkan : " );
        int banyakkamar = input.nextInt();

        if (banyakkamar < 1) {
            System.out.println(ANSI_RED + "Kamu tidak bisa memesan 0 kamar" + ANSI_RESET);
            return "gagal";
        } else if (banyakkamar > stockRooms[tipekamar - 1]) {
            System.out.println(ANSI_RED + "Maaf, hanya tersedia " + stockRooms[tipekamar - 1] + " kamar untuk tipe ini." + ANSI_RESET);
            return "gagal";
        }

        stockRooms[tipekamar - 1] -= banyakkamar; // Mengurangi ketersediaan kamar berdasarkan jumlah yang dipesan
        
        // Stylized banner for entering the number of nights
        System.out.println("╔═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗");
        System.out.println(  "║   "+ANSI_CYAN+"                     ░█▄█░█▀█░█▀▀░█░█░█░█░█░█░█▀█░█▀█░░░▀▀█░█░█░█▄█░█░░░█▀█░█░█░░░█▄█░█▀█░█░░░█▀█░█▄█                       "+ANSI_RESET+"║");
        System.out.println(  "║   "+ANSI_CYAN+"                     ░█░█░█▀█░▀▀█░█░█░█▀▄░█▀▄░█▀█░█░█░░░░░█░█░█░█░█░█░░░█▀█░█▀█░░░█░█░█▀█░█░░░█▀█░█░█                       "+ANSI_RESET+"║");
        System.out.println(  "║   "+ANSI_CYAN+"                     ░▀░▀░▀░▀░▀▀▀░▀▀▀░▀░▀░▀░▀░▀░▀░▀░▀░░░▀▀░░▀▀▀░▀░▀░▀▀▀░▀░▀░▀░▀░░░▀░▀░▀░▀░▀▀▀░▀░▀░▀░▀                       "+ANSI_RESET+"║");
        System.out.println("╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝" );
        System.out.print("Masukkan jumlah malam yang diinginkan : ");
        while (true) {
            if (input.hasNextInt()) {
                jmlmalam = input.nextInt();
                if (jmlmalam > 0) {
                    break; // Exit the loop if the input is valid
                } else {
                    System.out.println(ANSI_RED + "Jumlah malam harus lebih dari 0. Silakan coba lagi." + ANSI_RESET);
                }
            } else {
                System.out.print(ANSI_RED + "Masukkan angka yang valid : " + ANSI_RESET);
                input.next(); // Discard the invalid token from the input
            }
        }
        bookings[userIndex][7] = "" + jmlmalam;

        // Calculate total cost based on room type
        switch (tipekamar) {
            case 1:
                bookings[userIndex][0] = "Kamar Tipe Studio";
                hargapermalam = 100000 * banyakkamar;
                break;
            case 2:
                bookings[userIndex][0] = "Kamar Tipe Duplex";
                hargapermalam = 150000 * banyakkamar;
                break;
            case 3:
                bookings[userIndex][0] = "Kamar Tipe Triplex";
                hargapermalam = 200000 * banyakkamar;
                break;
            default:
                System.out.println(ANSI_RED + "Tipe kamar tidak valid." + ANSI_RESET);
                return "gagal";
        }

        bookings[userIndex][1] = "Jumlah Malam      : " + jmlmalam;

        totalbiaya = jmlmalam * hargapermalam;
        boolean tambahanLain = true;

        //displayCalendar();
        displayCalendar(input); // Pass 'input' to 'displayCalendar' method

         // Stylized banner for entering the reservation date
         System.out.println("╔═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗");
         System.out.println(  "║   "+ANSI_CYAN+"                ░█▀█░▀█▀░█░░░▀█▀░█░█░░░▀█▀░█▀█░█▀█░█▀▀░█▀▀░█▀█░█░░░░░█▀▄░█▀▀░█▀▀░█▀▀░█▀▄░█░█░█▀█░█▀▀░▀█▀                    "+ANSI_RESET+"║");
         System.out.println(  "║   "+ANSI_CYAN+"                ░█▀▀░░█░░█░░░░█░░█▀█░░░░█░░█▀█░█░█░█░█░█░█░█▀█░█░░░░░█▀▄░█▀▀░▀▀█░█▀▀░█▀▄░▀▄▀░█▀█░▀▀█░░█░                    "+ANSI_RESET+"║");
         System.out.println(  "║   "+ANSI_CYAN+"                ░▀░░░▀▀▀░▀▀▀░▀▀▀░▀░▀░░░░▀░░▀░▀░▀░▀░▀▀▀░▀▀▀░▀░▀░▀▀▀░░░▀░▀░▀▀▀░▀▀▀░▀▀▀░▀░▀░░▀░░▀░▀░▀▀▀░▀▀▀                    "+ANSI_RESET+"║");
         System.out.println("╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝");
        String reservationDate;
        while (true) {
        System.out.print("Masukkan tanggal reservasi (dd/mm/yyyy): ");
        reservationDate = input.next();
        if (isValidDate(reservationDate) && !unavailableDates.contains(reservationDate)) {
            break; // Keluar dari loop jika tanggal valid dan tersedia
        } else {
            System.out.println(ANSI_RED + "Tanggal tidak tersedia atau tidak valid. Silakan coba lagi." + ANSI_RESET);
        }
    }
         bookings[userIndex][1] = " " + reservationDate;

        // Stylized banner for additional facilities
        while (tambahanLain) {
            System.out.println( "╔═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗");
            System.out.println(   "║"+ANSI_CYAN+"                 ░█▀█░▀█▀░█░░░▀█▀░█░█░█▀█░█▀█░░░▀█▀░█▀█░█▄█░█▀▄░█▀█░█░█░░░█▀▀░█▀█░█▀▀░▀█▀░█░░░▀█▀░▀█▀░█▀█░█▀▀                  "+ANSI_RESET+"║");
            System.out.println(   "║"+ANSI_CYAN+"                 ░█▀▀░░█░░█░░░░█░░█▀█░█▀█░█░█░░░░█░░█▀█░█░█░█▀▄░█▀█░█▀█░░░█▀▀░█▀█░▀▀█░░█░░█░░░░█░░░█░░█▀█░▀▀█                  "+ANSI_RESET+"║");
            System.out.println(   "║"+ANSI_CYAN+"                 ░▀░░░▀▀▀░▀▀▀░▀▀▀░▀░▀░▀░▀░▀░▀░░░░▀░░▀░▀░▀░▀░▀▀░░▀░▀░▀░▀░░░▀░░░▀░▀░▀▀▀░▀▀▀░▀▀▀░▀▀▀░░▀░░▀░▀░▀▀▀                  "+ANSI_RESET+"║");
            System.out.println( "╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝");
            System.out.println("1 : Laundry (Rp.20,000 per malam)");
            System.out.println("2 : Sarapan (Rp.25,000 per malam)");
            System.out.println("3 : Selesai");

            System.out.print("Pilih tambahan fasilitas (1/2/3) : ");
            int tambahan = input.nextInt();

            if (tambahan == 1) {
                biayatambahan = 20000 * jmlmalam; // Laundry cost
                totalbiaya += biayatambahan * banyakkamar;
                bookings[userIndex][2] = "laundry";
            } else if (tambahan == 2) {
                biayatambahan = 25000 * jmlmalam; // Breakfast cost
                totalbiaya += biayatambahan * banyakkamar;
                bookings[userIndex][11] = "sarapan";
            } else if (tambahan == 3) {
                tambahanLain = false; // Exit the loop if the user chooses to finish
            } else {
                System.out.println(ANSI_RED + "Tambahan fasilitas tidak valid." + ANSI_RESET);
                return "gagal";
            }
        }

        // Stylized banner for displaying the total price
        System.out.println("" + ANSI_BOLD + "═══════════════════════");
        System.out.println("Tagihan = " + ANSI_YELLOW + "Rp. "+ totalbiaya + ANSI_RESET);
        System.out.println("═══════════════════════");

        // Stylized banner for payment options
        System.out.println("╔═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗");
        System.out.println(  "║"+ANSI_CYAN+"                        ░█▀█░▀█▀░█░░░▀█▀░█░█░░░█▀█░█▀█░█▀▀░▀█▀░░░█▀█░█▀▀░█▄█░█▀▄░█▀█░█░█░█▀█░█▀▄░█▀█░█▀█                       "+ANSI_RESET+"║");
        System.out.println(  "║"+ANSI_CYAN+"                        ░█▀▀░░█░░█░░░░█░░█▀█░░░█░█░█▀▀░▀▀█░░█░░░░█▀▀░█▀▀░█░█░█▀▄░█▀█░░█░░█▀█░█▀▄░█▀█░█░█                       "+ANSI_RESET+"║");
        System.out.println(  "║"+ANSI_CYAN+"                        ░▀░░░▀▀▀░▀▀▀░▀▀▀░▀░▀░░░▀▀▀░▀░░░▀▀▀░▀▀▀░░░▀░░░▀▀▀░▀░▀░▀▀░░▀░▀░░▀░░▀░▀░▀░▀░▀░▀░▀░▀                       "+ANSI_RESET+"║");                    
        System.out.println("╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝");
        System.out.println("1. Cash");
        System.out.println("2. Transfer Bank");
        System.out.print("Masukkan Pilihan Pembayaran : ");
        int paymentChoice = input.nextInt();
        input.nextLine(); // Consume the newline character

        switch (paymentChoice) {
            case 1:
                bookings[userIndex][5] = "Cash";
                break;
            case 2:
                bookings[userIndex][5] = "Transfer Bank";

                System.out.println("" + ANSI_BOLD + "═══════════════════════");
                System.out.println("NO VA : 23457654345678 "+ANSI_RESET+"");
                System.out.println("═══════════════════════");
                break;
            default:
                System.out.println(ANSI_RED + "Pilihan Pembayaran tidak valid."+ ANSI_RESET);
                return "gagal";
        }

        // Continue with promo code logic
        boolean promoAktif = false;
        while (true) {
            // Stylized banner for promo code activation
            System.out.println("╔═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗");
            System.out.println(  "║"+ANSI_CYAN+"       ░█▀█░█░█░▀█▀░▀█▀░█░█░█▀█░█▀▀░▀█▀░░░█▀█░█▀▄░█▀█░█▄█░█▀█░░░█▀█░█▀▀░█▄█░█▀▀░█▀▀░█▀█░█▀█░█▀█░█▀█░░░█░█░█▀█░█▄█░█▀█░█▀▄      "+ANSI_RESET+"║");
            System.out.println(  "║"+ANSI_CYAN+"       ░█▀█░█▀▄░░█░░░█░░▀▄▀░█▀█░▀▀█░░█░░░░█▀▀░█▀▄░█░█░█░█░█░█░░░█▀▀░█▀▀░█░█░█▀▀░▀▀█░█▀█░█░█░█▀█░█░█░░░█▀▄░█▀█░█░█░█▀█░█▀▄      "+ANSI_RESET+"║");
            System.out.println(  "║"+ANSI_CYAN+"       ░▀░▀░▀░▀░░▀░░▀▀▀░░▀░░▀░▀░▀▀▀░▀▀▀░░░▀░░░▀░▀░▀▀▀░▀░▀░▀▀▀░░░▀░░░▀▀▀░▀░▀░▀▀▀░▀▀▀░▀░▀░▀░▀░▀░▀░▀░▀░░░▀░▀░▀░▀░▀░▀░▀░▀░▀░▀      "+ANSI_RESET+"║");
            System.out.println("╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝");
            System.out.print("Apakah Anda ingin mengaktifkan promo? (Ya/Tidak) : ");

            String promoChoice = input.next();
            if (promoChoice.equalsIgnoreCase("Ya") || promoChoice.equalsIgnoreCase("Tidak")) {
                if (promoChoice.equalsIgnoreCase("Ya")) {

                    if (users.get(userIndex).isMembershipActive()) {
                        double discount = totalbiaya * users.get(userIndex).membership.getDiscountRate();
                        totalbiaya -= discount;
                        System.out.println("Diskon keanggotaan diterapkan, Anda mendapatkan Diskon sebesar : Rp. " + discount);
                    }

                        System.out.print("Apakah Anda memiliki kode diskon? (Ya/Tidak) : ");
                        String hasDiscount = input.next();
                        input.nextLine(); // Consume newline

                        if (hasDiscount.equalsIgnoreCase("Ya")) {
                            System.out.print("Masukkan Kode Diskon : ");
                            String discountCode = input.nextLine();

                            if (discounts.containsKey(discountCode)) {
                                double discountPercentage = discounts.get(discountCode);
                                int discountAmount = (int) (totalbiaya * discountPercentage);
                                totalbiaya -= discountAmount;
                                System.out.println("Diskon sebesar Rp." + discountAmount + " telah diterapkan.");
                            } else {
                                System.out.println("Kode Diskon tidak valid.");
                            }
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
            bookings[userIndex][6] = "Total biaya setelah promo : Rp. " + totalbiaya;
        }

        // Stylized banner for displaying the total price
        System.out.println("╔══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗");
        System.out.println(  "║"+ANSI_CYAN+"░█░█░█▀█░█▀▄░█▀▀░█▀█░░░█░█░█▀█░█▀█░█▀▀░░░█░█░█▀█░█▀▄░█░█░█▀▀░░░█▀▄░▀█▀░░░█▀▄░█▀█░█░█░█▀█░█▀▄░█░█░█▀█░█▀█░░░█▀█░█▀▄░█▀█░█░░░█▀█░█░█"+ANSI_RESET+"║");
        System.out.println(  "║"+ANSI_CYAN+"░█▀█░█▀█░█▀▄░█░█░█▀█░░░░█░░█▀█░█░█░█░█░░░█▀█░█▀█░█▀▄░█░█░▀▀█░░░█░█░░█░░░░█▀▄░█▀█░░█░░█▀█░█▀▄░█▀▄░█▀█░█░█░░░█▀█░█░█░█▀█░█░░░█▀█░█▀█"+ANSI_RESET+"║");
        System.out.println(  "║"+ANSI_CYAN+"░▀░▀░▀░▀░▀░▀░▀▀▀░▀░▀░░░░▀░░▀░▀░▀░▀░▀▀▀░░░▀░▀░▀░▀░▀░▀░▀▀▀░▀▀▀░░░▀▀░░▀▀▀░░░▀▀░░▀░▀░░▀░░▀░▀░▀░▀░▀░▀░▀░▀░▀░▀░░░▀░▀░▀▀░░▀░▀░▀▀▀░▀░▀░▀░▀"+ANSI_RESET+"║");
        System.out.println("╚══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝");
        System.out.println(ANSI_YELLOW + "Rp. " + totalbiaya +ANSI_RESET);

        Random random = new Random();
        int uniqueCode = random.nextInt(900) + 100; // Menghasilkan angka acak antara 100 dan 999
    
        int totalCostWithUniqueCode = totalbiaya + uniqueCode;
        bookings[userIndex][6] = String.valueOf(totalCostWithUniqueCode);

        printPaymentReceipt(bookings, userIndex, uniqueCode);
        statusReservasi = "berhasil";

        
        return statusReservasi;

    }

    private static void printPaymentReceipt(String[][] bookings, int userIndex, int uniqueCode) {
        System.out.println("" + ANSI_BOLD + "═════════════════════ STRUK PEMBAYARAN ═════════════════════");
        System.out.println("Metode Pembayaran                   : " + bookings[userIndex][5]);
        System.out.println("Kode Unik Pembayaran                : " + uniqueCode);
        System.out.println("Total Biaya (termasuk kode unik)    : Rp." + bookings[userIndex][6]);
        System.out.println("════════════════════════════════════════════════════════════");
    }
    
    private static void displayCalendar(Scanner input) {
        System.out.println("╔═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗");
        System.out.println(  "║"+ANSI_CYAN+"                         ░█░█░█▀▀░▀█▀░█▀▀░█▀▄░█▀▀░█▀▀░█▀▄░▀█▀░█▀█░█▀█░█▀█░░░▀█▀░█▀█░█▀█░█▀▀░█▀▀░█▀█░█░░                        "+ANSI_RESET+"║");
        System.out.println(  "║"+ANSI_CYAN+"                         ░█▀▄░█▀▀░░█░░█▀▀░█▀▄░▀▀█░█▀▀░█░█░░█░░█▀█░█▀█░█░█░░░░█░░█▀█░█░█░█░█░█░█░█▀█░█░                         "+ANSI_RESET+"║");
        System.out.println(  "║"+ANSI_CYAN+"                         ░▀░▀░▀▀▀░░▀░░▀▀▀░▀░▀░▀▀▀░▀▀▀░▀▀░░▀▀▀░▀░▀░▀░▀░▀░▀░░░░▀░░▀░▀░▀░▀░▀▀▀░▀▀▀░▀░▀░▀▀▀                        "+ANSI_RESET+"║");
        System.out.println("╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝");
    
        System.out.println("\n"+ ANSI_CYAN + "═════════════════════════════");

        // Get the current date
        Calendar calendar = Calendar.getInstance();
        int currentMonth = calendar.get(Calendar.MONTH);
        int currentYear = calendar.get(Calendar.YEAR);
    
        // Set the calendar to the first day of the current month
        calendar.set(currentYear, currentMonth, 1);
    
        // Find the day of the week for the first day of the month
        int firstDayOfWeek = calendar.get(Calendar.DAY_OF_WEEK);
    
        // Print the calendar header
        System.out.println("Sun Mon Tue Wed Thu Fri Sat");
    
        // Print leading spaces for the first week
        for (int i = Calendar.SUNDAY; i < firstDayOfWeek; i++) {
            System.out.print("    ");
        }
    
        // Print the days of the month
        // Print the days of the month
        while (calendar.get(Calendar.MONTH) == currentMonth) {
            int dayOfMonth = calendar.get(Calendar.DAY_OF_MONTH);
            String formattedDate = String.format("%02d/%02d/%04d", dayOfMonth, currentMonth + 1, currentYear);

            boolean isAvailable = !unavailableDates.contains(formattedDate);
            System.out.printf("%3d", dayOfMonth);
            System.out.print(isAvailable ? " " : ANSI_RED + "X" + ANSI_RESET);

            // Move to the next day
            calendar.add(Calendar.DAY_OF_MONTH, 1);

            // Start a new line for the next week
            if (calendar.get(Calendar.DAY_OF_WEEK) == Calendar.SUNDAY) {
                System.out.println();
            }
        }

        System.out.println("\n"+ ANSI_CYAN + "═════════════════════════════" + ANSI_RESET+"\n");
}

    public static void viewRegisteredUsers(ArrayList<User> users) {
        if (users.isEmpty()) {
            System.out.println("Tidak ada pengguna yang terdaftar.");
            return;
        }
    
        System.out.print("Daftar Nama Pengguna Terdaftar : ");
        for (User user : users) {
            System.out.println(registerednamaPengguna);
        }
    }

    public static void viewUserDetails(ArrayList<User> users, Scanner input) {
        System.out.print("Masukkan Nama pengguna : ");
        String namaPengguna = input.nextLine();
    
        for (User user : users) {
            if (namaPengguna.equals(namaPengguna)) {
                System.out.println("Nama Lengkap   : " + user.namaLengkap);
                System.out.println("Alamat         : " + user.alamat);
                // Format tanggal sesuai kebutuhan
                SimpleDateFormat sdf = new SimpleDateFormat("dd/MM/yyyy");
                System.out.println("Tanggal Lahir  : " + sdf.format(user.tanggalLahir));
                System.out.println("NIK            : " + user.nik);
                System.out.println("Membership     : " + user.membership);
                return;
            }
        }
    
        System.out.println(ANSI_RED +"Nama Pengguna tidak ditemukan."+ ANSI_RESET );
    }

    public static void deleteUser(ArrayList<User> users, ArrayList<String> namaPengguna, Scanner input) {
        System.out.print("Masukkan Nama Pengguna yang akan dihapus : ");
        String namaPenggunabaru = input.nextLine();
    
        for (int i = 0; i < users.size(); i++) {
            if (users.get(i).namaPengguna.equals(namaPenggunabaru)) {
                users.remove(i);
                namaPengguna.remove(namaPengguna);
                System.out.println("Akun pengguna " + namaPengguna + " telah dihapus.");
                return;
            }
        }
    
        System.out.println(ANSI_RED +"Nama Pengguna tidak ditemukan."+ ANSI_RESET);
    }

    public static void userFeedback(ArrayList<User> users, String[][] bookings, int userIndex ) {
        for (int i = 0; i < bookings.length; i++) {
            if (bookings[i][0] != null) { // Pastikan bahwa pemesanan ada
                System.out.println("══════════════════════════════════════════");
                System.out.println("Nama Pengguna       : " + registerednamaPengguna.get(i));
                System.out.println("Tipe Kamar          : " + bookings[i][0]);
                System.out.println("Tanggal Pemesanan   :"+ bookings[i][1]);
                System.out.println("Fasilitas tambahan  : " + bookings[i][2] + " " + bookings[i][11]);
                System.out.println("Rating              : " + bookings[i][3]);
                System.out.println("Ulasan              : "+ bookings[i][4]);
                if (bookings[i][6] != null) {
                    System.out.println("Kritik/Saran        : " + bookings[i][6]);
                }
                System.out.println("══════════════════════════════════════════");
                }
            }
    }

    public static void approveCheckOut(ArrayList<User> users, String[][] bookings, ArrayList<String> registerednamaPengguna, Scanner input) {
        System.out.println("Approving Check-Out Requests : ");
        for (int i = 0; i < bookings.length; i++) {
            if (bookings[i] != null && bookings[i][8] != null && bookings[i][8].equals(STATUS_PENDING_CHECKOUT)) {
                System.out.println("Pending Check-Out for User : " + registerednamaPengguna.get(i));
            }
        }
        System.out.print("Enter Nama Pengguna to approve Check-Out : ");
        String namaPenggunaCheckOut = input.nextLine();
        boolean userFound = false;
        for (int i = 0; i < registerednamaPengguna.size(); i++) {
            if (registerednamaPengguna.get(i).equals(namaPenggunaCheckOut) && bookings[i] != null && bookings[i][8].equals(STATUS_PENDING_CHECKOUT)) {
                bookings[i][8] = STATUS_APPROVED_CHECKOUT;
                System.out.println("Check-Out approved for " + namaPenggunaCheckOut);
                userFound = true;
                break;
            }
        }
        if (!userFound) {
            System.out.println("No pending check-out found for the Nama Pengguna : " + namaPenggunaCheckOut);
        }
    }

    public static void approveCheckIn(ArrayList<User> users, String[][] bookings, ArrayList<String> registerednamaPengguna, Scanner input) {
        // Setujui check-in pengguna
        System.out.println("Approving Check-In Requests : ");
        for (int i = 0; i < bookings.length; i++) {
            if (bookings[i] != null && bookings[i][8] != null && bookings[i][8].equals(STATUS_PENDING_CHECKIN)) {
                System.out.println("Pending Check-In for User : " + registerednamaPengguna.get(i));
                }
            }
        System.out.print("Enter Nama Pengguna to approve Check-In : ");
        String namaPenggunaCheckIn = input.nextLine();
        boolean userFound = false;
        for (int i = 0; i < registerednamaPengguna.size(); i++) {
            if (registerednamaPengguna.get(i).equals(namaPenggunaCheckIn) && bookings[i] != null && bookings[i][8] != null && bookings[i][8].equals(STATUS_PENDING_CHECKIN)) {
                    bookings[i][8] = STATUS_APPROVED_CHECKIN;
                    System.out.println("Check-In approved for " + namaPenggunaCheckIn);
                    userFound = true;
                break;
            }
        }
            if (!userFound) {
                System.out.println("No pending check-in found for the Nama Pengguna : " + namaPenggunaCheckIn);
            }
    }

    public static void userInformation(ArrayList<User> users, String[][] bookings, int userIndex) {
 
        // Lihat informasi pemesanan pengguna
        System.out.println("╔═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗");
        System.out.println(  "║ "+ANSI_CYAN+"       ░▀█▀░█▀█░█▀▀░█▀█░█▀▄░█▄█░█▀█░█▀▀░▀█▀░░░█▀█░█▀▀░█▄█░█▀▀░█▀▀░█▀█░█▀█░█▀█░█▀█░░░█▀█░█▀▀░█▀█░█▀▀░█▀▀░█░█░█▀█░█▀█░░         "+ ANSI_RESET +"║");
        System.out.println(  "║ "+ANSI_CYAN+"       ░░█░░█░█░█▀▀░█░█░█▀▄░█░█░█▀█░▀▀█░░█░░░░█▀▀░█▀▀░█░█░█▀▀░▀▀█░█▀█░█░█░█▀█░█░█░░░█▀▀░█▀▀░█░█░█░█░█░█░█░█░█░█░█▀█░░         "+ ANSI_RESET +"║");
        System.out.println(  "║ "+ANSI_CYAN+"       ░▀▀▀░▀░▀░▀░░░▀▀▀░▀░▀░▀░▀░▀░▀░▀▀▀░▀▀▀░░░▀░░░▀▀▀░▀░▀░▀▀▀░▀▀▀░▀░▀░▀░▀░▀░▀░▀░▀░░░▀░░░▀▀▀░▀░▀░▀▀▀░▀▀▀░▀▀▀░▀░▀░▀░▀░░         "+ ANSI_RESET +"║");
        System.out.println("╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝" );
                    
        
        for (int i = 0; i < bookings.length; i++) {
            if (bookings[i][0] != null) {
                System.out.println("═══════════════════════════════════════");
                System.out.println("Nama Pengguna     : " + registerednamaPengguna.get(i));
                System.out.println("Tipe Kamar        : " + bookings[i][0]);
                System.out.println("Tanggal Pemesanan :"+bookings[i][1]);
                System.out.println("Fasilitas Tambahan  : " + bookings[userIndex][2] + " " + bookings[userIndex][11]);
                System.out.println("Pembayaran        : " + bookings[i][5]);
                System.out.println("Status Check-in   : " + (bookings[i][8] != null ? bookings[i][8] : "Belum Check-in"));
                System.out.println("═══════════════════════════════════════");
            }
        }        

    }
    
    private static HashMap<String, Double> discounts = new HashMap<>();

    private static void manageDiscounts(Scanner input) {
    System.out.println("Mengelola Diskon:");
    System.out.println("1. Tambah Diskon");
    System.out.println("2. Hapus Diskon");
    System.out.println("3. Lihat Diskon");
    int choice = input.nextInt();
    input.nextLine(); // Consume newline

    switch (choice) {
        case 1:
            // Tambah Diskon
            System.out.print("Masukkan Kode Diskon : ");
            String code = input.nextLine();
            System.out.print("Masukkan Persentase Diskon (contoh: 0.10 untuk 10%) : ");
            try {
                double percentage = input.nextDouble();
                if (percentage >= 0.0 && percentage <= 1.0) {
                    discounts.put(code, percentage);
                    System.out.println("Diskon ditambahkan.");
                } else {
                    System.out.println("Persentase diskon harus antara 0.0 dan 1.0.");
                }
            } catch (InputMismatchException e) {
                System.out.println("Masukkan format persentase yang benar.");
            }
            input.nextLine(); // Consume the rest of the line
            break;
        case 2:
            // Hapus Diskon
            System.out.print("Masukkan Kode Diskon untuk dihapus : ");
            String codeToDelete = input.nextLine();
            if (discounts.remove(codeToDelete) != null) {
                System.out.println("Diskon dihapus.");
            } else {
                System.out.println("Kode Diskon tidak ditemukan.");
            }
            break;
        case 3:
            // Lihat Diskon
            System.out.println("Daftar Diskon:");
            for (Map.Entry<String, Double> entry : discounts.entrySet()) {
                System.out.println("Kode : " + entry.getKey() + ", Diskon : " + (entry.getValue() * 100) + "%");
            }
            break;
        default:
            System.out.println("Pilihan tidak valid.");
            break;
        }
    }

    private static void handleMembership(User user, Scanner input) {
        if (!user.isMembershipActive()) {
            System.out.println("Anda belum menjadi member atau membership Anda telah kedaluwarsa.");
            System.out.println("Anda akan membeli membership dengan biaya Rp 200.000 per bulan.");
            System.out.print("Apakah Anda ingin melanjutkan? (Ya/Tidak) : ");
            String response = input.nextLine();
    
            if (response.equalsIgnoreCase("Ya")) {
                System.out.println("Silakan bayar biaya membership sekarang : Rp 200.000. ");
                System.out.print("Masukkan jumlah yang dibayar : ");
                int amount = input.nextInt();
                input.nextLine(); // Consume newline
    
                if (amount >= 200000) {
                    user.activateMembership(); // Metode ini akan menetapkan tanggal aktivasi dan kedaluwarsa
                    System.out.println(ANSI_GREEN + "Pembayaran berhasil. Membership Anda sekarang aktif hingga " + user.membershipExpirationDate + ANSI_RESET);
                } else {
                    System.out.println(ANSI_RED + "Pembayaran gagal. Jumlah yang dibayar tidak cukup." + ANSI_RESET);
                }
            } else {
                System.out.println("Pembelian membership dibatalkan.");
            }
        } else {
            System.out.println("Anda sudah menjadi member. Membership Anda aktif hingga " + user.membershipExpirationDate);
        }
    }


    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        ArrayList<User> users = new ArrayList<>();
        int[] stockRooms = {1, 5, 3}; // Misalnya: 1 Studio, 5 Duplex, 3 Triplex
        String[][] bookings = new String[4][12]; // Maksimal 4 pengguna, dan 7 informasi pemesanan per pengguna
        boolean[] pesananDiterima = new boolean[4]; // Sesuaikan dengan jumlah pengguna maksimal
        ArrayList<String> registeredSandis = new ArrayList<>();

        boolean isProgramRunning = true;
        User currentUser = null;
        boolean isAdminLoggedIn = false;

        boolean loggedIn = false;
        String statusPemesanan = "Belum Dipesan";
        String statusCheckIn = "belum";
        String statusReservasi = "gagal";

        initializeUnavailableDates();

        int userIndex = -1; // Declare userIndex here

        System.out.println("╔═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗");
        System.out.println("║   █████╗ ██████╗  █████╗ ██████╗ ████████╗███████╗███╗   ███╗███████╗███╗   ██╗    ███████╗██╗   ██╗██╗  ██╗ █████╗ ████████╗ ║");
        System.out.println("║  ██╔══██╗██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝██╔════╝████╗ ████║██╔════╝████╗  ██║    ██╔════╝██║   ██║██║  ██║██╔══██╗╚══██╔══╝ ║");
        System.out.println("║  ███████║██████╔╝███████║██████╔╝   ██║   █████╗  ██╔████╔██║█████╗  ██╔██╗ ██║    ███████╗██║   ██║███████║███████║   ██║    ║");
        System.out.println("║  ██╔══██║██╔═══╝ ██╔══██║██╔══██╗   ██║   ██╔══╝  ██║╚██╔╝██║██╔══╝  ██║╚██╗██║    ╚════██║██║   ██║██╔══██║██╔══██║   ██║    ║");
        System.out.println("║  ██║  ██║██║     ██║  ██║██║  ██║   ██║   ███████╗██║ ╚═╝ ██║███████╗██║ ╚████║    ███████║╚██████╔╝██║  ██║██║  ██║   ██║    ║");
        System.out.println("║  ╚═╝  ╚═╝╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝     ╚═╝╚══════╝╚═╝  ╚═══╝    ╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝    ║");
        System.out.println("╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝");

    while (isProgramRunning) {
        if (currentUser == null && !isAdminLoggedIn) {
            // Tampilkan menu utama
            System.out.println("╔═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗");
            System.out.println(  "║ "+ANSI_CYAN+"                                           ░█▀█░▀█▀░█░░░▀█▀░█░█░░░█▀█░█░█░█▀▀░▀█▀░░░░░░                                       "+ANSI_RESET+"║");
            System.out.println(  "║ "+ANSI_CYAN+"                                           ░█▀▀░░█░░█░░░░█░░█▀█░░░█▀█░█▀▄░▀▀█░░█░░░░░▀░                                       "+ANSI_RESET+"║");                                                
            System.out.println(  "║ "+ANSI_CYAN+"                                           ░▀░░░▀▀▀░▀▀▀░▀▀▀░▀░▀░░░▀░▀░▀░▀░▀▀▀░▀▀▀░░░░▀░                                       "+ANSI_RESET+"║");                                                
            System.out.println("║═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════║");
            System.out.println(  "║ "+ANSI_BOLD+"  1. LOGIN                                                                                                                    ║");
            System.out.println("║   2. DAFTAR                                                                                                                   ║");
            System.out.println(  "║   3. KELUAR                                                                                                             "+ANSI_RESET+"      ║");
            System.out.println("╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝");
            System.out.print("Pilih aksi (1/3) : ");

            int choice = input.nextInt();
            input.nextLine(); // Consume newline

            switch (choice) {
                case 1:

                System.out.print("Masukkan Nama Pengguna : ");
                String namaPenggunaInput = input.nextLine(); // Declare namaPenggunaInput here
                System.out.print("Masukkan Sandi         : ");
                String SandiInput = input.nextLine(); // Declare SandiInput here

                    // Login
                    if (namaPenggunaInput.equals(ADMIN_namaPengguna) && SandiInput.equals(ADMIN_Sandi)) {
                        // Admin login
                        isAdminLoggedIn = true;
                        System.out.println(ANSI_GREEN + "Admin login successful." + ANSI_RESET);
                    } else {
                        // User login
                        userIndex = authenticateUser(registerednamaPengguna, registeredSandis, namaPenggunaInput, SandiInput);
                        if (userIndex != -1) {
                            currentUser = users.get(userIndex); // Assign the logged-in user
                            System.out.println(ANSI_GREEN + "Login Sukses" + ANSI_RESET);
                        } else {
                            System.out.println(ANSI_RED + "Login Gagal. Nama Pengguna atau Kata Sandi Salah." + ANSI_RESET);
                        }
                    }
                    break;
                case 2:
                    // Daftar (Register)
                    registerUser(registerednamaPengguna, registeredSandis, users, input);
                    break;
                case 3:
                    isProgramRunning = false;
                    break;
                default:
                    System.out.println(ANSI_RED + "Pilihan tidak valid." + ANSI_RESET);
                    break;
            }
        } else if (currentUser != null) {
            // Tampilkan menu pengguna
            System.out.println("╔═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗");
            System.out.println(  "║ "+ANSI_CYAN +"                                          ░█▀█░▀█▀░█░░░▀█▀░█░█░░░█▄█░█▀▀░█▀█░█░█░░░░░░                                        "+ ANSI_RESET +"║");
            System.out.println(  "║ "+ANSI_CYAN +"                                          ░█▀▀░░█░░█░░░░█░░█▀█░░░█░█░█▀▀░█░█░█░█░░░░▀░                                        "+ ANSI_RESET +"║");        
            System.out.println(  "║ "+ANSI_CYAN +"                                          ░▀░░░▀▀▀░▀▀▀░▀▀▀░▀░▀░░░▀░▀░▀▀▀░▀░▀░▀▀▀░░░░▀░                                        "+ ANSI_RESET +"║");
            System.out.println("║═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════║");
            System.out.println(  "║   " + ANSI_BLUE +  "  1. PEMESANAN KAMAR                                                                                                        "+ ANSI_RESET +"║");
            System.out.println(  "║   " + ANSI_GREEN+  "  2. CHECK-IN                                                                                                               "+ ANSI_RESET +"║");
            System.out.println(  "║   " + ANSI_RED  +  "  3. CHECK-OUT                                                                                                              "+ ANSI_RESET +"║");
            System.out.println(  "║   " + ANSI_PURPLE + "  4. MEMBERSHIP                                                                                                             "+ ANSI_RESET +"║"); 
            System.out.println(  "║   " + ANSI_YELLOW+ "  5. LOG-OUT                                                                                                                "+ ANSI_RESET +"║"); 
            System.out.println("╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝");
            System.out.print  ("  Silakan pilih opsi (1-5) : ");
            int userChoice = input.nextInt();
            input.nextLine(); // Consume newline

            switch (userChoice) {
                case 1:
                    // Pemesanan Kamar
                    if (statusPemesanan.equals("Dipesan")) {
                        System.out.println(ANSI_RED + "Anda sudah memesan kamar. Silakan check-in atau check-out terlebih dahulu." + ANSI_RESET);
                    } else if (statusPemesanan.equals("Belum Dipesan")) {
                        makeBooking(users, stockRooms, bookings, userIndex, input);
                        String hasilReservasi = makeBooking(users, stockRooms, bookings, userIndex, input);
                        
                        if (hasilReservasi.equals("berhasil")) {
                            statusPemesanan = "Dipesan";
                            break;
                        } else {
                            break;
                        }
                    } 
                
                    break;
                case 2:
                // Check-in

                // Stylized banner for Check-in
                System.out.println("╔═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗");
                System.out.println(  "║ "+ANSI_CYAN +"                                   ░█▀▀░▀█▀░▀█▀░█░█░█▀▄░░░█▀▀░█░█░█▀▀░█▀▀░█░█░░░░░▀█▀░█▀█                                     "+ ANSI_RESET +"║");
                System.out.println(  "║ "+ANSI_CYAN +"                                   ░█▀▀░░█░░░█░░█░█░█▀▄░░░█░░░█▀█░█▀▀░█░░░█▀▄░▄▄▄░░█░░█░█                                     "+ ANSI_RESET +"║");
                System.out.println(  "║ "+ANSI_CYAN +"                                   ░▀░░░▀▀▀░░▀░░▀▀▀░▀░▀░░░▀▀▀░▀░▀░▀▀▀░▀▀▀░▀░▀░░░░░▀▀▀░▀░▀                                     "+ ANSI_RESET +"║");
                System.out.println("╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝");

                if (bookings[userIndex] != null && statusPemesanan.equals("Dipesan")) {
                if (statusCheckIn.equals("belum")) {
                    statusCheckIn = STATUS_PENDING_CHECKIN;
                    bookings[userIndex][8] = STATUS_PENDING_CHECKIN;
                    System.out.println("Permintaan Check-In Anda sedang menunggu persetujuan admin.");
                } else if (bookings[userIndex][8].equals(STATUS_APPROVED_CHECKIN)) {
                    statusCheckIn = STATUS_APPROVED_CHECKIN;
                    System.out.println(ANSI_GREEN + "Permintaan Check-In disetujui." + ANSI_RESET);
                    System.out.println( "Selamat Datang, Tamu yang Terhormat!");
                    System.out.println(  "Status Pemesanan Anda : " + ANSI_GREEN + "Sudah" + ANSI_RESET);
                    System.out.println(  "Status Check-in Anda  : " + ANSI_GREEN + "Sudah" + ANSI_RESET);
                    System.out.println(ANSI_PURPLE + "═══════════════════════════════════════════════" + ANSI_RESET);
                    System.out.println(ANSI_BOLD + ANSI_CYAN + "               Detail Pemesanan                " + ANSI_RESET);
                    System.out.println(ANSI_PURPLE + "═══════════════════════════════════════════════" + ANSI_RESET);
                    System.out.println(ANSI_CYAN + "Nama Pengguna           : " + ANSI_RESET + registerednamaPengguna.get(userIndex) + ANSI_RESET);
                    System.out.println(ANSI_CYAN + "Tipe Kamar              : " + ANSI_RESET + bookings[userIndex][0] );
                    System.out.println(ANSI_CYAN + "Jumlah Malam            : " + ANSI_RESET + bookings[userIndex][7] );
                    System.out.println(ANSI_CYAN + "Status Check-in Anda    : " + ANSI_YELLOW + statusCheckIn );
                    System.out.println(ANSI_CYAN + "Tanggal Reservasi       :" +ANSI_RESET+bookings[userIndex][1] );
                    System.out.println(ANSI_CYAN + "Fasilitas Tambahan      : " + ANSI_RESET + bookings[userIndex][2] + "," + bookings[userIndex][11]);
                    System.out.println(ANSI_CYAN + "Pembayaran              : " + ANSI_RESET + bookings[userIndex][5] );
                    System.out.println(ANSI_CYAN + "Total Biaya             : " + ANSI_RESET + "Rp. "  + bookings[userIndex][6] );
                    System.out.println(ANSI_PURPLE + "═══════════════════════════════════════════════" + ANSI_RESET);
                    // Additional information or actions for check-in can be added here
                } else {
                    //Pesan jika belum reservasi
                    System.out.println(ANSI_RED+" ANDA BELUM MELAKUKAN RESERVASI" +ANSI_RESET);
                }
            };
                break;

                case 3:
                // Check-out
            
                // Stylized banner for Check-out
                System.out.println("╔═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗");
                System.out.println(  "║ "+ANSI_CYAN +"                                  ░█▀▀░▀█▀░▀█▀░█░█░█▀▄░░░█▀▀░█░█░█▀▀░█▀▀░█░█░░░░░█▀█░█░█░▀█▀                                  "+ ANSI_RESET +"║");
                System.out.println(  "║ "+ANSI_CYAN +"                                  ░█▀▀░░█░░░█░░█░█░█▀▄░░░█░░░█▀█░█▀▀░█░░░█▀▄░▄▄▄░█░█░█░█░░█░                                  "+ ANSI_RESET +"║");
                System.out.println(  "║ "+ANSI_CYAN +"                                  ░▀░░░▀▀▀░░▀░░▀▀▀░▀░▀░░░▀▀▀░▀░▀░▀▀▀░▀▀▀░▀░▀░░░░░▀▀▀░▀▀▀░░▀░                                  "+ ANSI_RESET +"║");
                System.out.println("╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝");
            

            if (bookings[userIndex] != null && statusPemesanan.equals("Dipesan")) {
                if (statusCheckIn.equals(STATUS_APPROVED_CHECKIN)) {
                    statusCheckIn = STATUS_PENDING_CHECKOUT;
                    bookings[userIndex][8] = STATUS_PENDING_CHECKOUT;
                    System.out.println("Permintaan Check-Out Anda sedang menunggu persetujuan admin.");
                } else if (bookings[userIndex][8].equals(STATUS_APPROVED_CHECKOUT)) {
                    System.out.println(ANSI_YELLOW + "Permintaan Check-Out Anda sudah disetujui oleh admin." + ANSI_RESET);
                    System.out.println();
                    System.out.println("Selamat tinggal! Terima kasih telah memilih layanan kami.");
                    System.out.println("Bagaimana pengalaman Anda menggunakan aplikasi kami?");
                    System.out.print("Beri rating (1-5) : ");
                    int rating = input.nextInt();
                    // Membersihkan buffer input
            
                    if (rating >= 1 && rating <= 5) {
                        bookings[userIndex][3] = "" + rating;
                        input.nextLine(); // Clear the newline character from the previous input
                        System.out.print("Tulis ulasan      : ");
                        String ulasan = input.nextLine();
                        bookings[userIndex][4] = " " + ulasan;
            
                        if (rating < 3) {
                            System.out.println("Mohon maaf atas ketidaknyamanan Anda.");
                            System.out.println("Masukkan komplain atau saran Anda : ");
                            String komplain = input.nextLine();
                            bookings[userIndex][6] = "" + komplain;
                            System.out.println("Terimakasih atas masukan dan sarannya, Kami mohon maaf yang sebesar - besarnya");
                            }
                    
                    statusPemesanan = "Belum Dipesan";
                    
            
                        }
                } else {
                        //Pesan jika belum reservasi
                        System.out.println("╔═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗");
                        System.out.println(  "║ "+ANSI_CYAN +"   ░█▀█░█▀█░█▀▄░█▀█░░░█▀▄░█▀▀░█░░░█░█░█▄█░░░█▄█░█▀▀░█░░░█▀█░█░█░█░█░█░█░█▀█░█▀█░░░█▀▄░█▀▀░█▀▀░█▀▀░█▀▄░█░█░█▀█░█▀▀░▀█▀         "+ ANSI_RESET +"║");
                        System.out.println(  "║ "+ANSI_CYAN +"   ░█▀█░█░█░█░█░█▀█░░░█▀▄░█▀▀░█░░░█░█░█░█░░░█░█░█▀▀░█░░░█▀█░█▀▄░█░█░█▀▄░█▀█░█░█░░░█▀▄░█▀▀░▀▀█░█▀▀░█▀▄░▀▄▀░█▀█░▀▀█░░█░         "+ ANSI_RESET +"║");
                        System.out.println(  "║ "+ANSI_CYAN +"   ░▀░▀░▀░▀░▀▀░░▀░▀░░░▀▀░░▀▀▀░▀▀▀░▀▀▀░▀░▀░░░▀░▀░▀▀▀░▀▀▀░▀░▀░▀░▀░▀▀▀░▀░▀░▀░▀░▀░▀░░░▀░▀░▀▀▀░▀▀▀░▀▀▀░▀░▀░░▀░░▀░▀░▀▀▀░▀▀▀         "+ ANSI_RESET +"║");
                        System.out.println("╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝");
                    }
            }
                    break;
                
                case 4:
                    handleMembership(currentUser, input);
                break;    

                case 5:
                    currentUser = null;
                    break;
                default:
                    System.out.println("Pilihan tidak valid.");
                    break;
            }
        } else if (isAdminLoggedIn) {
            // Tampilkan menu admin
            System.out.println("╔═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗");
            System.out.println(  "║ "+ANSI_CYAN+"                                                          ░█▄█░█▀▀░█▀█░█░█                                                    "+ ANSI_RESET +"║");
            System.out.println(  "║ "+ANSI_CYAN+"                                                          ░█░█░█▀▀░█░█░█░█                                                    "+ ANSI_RESET +"║");
            System.out.println(  "║ "+ANSI_CYAN+"                                                          ░▀░▀░▀▀▀░▀░▀░▀▀▀                                                    "+ ANSI_RESET +"║");
            System.out.println("║═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════║");
            System.out.println(  "║  "+ANSI_BOLD+"   1. Lihat Pemesanan                                                                                                        ║");
            System.out.println("║     2. Menyetujui Check-in                                                                                                    ║");
            System.out.println("║     3. Menyetujui Check-Out                                                                                                   ║");
            System.out.println("║     4. Masukan Pelanggan                                                                                                      ║");
            System.out.println("║     5. Lihat Akun Pelanggan                                                                                                   ║");
            System.out.println("║     6. Lihat Data Diri Pelanggan                                                                                              ║");
            System.out.println("║     7. Hapus Akun Pelanggan                                                                                                   ║");
            System.out.println("║     8. Kelola Diskon                                                                                                          ║");
            System.out.println(  "║     9. Log-Out                                                                                                      "+ANSI_RESET+"          ║");            
            System.out.println(  "╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝" + ANSI_RESET);
            System.out.print("Pilih Menu : ");
            int adminChoice = input.nextInt();
            input.nextLine(); // Consume newline

            switch (adminChoice) {
                case 1:
                    userInformation(users, bookings, userIndex);
                    break;
                case 2:
                     approveCheckIn(users, bookings, registerednamaPengguna, input);
                    break;
                case 3:
        
                    approveCheckOut(users, bookings, registerednamaPengguna, input);
                
                break;

                case 4:
                    userFeedback(users, bookings, userIndex);
                break;

                case 5:
                    viewRegisteredUsers(users);
                break;

                case 6:
                    viewUserDetails(users, input);
                break;
                
                case 7:
                    deleteUser(users, registerednamaPengguna, input);
                break;

                case 8:
                    manageDiscounts(input);
                break;
                
                case 9:
                    isAdminLoggedIn = false;
                    break;
                default:
                    System.out.println("Pilihan tidak valid.");
                    break;
            }
        }
    }

    input.close();
    System.out.println("Program selesai. Terima kasih telah menggunakan aplikasi kami.");
    }
}