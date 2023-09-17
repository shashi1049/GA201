package example;

public class Copains {
	public static void main(String[] args) {
		int[] arr = {1,2,3,4,5};
		printElement(arr);
	}

	private static void printElement(int[] arr) {
		// TODO Auto-generated method stub
		//length of array
		int n = arr.length;
		//iterating through array
		for(int i=0;i<n;i++) {
			System.out.println(arr[i]);
		}
		
	}

}
