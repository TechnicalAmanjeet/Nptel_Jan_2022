package com.Lecture_practice;

public class Main {
    public static void main(String[] args) {
        // System.out.println("Start writing cmd from here onwards.");

        Circle new_circle = new Circle();  // create new object of class circle.
        // set attributes xcor and ycor of center of class Circle => ( 0 , 0 )
        new_circle.xcor = 0;
        new_circle.ycor = 0;
        new_circle.r = 7;  // set the radius of circle => 7

        new_circle.area(); // called area() method of circle.
        new_circle.perimeter(); // call perimeter() method of circle.

    }
}
