package com.Solving_Quiz_Assignment;

class A{
    public int i;
    protected int j;
}

class B extends A{
    void display(){
        super.j = super.j - super.i;
        System.out.println(super.i+" "+super.j);
    }
}

public class Q1 {
    public static void main(String[] args) {
        B obj = new B();
        obj.i = 3;
        obj.j = 6;
        obj.display();
    }
}
