/* package whatever; // don't place package name! */

import java.util.*;
import java.lang.*;
import java.io.*;

/* Name of the class has to be "Main" only if the class is public. */
class Ideone
{
	public static void main (String[] args) throws java.lang.Exception
	{
		// your code goes here
		int[] arr  = {8,2,5,3,1,7};
		Ideone.weirdSorting(arr);
		for(int i=0;i<arr.length;i++){
			System.out.print(arr[i]+"	");
		}
	}
	
	static void weirdSorting(int[] arr){
		int max = 0;
		int temp = 0;
		for(int i=1;i<arr.length;i+=2){
			max = Ideone.findMax(arr,i);
			temp = arr[max];
			arr[max] = arr[i];
			arr[i] = temp;
		}
		
	}
	static int findMax(int[] arr, int i){
		int max = 0;
		if(i<arr.length-1){
				max = arr[i]>arr[i-1]? i:i-1;
				max = arr[i+1]>arr[max]? i+1:max;
		}else{
			max = arr[i]>arr[i-1]? i:i-1;
		}
			System.out.println(max +"max	");
		return max;
	}
}