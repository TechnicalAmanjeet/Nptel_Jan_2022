package com.Programming_Assginment;

import java.util.Scanner;

public class Pa_1 {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        double radius= s.nextDouble();
        double perimeter;
        double area;
//Calculate the perimeter
        //Calculate the area
        double pi = Math.PI;
        perimeter = 2*pi*radius;
        area = pi*Math.pow(radius,2);
        System.out.println(perimeter);
        System.out.print(area);

    }
}
