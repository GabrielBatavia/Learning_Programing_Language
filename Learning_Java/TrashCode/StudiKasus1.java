import java.util.Scanner;

public class StudiKasus1 {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in); 

        int panjang, lebar, keliling;

        System.out.println("Masukkan panjang: ");
        panjang = sc.nextInt();
        System.out.println("Masukkan lebar: ");
        lebar = sc.nextInt();
        keliling = 2 * (panjang + lebar);

        System.out.println("Keliling Persegi panjang: " + keliling); 

        sc.close(); 
    }
}
