package questions

/**
  * Created by Aneesha on 3/12/2017.
  */
object Encoder {
  def main(args: Array[String]): Unit = {
    allValidEncodedValues("12")
  }

  def toAlphabet(i : Int): String = (i+64).toChar.toString

  def allValidEncodedValues(ss : String): Any = {
    def loop(str : String, acc : String) : Unit = {
      if(str.isEmpty) print(acc)
      else if (str.length == 1) print(acc + toAlphabet(str.toInt))
      else{
        val secPart = str.substring(0,2)
        loop(str.substring(2,str.length), acc + toAlphabet(secPart.toInt))
        println
        val firstPart = str.substring(0,1)
        loop(str.substring(1,str.length), acc + toAlphabet(firstPart.toInt))
      }
    }
    loop(ss,"")
  }

}
