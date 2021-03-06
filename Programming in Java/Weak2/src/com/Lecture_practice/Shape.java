package com.Lecture_practice;

class Circle{
    double xcor, ycor;  // xcor and ycor represents the coordinates of center of circle.
    double r;  // represent radius of circle.

    Circle(double x, double y, double r){
        this.xcor = x;
        this.ycor = y;
        this.r = r;
    }

    Circle(double x, double r){
        this.xcor = this.ycor = x;
        this.r = r;
    }

    void area(){
        // Print Area of Circle
        double area_of_circle = 22/7 * this.r * this.r;
        System.out.println("Area of circle with radius " + this.r + " is "+ area_of_circle);
    }

    void circumference(){
        // print perimeter of circle
        double perimeter_of_circle = 2 * 22/7 * this.r;
        System.out.println("Circumference of circle with radius  "+ this.r + " is " + perimeter_of_circle);
    }

}

class Cuboid{
    double length, width, height;  // defined l, w and h of Cuboid class.

    Cuboid(double l, double w, double h){
        this.length = l;
        this.width = w;
        this.height = h;
    }

    Cuboid(double l, double h){
        this.length = this.width = l;
        this.height = h;
    }

    Cuboid(double l){
        this.length = this.height = this.width = l;
    }

    void surface_area(){
        // print surface area of cuboid.
        double l = this.length, w = this.width, h = this.height;
        double surface_area = 2 * ( l*w + w*h + h*l);
        System.out.println("Surface Area of cuboid is : " + surface_area);
    }

    void volume(){
        // print volume of cuboid.
        double l = this.length, w = this.width, h = this.height;
        double volume = l * w * h;
        System.out.println("Volume of cuboid : " + volume);
    }
}

public class Shape {
    public static void main(String[] args) {
        // create new obj of class Circle.

    }
}
