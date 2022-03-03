package com.Amanjeet.Programming_Assignment;

import java.util.Scanner;

public class Question5_3 {
    public static void main(String[] args) {
        int a, b;
        Scanner input = new Scanner(System.in);

        a= input.nextInt();
        b= input.nextInt();
        try{
            System.out.println(a/b);
        }catch (ArithmeticException e){
            System.out.println("Exception caught: Division by zero.");
        }
    }
}
