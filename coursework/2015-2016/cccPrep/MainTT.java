import java.util.Scanner;
import java.io.*;

public class Main {
	public static void main(String[] args) {
		try {
			Scanner scn = new Scanner(new File("tt.txt"));
			int a = Integer.parseInt(scn.nextLine());	
			int b = Integer.parseInt(scn.nextLine());
			int c = Integer.parseInt(scn.nextLine());

			if (a + b + c != 180){
				System.out.println("Error");
			}
			else if (a == b && b == c){
				System.out.println("Equilateral");
			}
			else if (a == b || b == c || a == c){
				System.out.println("Isoceles");
			}
			else {
				System.out.println("Scalene");
			}
		} catch (IOException e){
			System.out.println("Can't find file!");
		}
	}
}
