package example;

public class PrimeNumber {
	public static void main(String[] args) {
		int[] arr = {1,2,3,4,5,6,7};
		findPrime(arr);
	}

	private static void findPrime(int[] arr) {
		// TODO Auto-generated method stub
		int n = arr.length;
		for(int i=0;i<n;i++) {
			int count =0;
			for(int j=2;j<arr[i];j++) {
				if(arr[i]%j==0) {
					count++;
					break;
				}
			}
			if(count ==0) {
				System.out.println(arr[i]);
			}
		}
		
	}

}
