/* This is my banner - notice the multi-line comments
 * 
 * constructs.java
 * This program demonstrates the basic constructs of all programming languages
 * SSRGMIO - Sequential, Selection, Repetition, Graphics, Modularity, File input output
*/

//External libraries are here outside the class
import java.io.File;
import java.io.IOException;
import java.io.FileNotFoundException;
import java.io.PrintWriter;
import java.util.Scanner;
import javax.swing.JFrame;

public class constructs {
	
	// MODULARITY - this is the most simple method / function / module I could think of
	public static int squared(int x) {
		return  x * x;
	}

	public static void main(String[] args) {
		
		// SEQUENTIAL - notice the single line comment is not compiled
		String phrase = "All languages are Sequential";
		System.out.print(phrase);
		System.out.print("\n"); // this places a new line
		
		// SELECTION - most basic program flow control construct
		Integer favnum = 7; // Notice how variables in java must be declared, this is called a strongly typed language
		if (favnum < 10) {
			System.out.print("Favourite number is less than 10");
		} else if (favnum > 10) {
			System.out.print("Favourite number is greater than 10");
		} else {
			System.out.print("Favourite number is 10");
		}
		System.out.print("\n");
		
		// REPETITION
		for (int i = 0; i < 10; i++ ) {
			System.out.print(i + " time through");
			System.out.print("\n");
		}
		
		// GRAPHICS - use external library to draw a window
		JFrame frame = new JFrame();
		frame.setSize(400, 300);
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE); // set what happens when you exit
		frame.setVisible(true); // show the window
		
		// MODULARITY - break your program into byte :-) size chunks 
		// Modularity increases readability, re-usability of code and reduce bugs
		System.out.print(squared(3) + "\n"); // see squared method at the top of the program
		
		// FILE IO - Notice there is a try and catch block around it with a useful message
		// try catch blocks are called exception or error handling
		try {
			Scanner myscan = new Scanner(new File("stuff/teams.txt"));
			PrintWriter writer = new PrintWriter("stuff/the-file-name.txt");
			String line;
			
			// This code uses a while loop to go through file while not on last line
			while (myscan.hasNext())
		        {
				line = myscan.nextLine();
				System.out.print(line + "\n");
			        if (line.trim().equals("Leafs")) { // cool 'trim' and 'equals' method use for comparison with strings 
	            			writer.println(line + " are the best");
	            		} else {
	            			writer.println(line + " are ok");
	            		} 
	        	}
			writer.close(); // must close or won't write
		// List of Java exceptions - http://www.tutorialspoint.com/java/java_builtin_exceptions.htm
		} catch (FileNotFoundException e) {
			System.out.print("Can not find the file.");
		}
	}
}