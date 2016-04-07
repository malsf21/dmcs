import java.util.Scanner;
import java.io.*;

public class Main {
	public static void main(String[] args) {
		try {
			Scanner scn = new Scanner(new File("vc.txt"));
			int count = Integer.parseInt(scn.nextLine());	
			String votes = scn.nextLine();
			int a = 0;
			int b = 0;
			for (int i = 0; i < count; i++){
				if (votes.charAt(i) == 'A'){
					a +=1;
				} else {
					b +=1;
				}
			}
			if (a == b){
				System.out.println("Tie");
			}
			else if (a > b){
				System.out.println("A");
			}
			else{
				System.out.println("B");
			}
		} catch (IOException e){
			System.out.println("Can't find file!");
		}
	}
}
