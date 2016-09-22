public class q2{
	public static int commonTwo(String[] array1, String[] array2){
		int appear = 0;
		for (int i = 0; i < array1.length; i++){
			for (int j = 0; j < array2.length; j++){
				if (array1[i] == array2[j]){
					appear += 1;
				}
			}
		}
		return appear;
	}
	public static void main(String[] args){
		String arr1[] = {"a", "c", "x"};
		String arr2[] = {"a", "b", "c", "d", "x"};

		System.out.println(commonTwo(arr1, arr2));
	}

}
