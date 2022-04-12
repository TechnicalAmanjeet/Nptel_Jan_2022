package com.Lecture_practice;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.Statement;

public class test {
        public static void main(String args[]) {
            try {
                Connection conn = null;
                Statement stmt = null;
                String DB_URL = "jdbc:sqlite:/tempfs/db";
                System.setProperty("org.sqlite.tmpdir", "/tempfs");

                // JDBC Codes in the hidden section

                // Open a connection
                conn = DriverManager.getConnection(DB_URL);
                System.out.print(conn.isValid(1));
                conn.close();

// JDBC Codes in the visible section

            }
            catch(Exception e){ System.out.println(e);}
        }
}
