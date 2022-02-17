package com.Lecture_practice;

public class Student {
    int roll_number;
    String first_name, last_name, course;
    float fee;

    Student(int roll_number, String first_name, String last_name, String course){
        this.roll_number = roll_number;
        this.first_name = first_name;
        this.course = course;
    }

    Student(int roll_number, String first_name,String last_name, String course, float fee){
        new Student(roll_number,first_name, last_name, course); // calling the above constructor.
        this.fee = fee;
    }

    void show(){
        System.out.println("\nRoll Number : " + this.roll_number + " .");
        System.out.println("Name : " + this.first_name + " " + this.last_name + ".");
        System.out.println("Course Name : " + this.course);
        System.out.println("Fee : " + this.fee);
    }
}
