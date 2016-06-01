public class q1{
	public static String delDel(String original){
		if (original.substring(1,4).contains("del") == true){
			original = original.substring(0, 1)  + original.substring(4);
		}
		return original;
	}
	public static void main(String[] args){
		System.out.println(delDel("aadelHello"));
	}

}
