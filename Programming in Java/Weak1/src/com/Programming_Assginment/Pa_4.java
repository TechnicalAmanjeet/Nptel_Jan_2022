package com.Programming_Assginment;

import java.util.Scanner;

public class Pa_4 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n=sc.nextInt();
        int result=0;
//Use while loop check the number is Armstrong or not.
//store the output(1 or 0) in result variable.
        int original_number=n,sum=0;
        while (n>0){
            sum += Math.pow(n%10,3);
            n/=10;
        }
        if(sum==original_number) result=1;
        System.out.print(result);
    }
}
