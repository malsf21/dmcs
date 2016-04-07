import java.io.File;
import java.util.*;
import java.io.IOException;
import java.io.FileNotFoundException;
import java.util.Scanner;
import javax.swing.JFrame;
import javax.swing.JLabel;

public class names{
	public static void main(String[] args) {
			JFrame frame = new JFrame();
			JLabel gonames = new JLabel();
			JLabel banames = new JLabel();
			String goonames = "";
			String badnames = "";

			frame.setSize(1600, 900);
			frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE); // set what happens when you exit

			List<String> gnames = new ArrayList<String>();
			List<String> bnames = new ArrayList<String>();
			try {
				Scanner myscan = new Scanner(new File("names.txt"));
				String line;
				
				// This code uses a while loop to go through file while not on last line
				while (myscan.hasNext())
			        {
					line = myscan.nextLine();
					System.out.print(line + "\n");
				        if (line.trim().equals("matthew")) { // cool 'trim' and 'equals' method use for comparison with strings 
		            			gnames.add(line);
		            		} else if (line.trim().equals("matt")) { // cool 'trim' and 'equals' method use for comparison with strings 
		            			gnames.add(line);
		            		}
		            		else {
		            			bnames.add(line);
		            		} 
		        	}
		// List of Java exceptions - http://www.tutorialspoint.com/java/java_builtin_exceptions.htm
			} catch (FileNotFoundException e) {
				System.out.print("Can not find the file.");
			}
			for (String s : gnames){
				goonames += s + "\t";
			}
			for (String s : bnames){
				badnames += s + "\t";
			}
			gonames.setText("The best names I've ever seen are: " + goonames + "\n while the rest of these names " + badnames + "are okay, I guess");
			//banames.setText("The rest of these names " + badnames + "are okay, I guess.");
			gonames.setLocation(0,0);
			//banames.setLocation(0,100);
			frame.add(gonames);
			//frame.add(banames);
			frame.setVisible(true); // show the window
	}
}