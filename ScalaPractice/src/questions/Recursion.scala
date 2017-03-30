package questions

/**
  * Created by Aneesha on 3/22/2017.
  */
object Recursion {

  def main(args: Array[String]): Unit = {
    pascalTriangle(readInt)
  }

  def pascalTriangle(num : Int) : Unit = {
    def loop(n : Int, r : Int) : Unit = {
      if(n>num) println()
      else if(r<=n) {
        print(factorial(n) / (factorial(r) * factorial(n-r)))
        loop(n,r+1)
      }else {
        println()
        loop(n+1,0)
      }
    }
    loop(0,0)
  }
  val fact = Array.fill(100)(-1)
  def factorial(n : Int): Int = {
    def loop(nn : Int,res : Int) : Int = {
      if(nn>1) loop(nn-1,res*nn)
      else res
    }
    if(fact(n) == -1) loop(n,1) else fact(n)
  }
}
