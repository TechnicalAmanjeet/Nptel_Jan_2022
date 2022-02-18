package com.Programming_Assignment;

// This is the class named Printer
class Printer {
    // This are the methods in class Printer
    public void print() {
        System.out.println("Hi! I class SCHOOL.");
    }
    public void print(String s) {
        System.out.println(s);
    }
}

public class Question22{
    public static void main(String[] args) {

// Create an object of class Printer
        Printer p = new Printer();
// Call 'print()' methods for desired output
        String s="Hi! I am class STUDENT";
        p.print(s);
        p.print();

    }
}