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
		String str = "Time and tide wait for No Man";
		Ideone.countAlphabet(str);
		
		
	}
	public static void countAlphabet(String str){
		char[] charr = str.toCharArray();
		int[] alphaCount = new int[26];
		for(int i=0;i<charr.length;i++){
			if(charr[i]>=97 && charr[i]<=122){
				alphaCount[charr[i]-97]++;
			}else if(charr[i]>=65 && charr[i]<=90){
				alphaCount[charr[i]-65]++;
			}
		}
		for(int i=0;i<26;i++){
			System.out.println(Character.toString ((char) (i+97))+": "+alphaCount[i]);
		}
	}
}