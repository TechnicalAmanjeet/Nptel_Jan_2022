package com.Solving_Quiz_Assignment;

public class Q2 {
    public static int x = 7;

    public static void main(String[] args) {
        Q2 a = new Q2();
        Q2 b = new Q2();

        a.x = 2;
        b.x = 2;
        System.out.println(a.x + b.x + Q2.x);
    }
}
