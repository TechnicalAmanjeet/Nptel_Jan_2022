package com.Programming_Assginment;


import java.util.Scanner;

public class Pa_2 {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        int x = s.nextInt();
        int y = s.nextInt();
        int z = s.nextInt();
        int result = 0;
//Use if...else ladder to find the largest among 3 numbers and store the largest number in a variable called result.
        result = Math.max(Math.max(x,y),z);
        System.out.print(result);
    }
}
