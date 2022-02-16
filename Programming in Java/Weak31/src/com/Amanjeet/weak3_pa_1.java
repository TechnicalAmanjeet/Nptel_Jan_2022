package com.Amanjeet;

public class weak3_pa_1 {

    class Point{
        double x,y;

        public void distance(Point p1, Point p2){
            double x1 = p1.x, x2 = p2.x, y1=p1.y, y2 = p2.y;
            double first = x2 -x1, second = y2-y1;
            first = first * first;
            second = second * second;
            double distance = Math.sqrt(first + second);
            System.out.println(distance);
        }
    }

}
