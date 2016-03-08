/* package whatever; // don't place package name! */
//https://www.careercup.com/question?id=5695660973096960
import java.util.*;
import java.lang.*;
import java.io.*;

/* Name of the class has to be "Main" only if the class is public. */
class Ideone
{
	public static void main (String[] args) throws java.lang.Exception
	{
		// your code goes here
		int x=4;
		int max = 7;
		System.out.print(Ideone.sum(x,max));
	}
	public static int sum(int x, int max){
		if(x==max)
		  return max;
		else 
			return x + sum(x+1,max);
	}
}