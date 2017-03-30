package questions
import scala.io.StdIn._
/**
  * Created by Aneesha on 3/19/2017.
  */
object Polygon {
  case class Point(x : Int, y : Int)

  def findPerimeter : Double = {
    val points = ( 1 to readInt ).map( _ => readLine.split(" ")).map{ case Array(x,y) => Point(x.toInt, y.toInt)}.toList
    val polyLines = points :+ points.head
    polyLines.tail.foldLeft((0.0,polyLines.head)) {
      case (acc,p) => (acc._1 + distance(acc._2, p) , p)
    }._1
  }
  def distance(p1 : Point, p2 : Point ) : Double = Math.sqrt(Math.pow(p1.x - p2.x, 2.0) + Math.pow(p1.y - p2.y, 2.0))

  def main(args: Array[String]): Unit = {
    println(findPerimeter)
  }
}
