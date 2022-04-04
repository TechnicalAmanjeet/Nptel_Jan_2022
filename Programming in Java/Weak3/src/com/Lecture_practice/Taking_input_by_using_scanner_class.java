package com.Lecture_practice;

import java.util.Scanner;

public class Taking_input_by_using_scanner_class {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int[] array = new int[10];
        for(int i=0; i<10; ++i){
            System.out.print("Enter " + i+1 + "th value : ");
            int input_user = sc.nextInt();
            array[i] = input_user;
        }

        for(int i = 0; i<10; ++i){
            System.out.print(array[i] + " ");
        }
    }
}
