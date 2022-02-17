package com.Lecture_practice;

public class Point {
    double x;
    double y;

    Point(){
        this.x = this.y = 0;
    }

    Point(double x, double y){
        this.x = x;
        this.y = y;
    }

    Point(double x){
        this.x = this.y = x;
    }

    static void distance(Point p1, Point p2){
        double x = p1.x - p2.x;
        double y = p1.y - p2.y;
        double distance = Math.sqrt(x * x + y * y);
        System.out.println("Point 1 : ");
        p1.show_attributes();
        System.out.println("Point 2 : ");
        p2.show_attributes();

        System.out.println("Distance b/w point p1 and p2 : " + distance + " unit.");
    }

//    void distance(Point p){
//        double distance = Math.sqrt(p.x * p.x + p.y * p.y);
//        p.show_attributes();
//        System.out.println("The distance from origin to p is "+ distance + " units.");
//    }

    void show_attributes(){
        // will display all the attributes of this class.
        System.out.println("Xcor : " + this.x);
        System.out.println("Ycor : " + this.y);
    }
}
