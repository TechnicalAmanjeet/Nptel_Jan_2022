package com.Lecture_practice;

public class Main {
    public static void main(String[] args) {
        // System.out.println("Start writing cmd from here onwards.");

//        Circle circle1 = new Circle();  // create new object of class circle.
//        // set attributes xcor and ycor of center of class Circle => ( 0 , 0 ).
//        circle1.xcor = 0;
//        circle1.ycor = 0;
//        circle1.r = 7;  // set the radius of circle => 7.
//
//        System.out.println("\nCircle obj => \n");
//
//        // printing attributes of obj circle1.
//        System.out.println("Center of circle1 is " + circle1.xcor + " , " + circle1.ycor);
//        circle1.area(); // calling area() method of circle.
//        circle1.circumference(); // calling perimeter() method of circle.

//        Circle circle2 = new Circle(); // created 2nd obj of class Circle.
//        circle2.xcor = 1; // set xcor of circle 2 to 1.
//        circle2.ycor = 1; // set ycor of circle 2 to 1.
//        circle2.r = 10; // set radius of circle to 10.
//
//        // printing attributes of obj circle2.
//        System.out.println("Center of circle2 is " + circle2.xcor + " , " + circle2.ycor);
//        circle2.area(); // calling area method of circle2 obj.
//        circle2.circumference(); // calling perimeter method of circle2 obj.
//
//        // double perimeter = 22/7 * 7 * 2;
//        // System.out.println(perimeter);

//        // create obj of cuboid class.
//        Cuboid cuboid = new Cuboid(); // creating cuboid obj.
//        cuboid.length = 10; // setting length of cuboid.
//        cuboid.width = 13; // setting width of cuboid.
//        cuboid.height = 15; // setting height of cuboid.
//
//        System.out.println("\nCuboid obj => \n");
//
//        // print all the attributes of cuboid class.
//        System.out.println("Length : " + cuboid.length + "\nWidth : " + cuboid.width + "\nHeight : " + cuboid.height);
//        cuboid.surface_area();  // calling surface_area method of cuboid.
//        cuboid.volume();  // calling volume method of cuboid.

//        // circle class starts.
//        System.out.println("Circle class =>  ");
//        Circle circle1 = new Circle(0, 0, 10);  // create an object of class circle and set the attribute value
//        // by using constructor.
//
//        // print the attribute value of circle class.
//        System.out.println("Xcor of circle : " + circle1.xcor);
//        System.out.println("Ycor of circle : " + circle1.ycor);
//        System.out.println("Radius of circle : " + circle1.r);
//
//        // calling diff. methods of circle class.
//        circle1.circumference();   // calling perimeter attributes.
//        circle1.area();  // calling area method.
//
//        // cuboid class starts from here.
//        System.out.println("Cuboid class =>  ");
//
//        Cuboid cuboid = new Cuboid(10, 12, 15); // created an object of type cuboid and set their attribute by using constructor.
//        // print all attributes of cuboid.
//        System.out.println("Length of cuboid : " + cuboid.length);
//        System.out.println("width of cuboid : " + cuboid.width);
//        System.out.println("height of cuboid : " + cuboid.height);
//
//        // call diff. attributes of class cuboid.
//        cuboid.surface_area(); // calling surface area method.
//        cuboid.volume(); // calling volume method.
//
//        // Point class
//        System.out.println("Point Class =>  ");
//        Point p1 = new Point(0, 0); // creating an obj and setting its attributes value by using constructor
//        System.out.println("Attributes of p1 : ");
//        p1.show_attributes(); // will show all the attributes of p1 obj.
//
//        Point p2 = new Point(1,1); // creating an obj and setting its attributes values by using constructor.
//        System.out.println("Attributes of p2 : ");
//        p2.show_attributes(); // will show all the attributes of p2 obj.
//
//        // print distance b/w point p1 and p2.
//        Point.distance(p1, p2);

//        // student class starts.
//        System.out.println("\nStudent class => ");
//        // creating an obj and setting their attributes value by using constructor.
//        Student student1 = new Student(1, "Amanjeet", "Kumar", "Programming in Java");
//        student1.show();
//
//        // creating another student obj and set the attributes by using diff. constructor.
//        Student student2 = new Student(2, "Riya", "Kumari", "Programming in Java", 2000);
//        student2.show();

        // calculator class starts from here.
        Calculator calc = new Calculator(); // creating an obj of calculator.
        calc.x = 16; // set the value of x for calc obj.
        calc.show();
        System.out.println(calc.square_root);
//        System.out.println(Math.sqrt(16));
        System.out.println("done till weak 2");
    }
}
