import java.util.Scanner;
/**
 * factorialFor
 */
public class factorialFor {

    public static void main(String[] args) {
        
        Scanner input = new Scanner(System.in);

        int number, factorial, i; //int experiment 1
        int b; //int experiment 2
        int l, count; // int experiment 3
        double avg, total; //double experiment 3

        System.out.println("Enter a number: ");
        number = input.nextInt();

        //experiment 1 loop using for
        factorial = 1;
        for (i = 1; i <= number; i++) {
            factorial = factorial * i;
        }

        System.out.printf("The factorial of %d is %d\n", number, factorial);
        // experiment 1 loop using for

        // experiment 1 loop using while
        System.out.println("Enter a number: ");
        number = input.nextInt();

        factorial = 1;
        i = 1;
        while (i <= number) {
            factorial = factorial * i;
            i++;
        }

        System.out.printf("The factorial od %d is %d\n", number, factorial);
        //experiment 1 loop using while

        //experiment 1 loop using do-while
        System.out.println("Enter a number : ");
        number = input.nextInt();

        factorial = 1;
        i = 1;
        do {
            factorial = factorial * i;
            i++;
        } while (i <= number);

        System.out.printf("The factorial of %d is %d\n", number, factorial);
        //experiment 1 loop suing do-while

        System.out.println();//sout kosong untuk pembeda exp 1 dan exp2
        System.out.println();// sout kosong jarak

        //experiment 2 exit loop using break
        for (b = 0; true;){
            System.out.println("Enter a number: ");
            number = input.nextInt();;
            b += number;
            if (b > 50) {
                break;
            }
        }
        System.out.printf("The numbers stop at the sum of the numbers %d\n", b);
        //experiment 2 exit loop using break

        System.out.println();//sout kosong jarak
        System.out.println();//sout kosong jarak

        //experiment 3 exit loop using continue
        b = 0;
        count = 0;
        for (i = 0; i < 5; i++){
            System.out.println("Enter a number : ");
            number = input.nextInt();
            if (number >= 50) {
                continue;
            }
            b += number;
            count++;
        }
        total = (double) b;
        System.out.printf("The total number is less than 50: %.2f\n", total);
        avg = (double) b / count;
        System.out.printf("Avarage number less than 50: %.2f\n", avg);

        int a = 10;
        a%=5;
        System.out.println(a!=6);
    }
}