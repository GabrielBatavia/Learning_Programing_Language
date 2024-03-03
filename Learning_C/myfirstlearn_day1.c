#include <stdio.h>
#include <stdbool.h>

int main() {
  printf("Hello Sekai!\n\tI am learning \"C.\nAnd it is awesome!\n"); //aku komen

  //Learn variable

  int myNum = 15;
  printf("%d\n", myNum);

  float myFloat = 2.0f;
  printf("%f\n", myFloat);

  char myLetter = 'D';
  printf("My number is %d and my letter is %c\n", myNum, myLetter);

  printf("%c\n", myLetter);

  myNum = 10;  // Now myNum is 10

  printf("%d\n", myNum);

  int myOtherNum = 23;

  myNum = myOtherNum; // Assign the value of myOtherNum (23) to myNum

  printf("%d\n", myOtherNum);

  printf("%d\n", myNum);

  myNum = 100; // Assign the value of myNum

  myOtherNum = myNum;

  printf("%d\n", myOtherNum);

  //add variable

  int x = 5;
  int y = 6;
  int sum = x + y;
  printf("%d\n", sum);

  //declare multi variable

  int a = 5, b = 6, c = 50;
  printf("%d\n", a + b + c);

  int d, f, g;
  d = f = g = 50;
  printf("%d\n", d + f + g);

  char myText[] = "Hello";
  printf("%s\n", myText);

  double mydob = 19.99;
  printf("%lf\n", mydob);

  float f1a = 35e3; //Scientific Numbers
  double d1b = 12E4;

  printf("%f\n", f1a);
  printf("%lf\n", d1b);

  int myIntcek;
  float myFloatcek;
  double myDoublecek;
  char myCharcek;

  printf("%lu\n", sizeof(myIntcek));
  printf("%lu\n", sizeof(myFloatcek));
  printf("%lu\n", sizeof(myDoublecek));
  printf("%lu\n", sizeof(myCharcek));

  // Create variables of different data types
  int items = 50;
  float cost_per_item = 9.99;
  float total_cost = items * cost_per_item;
  char currency = '$';

  // Print variables
  printf("Number of items : %d\n", items);
  printf("Cost per item : %.2f %c\n", cost_per_item, currency);
  printf("Total cost = %.2f %c\n", total_cost, currency);

  // Automatic conversion: float to int
  int myInt = 9.99;

  printf("%d", myInt); // 9

  const int minutesPerHour = 60;
  const float PI = 3.14;

  printf("%d\n", minutesPerHour);

  int sum1 = 100 + 50;        // 150 (100 + 50)
  int sum2 = sum1 + 250;      // 400 (150 + 250)
  int sum3 = sum2 + sum2;     // 800 (400 + 400)
  printf("%d\n", sum1);
  printf("%d\n", sum2);
  printf("%d\n", sum3);

  int aku = 10;
  aku *= 5;

  printf("%d\n", aku);

  // Create boolean variables
  bool isProgrammingFun = true;
  bool isFishTasty = false;
  printf("%d\n", isProgrammingFun);  // Returns 1 (true)
  printf("%d", isFishTasty);         // Returns 0 (false)

  


    return 0;
  }

/*
jsafiishoooooo komennnnnn
*/

