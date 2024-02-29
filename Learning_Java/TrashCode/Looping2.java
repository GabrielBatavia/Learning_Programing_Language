import java.util.Scanner;
/**
 * Looping2
 */
 public class Looping2 {

    public static void main(String[] args) {
        
        Scanner sc = new Scanner(System.in);

        //Experiment 1 Start
        System.out.println("Enter the value or N: ");
        int N = sc.nextInt();

        for (int i = 0; i <= N; i++) {
            System.out.print("*");
        }
        //End Experiment 1

        System.out.println(); //kosongan

        //Experiment 2 start
        System.out.println("Enter the value or M: ");
        int M = sc.nextInt();

        for (int i = 1; i <= M; i++) {
            System.out.print("*");
        }

    }
}