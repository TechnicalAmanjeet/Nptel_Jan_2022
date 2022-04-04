package com.inheritance;

public class Human {
    int numOfHuman;
    String name;
    int bod, boy, bom;
    double mobileNumber;
    boolean gender;
    static int numHuman;

    public Human() {
        numHuman += 1;
        this.numOfHuman = Human.numHuman;
    }

    public Human(String name) {
        this();
        this.name = name;
    }

    public Human(String name, int bom, int bod, int boy, double mobileNumber, boolean gender) {
        this();
        this.name = name;
        this.bom = bom;
        this.bod = bod;
        this.boy = boy;
        this.mobileNumber = mobileNumber;
        this.gender = gender;
    }

    void readData(String name, int bom, int bod, int boy, double mobileNumber, boolean gender){
        this.name = name;
        this.bom = bom;
        this.bod = bod;
        this.boy = boy;
        this.mobileNumber = mobileNumber;
        this.gender = gender;
    }

    void printData(){
        System.out.println("He/She is " + this.numOfHuman + "th human of " + Human.numHuman + " here.");
        System.out.println("Name : " + this.name);
        String gender = (this.gender == true) ? "male" : "female";
        System.out.println("Gender : " + gender);
        System.out.println("Mobile : "+ this.mobileNumber);
        System.out.println("Dob : " + this.bod + "/" + this.bom + "/" + this.boy);
        System.out.println();
    }


    public static void main(String[] args) {
        Human h1 = new Human("Amanjeet Kumar", 21, 12, 2000, 620901227,true);
        Human h2 = new Human("Riya",21,12,2005,3434059,false);
        h1.printData();
        h2.printData();
    }
}
