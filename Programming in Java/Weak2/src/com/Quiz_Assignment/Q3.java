package com.Quiz_Assignment;

public class Q3 {
    public static void main(String[] args) {
        char[] copyfrom = {'j','a','n','n','p','t','e','l','j','a','v','a'};
        char[] copyto = new char[9];
        System.arraycopy(copyfrom, 3 , copyto, 0, 9);
        System.out.println(copyfrom);
        System.out.println(copyto);
    }
}
