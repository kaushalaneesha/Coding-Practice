package practice
/**
  * Created by akaushal on 3/10/2017.
  **/
object ListSubstring {
  def listIncreasingSubstring(str : String): List[String] = {
    def loop(start : Int, end : Int, result : List[String]) : List[String] = {
      val sub = str.substring(start,end+1)
      //See if this substring is strictly increasing
      val correctStart = everyCharIsGreaterThanLast(str,start,end)
      //Add the substring if it is increasing
      val newResult = if(correctStart) sub :: result else result
      //further loop conditions
      if(end == str.length - 1 && start == str.length - 2) newResult
      //checking correctStart here so that if a substring is not increasing from a fixed start there is no point in checking further from that start
      else if (end == str.length - 1 || !correctStart) loop(start+1,start+2,newResult)
      else loop(start,end+1,newResult)
    }
    loop(0,1,Nil)
  }

  def everyCharIsGreaterThanLast(str: String, start : Int, end: Int) : Boolean = {
    if (start == end) true
    else if(str.charAt(start) >= str.charAt(start+1)) false
    else everyCharIsGreaterThanLast(str,start+1,end)
  }
}
