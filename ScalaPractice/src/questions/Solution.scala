// main method in "Solution" will be run as your answer
object Solution {

  def main(args: Array[String]): Unit = {
    val input = readLine().split(" ").map(_.toLowerCase)
    val m = readInt()
    val finalmap = scala.collection.mutable.HashMap.empty[Int,scala.collection.mutable.Map[String,Int]]
    for (i <- 0 to m * 2) {
      val id = readInt()
      val arrWords = readLine().filterNot( x=> x == ',' || x == '.').split(" ").map(_.toLowerCase)
      val map = scala.collection.mutable.HashMap.empty[String,Int]
      arrWords foreach {
        wrd => if(map.contains(wrd)) map.put(wrd,map(wrd) + 1)
        else map.put(wrd,1)
      }

      if(finalmap.contains(id)) finalmap.put(id,finalmap(id) ++ map.map{ case (k,v) => k -> (v + finalmap(id).getOrElse(k,0)) })
      else finalmap.put(id,map)
    }

//      val set = finalmap.keySet
//    val countM = scala.collection.mutable.HashMap.empty[Int, Int]
//      set foreach{ id => {
//        input.foreach{
//          wrd => finalmap(id).get(wrd) map {
//            value => if(countM.contains(id)) countM.put(id,countM(id) + value) else countM.put(id,value)
//          }
//        }
//      }
        println(finalmap)
 //     }
  }


  def polygon = {
    //Enter your code here. Read input from STDIN. Print output to STDOUT

    var square = 0
    var rec = 0
    var other = 0
    var ok = true
    while (ok) {
      val ln = readLine()
      ok = ln != null
      if (ok) {
        val arr = ln.split(" ").map(_.toInt)
        if(arr(0) == arr(1) && arr(2) == arr(1) && arr(2) == arr(3))
          square = square + 1
        else if (arr(0) == arr(2) && arr(1) == arr(3)){
          if(arr(0)>0 && arr(1)<0 || arr(1)>0 && arr(0)<0)
            other = other + 1
          else
            rec = rec + 1
        }
        else
          other = other + 1

      }
    }
    print(square + " "+rec+" "+other )
  }

}