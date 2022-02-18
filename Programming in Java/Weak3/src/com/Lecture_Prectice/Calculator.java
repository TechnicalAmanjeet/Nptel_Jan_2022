package com.Lecture_practice;

public class Calculator {
    double x;
    double square_root = Math.sqrt(x);

    void show(){
        System.out.println("x : " + this.x);
        System.out.println("square root of " + this.x + " is "+ this.square_root + ".");
    }
}
