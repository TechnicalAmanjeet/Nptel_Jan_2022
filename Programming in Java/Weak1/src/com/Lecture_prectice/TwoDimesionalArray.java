package com.Lecture_prectice;

public class TwoDimesionalArray {
    public static void main(String[] args) {
        int[][] twoDarray = new int[3][4]; // initialization and memory allocation

        System.out.println(twoDarray.length);
        System.out.println(twoDarray[0].length);

        for(int i=0;i<twoDarray.length;++i){
            for(int j=0;j<twoDarray[i].length;++j){
                twoDarray[i][j] = i*j;  // adding value to each box of two d array.
            }
        }

        for(int i=0;i<twoDarray.length;++i){
            for(int j=0;j<twoDarray[i].length;++j){
                System.out.print(twoDarray[i][j] + " "); // displaying the value of 2d array.
            }
            System.out.println();
        }


    }
}
