import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Scanner;
import java.util.Calendar;
import java.util.Random;

class User {
    String username;
    String password;
    Booking booking;

    User(String username, String password) {
        this.username = username;
        this.password = password;
    }
}

class Booking {
    String roomType;
    int numberOfNights;
    String reservationDate;
    String additionalFacilities;
    String paymentMethod;
    String promoApplied;
    int totalCost;

    Booking(String roomType, int numberOfNights, String reservationDate, String additionalFacilities, String paymentMethod, int totalCost) {
        this.roomType = roomType;
        this.numberOfNights = numberOfNights;
        this.reservationDate = reservationDate;
        this.additionalFacilities = additionalFacilities;
        this.paymentMethod = paymentMethod;
        this.totalCost = totalCost;
    }
}

public class javaproject_1 {
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
    private static final String ADMIN_USERNAME = "admin";
    private static final String ADMIN_PASSWORD = "admin123";
    

    private static ArrayList<String> registeredUsernames = new ArrayList<>();
    private static String[][] bookings = new String[10][5]; // Contoh: 10 pemesanan, dengan 5 informasi per pemesanan
  

    private static int authenticateUser(ArrayList<String> usernames, ArrayList<String> passwords, String usernameInput, String passwordInput) {
        if (usernames.contains(usernameInput)) {
            int userIndex = usernames.indexOf(usernameInput);
            if (passwords.get(userIndex).equals(passwordInput)) {
                System.out.println("Selamat datang, " + usernameInput + "!");
                return userIndex;
            }
        }
        System.out.println(ANSI_RED + "Username atau password salah. Silakan coba lagi." + ANSI_RESET);
        return -1;
    }

    private static boolean isValidDate(String date) {
    SimpleDateFormat sdf = new SimpleDateFormat("dd/MM/yyyy");
    sdf.setLenient(false); // Set lenient to false to strictly parse the date
    try {
        sdf.parse(date); // Parse the date. If invalid, it will throw ParseException
        return true; // Date is valid
    } catch (ParseException e) {
        return false; // Date is invalid
    }
}

    private static void registerUser(ArrayList<String> usernames, ArrayList<String> passwords, ArrayList<User> users, Scanner input) {
        System.out.print("Masukkan Username baru: ");
        String newUsername = input.nextLine();
    
        if (!usernames.contains(newUsername)) {
            System.out.print("Masukkan Password baru: ");
            String newPassword = input.nextLine();
    
            usernames.add(newUsername);
            passwords.add(newPassword);
            users.add(new User(newUsername, newPassword)); // Add new user to the users list
    
            System.out.println(ANSI_GREEN + "Akun berhasil dibuat! Silakan login." + ANSI_RESET);
        } else {
            System.out.println(ANSI_RED + "Username sudah digunakan. Silakan pilih username lain." + ANSI_RESET);
        }
    }

    public static void approveCheckIn(String username) {
        // Mencari pengguna dengan username
        for (String[] booking : bookings) {
            if (booking[0].equals(username) && booking[9].equals("pending")) {
                booking[9] = "sudah"; // Menyetujui check-in
                System.out.println("Check-In untuk " + username + " telah disetujui.");
            }
        }
    }

    public static void approveCheckOut(String username) {
        // Mencari pengguna dengan username
        for (String[] booking : bookings) {
            if (booking != null && booking[0] != null && booking[0].equals(username) && booking[9].equals("pending checkout")) {
                booking[9] = "telah check-out"; // Menyetujui check-out
                System.out.println("Check-Out untuk " + username + " telah disetujui.");
            }
        }
    }


    private static void makeBooking(int[] stockRooms, String[][] bookings, int userIndex, Scanner input) {
        int hargapermalam = 0, jmlmalam, biayatambahan, totalbiaya;

        // Stylized banner for selecting room type
        System.out.println(ANSI_CYAN + "  ╔══════════════════════════════════════════════════════════════════════╗");
        System.out.println(          "  ║                            Pilihan Tipe Kamar                        ║");
        System.out.println(          "  ║══════════════════════════════════════════════════════════════════════║");
        System.out.println(          "  ║   1 : Studio (Rp.100000)                                             ║");                                         
        System.out.println(          "  ║    -------------------------------                                   ║");
        System.out.println(          "  ║       Spesifikasi: Single bed, TV, AC                                ║");
        System.out.println(          "  ║       Fasilitas   : Free Wi-Fi, Toiletries                           ║");
        System.out.println(          "  ║   2 : Duplex (Rp.150000)                                             ║");
        System.out.println(          "  ║    -------------------------------                                   ║" );
        System.out.println(          "  ║       Spesifikasi: Double bed, TV, AC, Mini Kitchen                  ║");
        System.out.println(          "  ║       Fasilitas   : Free Wi-Fi, Toiletries, Room Service             ║");
        System.out.println(          "  ║   3 : Triplex (Rp.200000)                                            ║");
        System.out.println(          "  ║    -------------------------------                                   ║");
        System.out.println(          "  ║       Spesifikasi: Queen bed, TV, AC, Kitchen, Jacuzzi               ║");
        System.out.println(          "  ║       Fasilitas   : Free Wi-Fi, Toiletries, Room Service, Spa Access ║");
        System.out.println(            "  ╚══════════════════════════════════════════════════════════════════════╝" + ANSI_RESET);
        System.out.print("Masukkan tipe kamar yang diinginkan: ");
        int tipekamar = input.nextInt();

        if (tipekamar >= 1 && tipekamar <= stockRooms.length && stockRooms[tipekamar - 1] > 0) {
            // There is available stock, proceed with booking
            stockRooms[tipekamar - 1]--; // Decrease the available room count
        } else {
            System.out.println(ANSI_RED + "Maaf, kamar tipe ini sudah habis atau tipe kamar tidak valid." + ANSI_RESET);
            return;
        }

        // Stylized banner for entering the number of nights
        System.out.println(ANSI_CYAN + "  ╔════════════════════════════════════════════╗");
        System.out.println(          "  ║           Masukkan Jumlah Malam            ║");
        System.out.println(            "  ╚════════════════════════════════════════════╝" + ANSI_RESET);
        System.out.print("Masukkan jumlah malam yang diinginkan: ");
        while (true) {
            if (input.hasNextInt()) {
                jmlmalam = input.nextInt();
                if (jmlmalam > 0) {
                    break; // Exit the loop if the input is valid
                } else {
                    System.out.println(ANSI_RED + "Jumlah malam harus lebih dari 0. Silakan coba lagi." + ANSI_RESET);
                }
            } else {
                System.out.print(ANSI_RED + "Masukkan angka yang valid: " + ANSI_RESET);
                input.next(); // Discard the invalid token from the input
            }
        }
        bookings[userIndex][7] = "Jumlah Malam: " + jmlmalam;

        // Calculate total cost based on room type
        switch (tipekamar) {
            case 1:
                bookings[userIndex][0] = "Kamar Tipe Studio";
                hargapermalam = 100000;
                break;
            case 2:
                bookings[userIndex][0] = "Kamar Tipe Duplex";
                hargapermalam = 150000;
                break;
            case 3:
                bookings[userIndex][0] = "Kamar Tipe Triplex";
                hargapermalam = 200000;
                break;
            default:
                System.out.println(ANSI_RED + "Tipe kamar tidak valid." + ANSI_RESET);
                return;
        }

        bookings[userIndex][1] = "Jumlah Malam      : " + jmlmalam;

        totalbiaya = jmlmalam * hargapermalam;
        boolean tambahanLain = true;

        //displayCalendar();
        displayCalendar(input); // Pass 'input' to 'displayCalendar' method

         // Stylized banner for entering the reservation date
         System.out.println(ANSI_CYAN +  " ╔════════════════════════════════════════════╗");
         System.out.println(           " ║        Pilih Tanggal Reservasi             ║");
         System.out.println(           " ╚════════════════════════════════════════════╝" + ANSI_RESET);
        String reservationDate;
        while (true) {
        System.out.print("Masukkan tanggal reservasi (dd/mm/yyyy): ");
        reservationDate = input.next();
            if (isValidDate(reservationDate)) {
                break; // Keluar dari loop jika tanggal valid
            } else {
                System.out.println(ANSI_RED + "Format tanggal salah atau tanggal tidak valid. Silakan coba lagi." + ANSI_RESET);
            }
        }
    
         bookings[userIndex][1] = "Tanggal Reservasi: " + reservationDate;

        // Stylized banner for additional facilities
        while (tambahanLain) {
            System.out.println("╔════════════════════════════════════════════╗");
            System.out.println("║          Pilihan Tambahan Fasilitas        ║ ");
            System.out.println("╚════════════════════════════════════════════╝");
            System.out.println("1 : Laundry (Rp.20,000 per malam)");
            System.out.println("2 : Sarapan (Rp.25,000 per malam)");
            System.out.println("3 : Selesai");

            System.out.print("Pilih tambahan fasilitas (1/2/3): ");
            int tambahan = input.nextInt();

            if (tambahan == 1) {
                biayatambahan = 20000 * jmlmalam; // Laundry cost
                totalbiaya += biayatambahan;
                bookings[userIndex][2] = "Biaya laundry: Rp." + biayatambahan;
            } else if (tambahan == 2) {
                biayatambahan = 25000 * jmlmalam; // Breakfast cost
                totalbiaya += biayatambahan;
                bookings[userIndex][2] = "Biaya sarapan: Rp." + biayatambahan;
            } else if (tambahan == 3) {
                tambahanLain = false; // Exit the loop if the user chooses to finish
            } else {
                System.out.println(ANSI_RED + "Tambahan fasilitas tidak valid." + ANSI_RESET);
                return;
            }
        }

        // Stylized banner for displaying the total price
        System.out.println("\n===============================================");
        System.out.println("Tagihan = " + ANSI_YELLOW + "Rp."+ totalbiaya + ANSI_RESET);
        System.out.println("===============================================");

        // Stylized banner for payment options
        System.out.println("╔════════════════════════════════════════════╗");
        System.out.println("║             Pilih Opsi Pembayaran          ║ ");
        System.out.println("╚════════════════════════════════════════════╝");
        System.out.println("1. Cash");
        System.out.println("2. Transfer Bank");
        System.out.print("Masukkan Pilihan Pembayaran: ");
        int paymentChoice = input.nextInt();
        input.nextLine(); // Consume the newline character

        switch (paymentChoice) {
            case 1:
                bookings[userIndex][5] = "Pembayaran: Cash";
                break;
            case 2:
                bookings[userIndex][5] = "Pembayaran: Transfer Bank";

                System.out.println("\n NO VA : 23457654345678");
                break;
            default:
                System.out.println(ANSI_RED + "Pilihan Pembayaran tidak valid."+ ANSI_RESET);
                return;
        }

        // Continue with promo code logic
        boolean promoAktif = false;
        while (true) {
            // Stylized banner for promo code activation
            System.out.println("╔════════════════════════════════════════════╗");
            System.out.println("║        Aktivasi Promo Pemesanan Kamar      ║ ");
            System.out.println("╚════════════════════════════════════════════╝");
            System.out.print("Apakah Anda ingin mengaktifkan promo? (Ya/Tidak): ");

            String promoChoice = input.next();
            if (promoChoice.equalsIgnoreCase("Ya") || promoChoice.equalsIgnoreCase("Tidak")) {
                if (promoChoice.equalsIgnoreCase("Ya")) {
                    System.out.print("Berapa jumlah malam yang Anda pesan? ");
                    int jmlMalam = input.nextInt();
                    if (jmlMalam >= 3) {
                        double diskon = 0.1; // 10% discount
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
            bookings[userIndex][6] = "Total biaya setelah promo: Rp." + totalbiaya;
        }

        // Stylized banner for displaying the total price
        System.out.println("  ╔════════════════════════════════════════════╗");
        System.out.println("  ║     Harga yang harus dibayarkan adalah     ║");
        System.out.println("  ╚════════════════════════════════════════════╝");
        System.out.println(ANSI_YELLOW + "Rp." + totalbiaya +ANSI_RESET);

        Random random = new Random();
        int uniqueCode = random.nextInt(900) + 100; // Menghasilkan angka acak antara 100 dan 999
    
        int totalCostWithUniqueCode = totalbiaya + uniqueCode;
        bookings[userIndex][6] = String.valueOf(totalCostWithUniqueCode);

        printPaymentReceipt(bookings, userIndex, uniqueCode);
    

    }

    private static void printPaymentReceipt(String[][] bookings, int userIndex, int uniqueCode) {
        System.out.println("\n====================== STRUK PEMBAYARAN ======================");
        System.out.println("Metode Pembayaran: " + bookings[userIndex][5]);
        System.out.println("Kode Unik Pembayaran: " + uniqueCode);
        System.out.println("Total Biaya (termasuk kode unik): Rp" + bookings[userIndex][6]);
        System.out.println("=============================================================");
    }
    
    private static void displayCalendar(Scanner input) {
        System.out.println(ANSI_CYAN + "  ╔════════════════════════════════════════════╗ ");
        System.out.println(          "  ║               Available Dates              ║ ");
        System.out.println(          "  ╚════════════════════════════════════════════╝ ");
    
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
        while (calendar.get(Calendar.MONTH) == currentMonth) {
            int dayOfMonth = calendar.get(Calendar.DAY_OF_MONTH);
            System.out.printf("%3d", dayOfMonth);
    
            // Check if the day is available (for demonstration, assume all days are available)
            boolean isAvailable = true;
            System.out.print(isAvailable ? " " : "X");
    
            // Move to the next day
            calendar.add(Calendar.DAY_OF_MONTH, 1);
    
            // Start a new line for the next week
            if (calendar.get(Calendar.DAY_OF_WEEK) == Calendar.SUNDAY) {
                System.out.println();
            }
        }

        System.out.println("\n===============================================" + ANSI_RESET);
    }


    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        ArrayList<User> users = new ArrayList<>();
        int[] stockRooms = {1, 5, 3}; // Misalnya: 1 Studio, 5 Duplex, 3 Triplex
        String[][] bookings = new String[4][10]; // Maksimal 4 pengguna, dan 7 informasi pemesanan per pengguna
        boolean[] pesananDiterima = new boolean[4]; // Sesuaikan dengan jumlah pengguna maksimal
        ArrayList<String> registeredPasswords = new ArrayList<>();

        boolean isProgramRunning = true;
        User currentUser = null;
        boolean isAdminLoggedIn = false;

        boolean loggedIn = false;
        String statusPemesanan = "BelumDipesan";
        String statusCheckIn = "belum";

        int userIndex = -1; // Declare userIndex here

        System.out.println("╔═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗");
        System.out.println("║   █████╗ ██████╗ ██████╗  █████╗ ██████╗ ████████╗███████╗███╗   ███╗███████╗███╗   ██╗    ███████╗██╗   ██╗██╗  ██╗ █████╗ ████████╗ ║");
        System.out.println("║  ██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝██╔════╝████╗ ████║██╔════╝████╗  ██║    ██╔════╝██║   ██║██║  ██║██╔══██╗╚══██╔══╝ ║");
        System.out.println("║  ███████║██████╔╝██████╔╝███████║██████╔╝   ██║   █████╗  ██╔████╔██║█████╗  ██╔██╗ ██║    ███████╗██║   ██║███████║███████║   ██║    ║");
        System.out.println("║  ██╔══██║██╔═══╝ ██╔═══╝ ██╔══██║██╔══██╗   ██║   ██╔══╝  ██║╚██╔╝██║██╔══╝  ██║╚██╗██║    ╚════██║██║   ██║██╔══██║██╔══██║   ██║    ║");
        System.out.println("║  ██║  ██║██║     ██║     ██║  ██║██║  ██║   ██║   ███████╗██║ ╚═╝ ██║███████╗██║ ╚████║    ███████║╚██████╔╝██║  ██║██║  ██║   ██║    ║");
        System.out.println("║  ╚═╝  ╚═╝╚═╝     ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝     ╚═╝╚══════╝╚═╝  ╚═══╝    ╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝    ║");
        System.out.println("╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝");

    while (isProgramRunning) {
        if (currentUser == null && !isAdminLoggedIn) {
            // Tampilkan menu utama
            System.out.println(ANSI_CYAN + "  ╔════════════════════════════════════════════╗");
            System.out.println(          "  ║               Pilih Aksi:                  ║");
            System.out.println(          "  ║════════════════════════════════════════════║");
            System.out.println(          "  ║   1. Login                                 ║");
            System.out.println(          "  ║   2. Daftar                                ║");
            System.out.println(          "  ║   3. Keluar                                ║");
            System.out.println(            "  ╚════════════════════════════════════════════╝" + ANSI_RESET);
            System.out.print("Pilih aksi (1/2): ");

            int choice = input.nextInt();
            input.nextLine(); // Consume newline

            switch (choice) {
                case 1:

                System.out.print("Masukkan Username: ");
                String usernameInput = input.nextLine(); // Declare usernameInput here
                System.out.print("Masukkan Password: ");
                String passwordInput = input.nextLine(); // Declare passwordInput here

                    // Login
                    if (usernameInput.equals(ADMIN_USERNAME) && passwordInput.equals(ADMIN_PASSWORD)) {
                        // Admin login
                        isAdminLoggedIn = true;
                        System.out.println("Admin login successful.");
                    } else {
                        // User login
                        userIndex = authenticateUser(registeredUsernames, registeredPasswords, usernameInput, passwordInput);
                        if (userIndex != -1) {
                            currentUser = users.get(userIndex); // Assign the logged-in user
                            System.out.println("User login successful.");
                        } else {
                            System.out.println("Login failed. Incorrect username or password.");
                        }
                    }
                    break;
                case 2:
                    // Daftar (Register)
                    registerUser(registeredUsernames, registeredPasswords, users, input);
                    break;
                case 3:
                    isProgramRunning = false;
                    break;
                default:
                    System.out.println("Pilihan tidak valid.");
                    break;
            }
        } else if (currentUser != null) {
            // Tampilkan menu pengguna
            System.out.println("  ╔════════════════════════════════════════════╗");
            System.out.println("  ║          \u001B[1mHotel Management System\u001B[0m           ║"); // Bold judul
            System.out.println("  ║════════════════════════════════════════════║");
            System.out.println("  ║  \u001B[34m1. \u001B[0mPemesanan Kamar                        ║"); // Biru untuk pilihan 1
            System.out.println("  ║  \u001B[32m2. \u001B[0mCheck-in                               ║"); // Hijau untuk pilihan 2
            System.out.println("  ║  \u001B[31m3. \u001B[0mCheck-out                              ║"); // Merah untuk pilihan 3
            System.out.println("  ║  \u001B[33m4. \u001B[0mLog-Out                                ║"); // Kuning untuk pilihan 4
            System.out.println("  ╚════════════════════════════════════════════╝");
            System.out.println("\u001B[0m"); // Reset warna teks
            System.out.println("  Silakan pilih opsi (1-4): ");
            int userChoice = input.nextInt();
            input.nextLine(); // Consume newline

            switch (userChoice) {
                case 1:
                    // Pemesanan Kamar
                    if (statusPemesanan.equals("Dipesan")) {
                        System.out.println("Anda sudah memesan kamar. Silakan check-in atau check-out terlebih dahulu.");
                        break;
                    }

                    makeBooking(stockRooms, bookings, userIndex, input);
                    statusPemesanan = "Dipesan";
                    break;
                case 2:
                // Check-in

                // Stylized banner for Check-in
                System.out.println("  ╔════════════════════════════════════════════╗");
                System.out.println("  ║               Fitur Check-in               ║");
                System.out.println("  ╚════════════════════════════════════════════╝");

                if (statusPemesanan.equalsIgnoreCase("Dipesan") && statusCheckIn.equalsIgnoreCase("belum")) {
                    statusCheckIn = "pending";
                    System.out.println(ANSI_YELLOW + "Permintaan Check-In Anda sedang menunggu persetujuan admin." + ANSI_RESET);
                    System.out.println(ANSI_GREEN + "Selamat Datang, Tamu yang Terhormat!" + ANSI_RESET);
                    System.out.println(ANSI_CYAN + "Status Pemesanan Anda: " + ANSI_YELLOW + statusPemesanan + ANSI_RESET);
                    System.out.println(ANSI_CYAN + "Status Check-in Anda : " + ANSI_YELLOW + statusCheckIn + ANSI_RESET);
                    System.out.println(ANSI_PURPLE + "-----------------------------------------------" + ANSI_RESET);
                    System.out.println(ANSI_BOLD + ANSI_CYAN + "               Detail Pemesanan                " + ANSI_RESET);
                    System.out.println(ANSI_PURPLE + "-----------------------------------------------" + ANSI_RESET);
                    System.out.println(ANSI_CYAN + "Username             : " + ANSI_WHITE + registeredUsernames.get(userIndex) + ANSI_RESET);
                    System.out.println(ANSI_CYAN + "Tipe Kamar           : " + ANSI_WHITE + bookings[userIndex][0] + ANSI_RESET);
                    System.out.println(ANSI_WHITE + bookings[userIndex][7] + ANSI_RESET);
                    System.out.println(ANSI_CYAN + "Status Check-in Anda : " + ANSI_YELLOW + statusCheckIn + ANSI_RESET);
                    System.out.println(ANSI_WHITE + bookings[userIndex][1] + ANSI_RESET);
                    System.out.println(ANSI_CYAN + "Fasilitas            : " + ANSI_WHITE + bookings[userIndex][2] + ANSI_RESET);
                    System.out.println(ANSI_CYAN + "Pembayaran           : " + ANSI_WHITE + bookings[userIndex][5] + ANSI_RESET);
                    System.out.println(ANSI_PURPLE + "-----------------------------------------------" + ANSI_RESET);

                    // Additional information or actions for check-in can be added here

                    statusCheckIn = "sudah";
                } else if (statusPemesanan.equals("BelumDipesan")) {
                    System.out.println("  ╔══════════════════════════════════╗");
                    System.out.println("  ║            Mohon Maaf            ║");
                    System.out.println("  ║     Anda belum memesan Kamar     ║");
                    System.out.println("  ║        Silakan pesan kamar       ║");
                    System.out.println("  ║         terlebih dahulu.         ║");
                    System.out.println("  ╚══════════════════════════════════╝");
                } else {
                    System.out.println(ANSI_RED + "Maaf, Anda sudah check-in atau status pemesanan belum tersedia." + ANSI_RED);
                }
                    break;
                case 3:
                // Check-out
            
                // Stylized banner for Check-out
                System.out.println("  ╔════════════════════════════════════════════╗");
                System.out.println("  ║               Fitur Check-out              ║");
                System.out.println("  ╚════════════════════════════════════════════╝");
            
                if (statusPemesanan.equals("Dipesan") && statusCheckIn.equals("belum")) {
                    System.out.println(" Anda belum check-in. Silakan check-in terlebih dahulu.");
                }if (statusPemesanan.equals("Dipesan") && statusCheckIn.equals("sudah")) {
                    statusCheckIn = "pending checkout";
                    System.out.println(ANSI_YELLOW + "Permintaan Check-Out Anda sedang menunggu persetujuan admin." + ANSI_RESET);
                    System.out.println();
                    System.out.println(bookings[userIndex][1]);
                    System.out.println("Selamat tinggal! Terima kasih telah memilih layanan kami.");
                    System.out.println("Bagaimana pengalaman Anda menggunakan aplikasi kami?");
                    System.out.print("Beri rating (1-5): ");
                    int rating = input.nextInt();
            
                    if (rating >= 1 && rating <= 5) {
                        bookings[userIndex][3] = "Rating: " + rating;
                        input.nextLine(); // Clear the newline character from the previous input
                        System.out.print(" Tulis ulasan: ");
                        String ulasan = input.nextLine();
                        bookings[userIndex][4] = "Ulasan: " + ulasan;
            
                        if (rating < 3) {
                            System.out.println(" Mohon maaf atas ketidaknyamanan Anda.");
                            System.out.print("Masukkan komplain atau saran Anda: ");
                            String komplain = input.nextLine();
                            bookings[userIndex][6] = "Komplain: " + komplain;
                            System.out.println();
                            System.out.println("Terimakasih atas masukan dan sarannya, Kami mohon maaf yang sebesar-besarnya");
                        }
            
                        statusPemesanan = "BelumDipesan";
                        statusCheckIn = "belum";
                    } else {
                        System.out.println(ANSI_RED + " Rating tidak valid." + ANSI_RESET);
                        return;
                    }
                } else if (statusPemesanan.equals("BelumDipesan")) {
                    System.out.println(ANSI_RED + " Anda belum memesan kamar. Silakan pesan terlebih dahulu." + ANSI_RESET);
                } else {
                    System.out.println(ANSI_RED + " Anda belum check-in atau status pemesanan belum tersedia." + ANSI_RESET);
                }
                    break;
                case 4:
                    currentUser = null;
                    break;
                default:
                    System.out.println("Pilihan tidak valid.");
                    break;
            }
        } else if (isAdminLoggedIn) {
            // Tampilkan menu admin
            System.out.println("  ╔════════════════════════════════════════════╗");
            System.out.println("  ║                    Menu                    ║");
            System.out.println("  ║════════════════════════════════════════════║");
            System.out.println("  ║  1. View Booking                           ║");
            System.out.println("  ║  2. Approve Check-in                       ║");
            System.out.println("  ║  3. Approve Check-Out                       ║");
            System.out.println("  ║  4. Log-Out                                ║");
            System.out.println("  ╚════════════════════════════════════════════╝");
            int adminChoice = input.nextInt();
            input.nextLine(); // Consume newline

            switch (adminChoice) {
                case 1:
                    // Lihat informasi pemesanan pengguna
                    System.out.println("  ===============================================");
                    System.out.println("           Informasi Pemesanan Pengguna         ");
                    System.out.println("  ===============================================");
                    
                    for (int i = 0; i < bookings.length; i++) {
                        if (bookings[i][0] != null) {
                            System.out.println("Username: " + registeredUsernames.get(i));
                            System.out.println("Tipe Kamar: " + bookings[i][0]);
                            System.out.println(bookings[i][1]);
                            System.out.println("Fasilitas: " + bookings[i][2]);
                            System.out.println("Pembayaran: " + bookings[i][5]);
                            System.out.println("Status Check-in: " + (bookings[i][8] != null ? bookings[i][8] : "Belum Check-in"));
                            System.out.println("-----------------------------------------------");
                        }
                    }
                    break;
                case 2:
                    // Setujui check-in pengguna
                    System.out.println("  ===============================================");
                    System.out.println("            Setujui Check-in Pengguna           ");
                    System.out.println("  ===============================================");
                
                    // Menampilkan informasi pemesanan yang belum disetujui check-in
                    for (int i = 0; i < bookings.length; i++) {
                        if (bookings[i][0] != null && "Dipesan".equals(bookings[i][7]) && "belum".equals(bookings[i][8])) {
                            System.out.println("Username: " + registeredUsernames.get(i));
                            System.out.println("Tipe Kamar: " + bookings[i][0]);
                            System.out.println(bookings[i][1]);
                            System.out.println("Fasilitas: " + bookings[i][2]);
                            System.out.println("Pembayaran: " + bookings[i][5]);
                            System.out.println("-----------------------------------------------");
                
                            System.out.println("Masukkan Username untuk Menyetujui Check-In:");
                            String usernameCheckIn = input.nextLine();
                            javaproject_1.approveCheckIn(usernameCheckIn);
                            break;
                        }
                    }
                    break;

                case 3:
                System.out.println("Masukkan Username untuk Menyetujui Check-Out:");
                String usernameCheckOut = input.nextLine();
                javaproject_1.approveCheckOut(usernameCheckOut);
                    break;

                case 4:
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