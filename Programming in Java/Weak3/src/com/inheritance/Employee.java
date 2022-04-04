package com.inheritance;

public class Employee extends Human{
    static int empplyeeIndex;
    int empNum, salary;
    String orgenisation, designation;

    public Employee() {
        super();
        Employee.empplyeeIndex += 1;
        this.empNum = empplyeeIndex;
    }

    public Employee(int empNum, int salary, String orgenisation, String designation) {
        super();
        this.empNum = empNum;
        this.salary = salary;
        this.orgenisation = orgenisation;
        this.designation = designation;
    }

    public Employee(String name, int bom, int bod, int boy, double mobileNumber, boolean gender,
                    int empNum, int salary, String orgenisation, String designation) {
        super(name, bom, bod, boy, mobileNumber, gender);
        this.empNum = empNum;
        this.salary = salary;
        this.orgenisation = orgenisation;
        this.designation = designation;
    }

    void printEmpStatus(){
        super.printData();
        System.out.println("Employee id : " + this.empNum);
        System.out.println("Orgenisation : " + this.orgenisation);
        System.out.println("salary : " + this.salary);
        System.out.println("Designation : " + this.designation);
    }

    public static void main(String[] args) {
//        Employee e1 = new Employee("")
    }
}
