package com.Amanjeet.Programming_Assignment;

import java.sql.*;
import java.lang.*;
import java.util.Scanner;

public class paq2 {

        public static void main(String args[]) {
            try {
                Connection conn = null;
                Statement stmt = null;
                String DB_URL = "jdbc:sqlite:/tempfs/db";
                System.setProperty("org.sqlite.tmpdir", "/tempfs");


            }
            catch(Exception e){ System.out.println(e);}
        }
}


