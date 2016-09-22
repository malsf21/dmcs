public class chocolate{

	public static String wrapper(String chocolate, int bars){
		String answer = "";
		if (chocolate.length() > 3){
			chocolate = chocolate.substring(0,3);
		}
		for (int i = 0; i < bars; i ++){
			answer += chocolate;
		}
		return answer;
	}
	public static void main(String[] args){
		String chocolate = "chocolate";
		int bars = 3;

		System.out.println(wrapper(chocolate, bars));
	}

}
