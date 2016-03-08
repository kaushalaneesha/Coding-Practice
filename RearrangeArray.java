/* package whatever; // don't place package name! */
//https://www.careercup.com/question?id=5745017811369984
import java.util.*;
import java.lang.*;
import java.io.*;

/* Name of the class has to be "Main" only if the class is public. */
class Ideone
{
	public static void main (String[] args) throws java.lang.Exception
	{
		// your code goes here
		int[] arr = {2,4,1,3,0};
		Ideone.rearrangeArray(arr);
		for(int i=0;i<arr.length;i++){
			System.out.print(arr[i]+" ");
		}
	}
	public static void rearrangeArray(int[] arr){
		int newValue = 0;
		for(int i=0;i<arr.length;i++){
			newValue = arr[arr[i]]%arr.length;
			arr[i] = arr[i] + newValue*arr.length;
		}
		for(int i=0;i<arr.length;i++){
			arr[i]/=arr.length;
		}
	}
}