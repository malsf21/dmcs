public class hello{
	//if a main method exists, it will autorun w/out calling it
	public static void main(String[] args){
		int num = 7;
		if (num < 10){
			System.out.println("Barney Stinson here, ");
			if (num == 0){
				System.out.println("BARNABYYYYYYYYY");
			}
		}
		else if (num > 10){
			System.out.println("Teh Schmosby here, ");
		}
		else{
			System.out.println("Robin Scherbosky here, ");
		}
		System.out.println("Helllllllllloooooooo New York");

		for(int i=0;i<5;i++){
			System.out.println("Haaaaaaave you met Ted?");
		}
		num = 0;
		while (num<5){
			System.out.println("Ted has only been dumped by " + num+1 + " girls.");
			num ++;
		}
		num = 0;
		do {
			System.out.println("Barney's been with "+ num+7*3/2*27+7 + " girls.");
			num ++;
		} while (num<5);
	}
}