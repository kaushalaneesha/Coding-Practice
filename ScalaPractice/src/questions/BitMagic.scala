package questions

/**
  * Created by Aneesha on 2/26/2017.
  */
object BitMagic {
  def main(args: Array[String]) {
    println(findAnd(10,15))

  }
  def mostSig(a: Long) : Int = {
    def loop(aa : Long, count : Int ) : Int = {
      if(aa > 0 ) loop(aa >> 1,count+1) else count - 1
    }
    loop(a,0)
  }
  //find and of all numbers between two numbers. (Numbers are non negative)
  def findAnd(a:Long, b: Long) : Long = {
    def loop(aa: Long, bb: Long, res : Long) : Long = {
      val n = mostSig(aa)
      val m = mostSig(bb)

      if(n.equals(m)) {
        val pow = Math.pow(2,n).toLong
        loop(aa-pow,bb-pow,res + pow)
      }
      else res
    }
    loop(a,b,0)
  }
  //http://www.geeksforgeeks.org/multiplying-variable-constant-without-using-multiplication-operator/
  def multipleWithCons(n : Long, cons : Long) : Long  = {
    def loop(consLeft : Long, res : Long) : Long = {
      if(consLeft == 0)
        res
      else {
        val ms = mostSig(consLeft)
        val pow = Math.pow(2,ms).toLong
        val remainingPart = consLeft - pow
        loop(remainingPart, (n << ms) + res)
      }
    }

    val newNum = loop(Math.abs(cons),0)
    if(cons > 0) newNum
    else -newNum
  }


}
