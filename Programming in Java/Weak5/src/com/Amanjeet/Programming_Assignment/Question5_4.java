package com.Amanjeet.Programming_Assignment;

//Prefixed Fixed Code:
import java.util.*;
public class Question5_4 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int length = sc.nextInt();
        // create an array to save user input
        int[] name = new int[length];
        int sum = 0;//save the total sum of the array.
        for(int i=0;i<length;++i){
            try{
                name[i] = sc.nextInt();
                sum += name[i];
            }catch (InputMismatchException e){
                System.out.println("You entered bad data.");
                return;
            }
        }
        System.out.println(sum);
    }
}
