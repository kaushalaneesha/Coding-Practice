package practice

/**
  * Created by akaushal on 3/10/2017.
  **/
object RotateList {
  def rotateList(list : List[Int], k : Int) : List[Int] = list.drop(k)++list.take(k)
}
