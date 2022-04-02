package com.Amanjeet.weak1;

import java.applet.Applet; // importing applet class in this program
import java.awt.*;  // importing for all methods and class of java.awt class.

public class HelloWorldApplet extends Applet { // including applet superclass in this class.
    public void paint(Graphics g){
        g.drawString("Amanjeet loves Riya", 0,0);
    }
}
