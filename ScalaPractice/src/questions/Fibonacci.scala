package questions

/**
  * Created by Aneesha on 3/19/2017.
  */
object Fibonacci {
  def fibonacci(x:Int):Int = {

    // Fill Up this function body
    // You can add another function as well, if required
    if(x==1) 0
    else if(x == 2) 1
    else fibonacci(x-1) + fibonacci(x-2)
  }

  def main(args: Array[String]) {
    /** This will handle the input and output**/
    println(fibonacci(readInt()))

  }
}
