package com.Programming_Assginment;

import java.util.Scanner;

public class Pa_3 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int sum = 0;
//Use for or while loop do the operation.
        for (int i = 0; i >= 0; i += 2) {
            if (i % 3 == 0) sum += i;
            n -= 1;
            if (n == 0) break;
        }
        System.out.print(sum);
    }
}
