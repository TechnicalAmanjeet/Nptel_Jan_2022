package com.Solving_Quiz_Assignment;

class Men{
    int wd(int weight){
        System.out.println(10);
        return 10;
    }
}

class Wildman extends Men {
    int wd(int weight) {
        System.out.println("20");
        return 20;
    }
}
//    void wd(int weight){
//        System.out.println("20");
//    }
//}

public class Q5 {
    public static void main(String[] args) {
        Wildman wc = new Wildman();
        wc.wd(30);
    }
}
