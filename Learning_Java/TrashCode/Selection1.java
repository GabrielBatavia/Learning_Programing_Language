import java.util.Scanner;
/**
 * Selection1
 */
public class Selection1 {

    public static void main(String[] args) {
        
        Scanner input = new Scanner(System.in);

        int number, score, age, score1, score2, nilai1, nilai2;
        double number1, number2, result;
        char operator;
    
        System.out.println("Enter a number: ");
        number = input.nextInt();

        String output = (number % 2 == 0) ? "Even number" : "Odd number";
        System.out.println(output);

        System.out.println("Enter a score1: ");
        score1 = input.nextInt();

        System.out.println("Enter the score2: ");
        score2 = input.nextInt();

        int total = score1 + score2;
        double average = total / 2;

        if (average >= 100) {
            average -= 5;
        } else {
            System.out.println(average);
        }

        System.out.println("The final score is " + average);

        System.out.println("Enter your age: ");
        age = input.nextInt();
        
        if (age > 65) {
            System.out.println("Elderly");
        } else if (age > 18){
            System.out.println("Adults");
        } else if (age > 12) {
            System.out.println("Teens");
        } else if (age > 5) {
            System.out.println("Children");
        } else if (age >= 1) {
            System.out.println("Toddler");
        } else {
            System.out.println("Sorry, that your age is wrong");
        }

        System.out.println("Enter the first number: ");
        number1 = input.nextDouble();
        System.out.println("Enter the second number: ");
        number2 = input.nextDouble();
        System.out.println("Enter an operator (+-^/): ");
        operator = input.next().charAt(0);

        switch (operator) {
            case '+':
                result = number1 + number2;
                System.out.println(number1 + " + " + number2 + " = " + result);
                break;
            case '-':
                result = number1 - number2;
                System.out.println(number1 + " - " + number2 + " = " + result);
                break;
            case '*':
                result = number1 * number2;
                System.out.println(number1 + " * " + number2 + " = " + result);
                break;
            case '/':
                result = number1 / number2;
                System.out.println(number1 + " / " + number2 + " = " + result);
                break;
            default:
            System.out.println("The operator you entered is wrong");
                break;
            }
        
            System.out.println("Enter nilai1 : ");
            nilai1 = input.nextInt();

            System.out.println("Enter nilai2: ");
            nilai2 = input.nextInt();

            if (nilai1 > nilai2) {
                System.out.println("Inilah nilai1 : " + nilai1);
            } else {
                System.out.println("Inilah nilai yang paling besar : " + nilai2);
            }
        
    }
}