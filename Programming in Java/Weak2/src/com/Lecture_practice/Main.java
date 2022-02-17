package com.Lecture_practice;

public class Main {
    public static void main(String[] args) {
        // System.out.println("Start writing cmd from here onwards.");

        Circle circle1 = new Circle();  // create new object of class circle.
        // set attributes xcor and ycor of center of class Circle => ( 0 , 0 ).
        circle1.xcor = 0;
        circle1.ycor = 0;
        circle1.r = 7;  // set the radius of circle => 7.

        // printing attributes of obj circle1.
        System.out.println("Center of circle1 is " + circle1.xcor + " , " + circle1.ycor);
        circle1.area(); // calling area() method of circle.
        circle1.perimeter(); // calling perimeter() method of circle.

        Circle circle2 = new Circle(); // created 2nd obj of class Circle.
        circle2.xcor = 1; // set xcor of circle 2 to 1.
        circle2.ycor = 1; // set ycor of circle 2 to 1.
        circle2.r = 10; // set radius of circle to 10.

        // printing attributes of obj circle2.
        System.out.println("Center of circle2 is " + circle2.xcor + " , " + circle2.ycor);
        circle2.area(); // calling area method of circle2 obj.
        circle2.perimeter(); // calling perimeter method of circle2 obj.

        // double perimeter = 22/7 * 7 * 2;
        // System.out.println(perimeter);
    }
}
