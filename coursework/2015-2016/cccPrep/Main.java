import java.util.Scanner;
import java.io.*;

public class Main {
	public static void main(String[] args) {
		try {
			Scanner scn = new Scanner(new File("sd.txt"));
			int month = Integer.parseInt(scn.nextLine());
			int day  = Integer.parseInt(scn.nextLine());
			if (month == 2 && day == 18){
				System.out.println("Special");
			}
			else if (month == 2 && day < 18){
				System.out.println("Before");
			}
			else if (month <2){

				System.out.println("Before");
			}
			else {
				System.out.println("After");
			}	
		} catch (IOException e){
			System.out.println("Can't find file!");
		}
	}
}
