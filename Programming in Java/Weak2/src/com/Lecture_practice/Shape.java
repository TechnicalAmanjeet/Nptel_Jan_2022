package com.Lecture_practice;

class Circle{
    double xcor, ycor;  // xcor and ycor represents the coordinates of center of circle.
    double r;  // represent radius of circle.

    void area(){
        // Print Area of Circle
        double area_of_circle = 22/7 * this.r * this.r;
        System.out.println("Area of circle with " + this.r + " is "+ area_of_circle);
    }

    void perimeter(){
        // print perimeter of circle
        double perimeter_of_circle = 2 * 22/7 * this.r;
        System.out.println("Perimeter of circle with "+ this.r + " is " + perimeter_of_circle);
    }

}

public class Shape {
}
