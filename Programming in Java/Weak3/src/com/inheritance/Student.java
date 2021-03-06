package com.inheritance;

public class Student extends Human{
    String instituation;
    int rollNum, marks;

    public Student() {
        super();
    }

    public Student(String instituation, int rollNum, int marks) {
        this();
        this.instituation = instituation;
        this.rollNum = rollNum;
        this.marks = marks;
    }

    public Student(String name, int bom, int bod, int boy, double mobileNumber, boolean gender,
                   String instituation, int rollNum, int marks) {
        super(name, bom, bod, boy, mobileNumber, gender);
        this.instituation = instituation;
        this.rollNum = rollNum;
        this.marks = marks;
    }

    void printBioData(){
        super.printData();
        System.out.println("Instituation : " + this.instituation);
        System.out.println("Roll Num : " + this.rollNum);
        System.out.println("marks : " + this.marks);
    }
}
