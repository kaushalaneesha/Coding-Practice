package questions

/**
  * Created by Aneesha on 3/13/2017.
  */
//https://www.careercup.com/question?id=5091778836299776
object SubsetCount {

  def binarySearch(nums: Array[Int], start :Int, end : Int, x: Int) : Option[Int] = {
    val mid = (start+end) / 2
    if(nums(mid)==x) if(mid>0) Some(mid-1) else None
    else if(nums(mid)>x) if(mid==0) None else binarySearch(nums,start,mid,x)
    else {
      if(mid == nums.length-1) Some(mid)
      else if (nums(mid+1)<x) binarySearch(nums,mid,end,x)
      else Some(mid)
    }
  }

  def countSubSet(nums : Array[Int], target : Int) : Option[Int] = {
    val sortedNums = nums.sorted
    //Find the position of element less just than target so that we dont check after that position,
    //as all will be invalid (in other words greater that what we need)
    val posLimit = if(target%2==0)
      binarySearch(sortedNums,0,sortedNums.length-1,target/2)
    else
      binarySearch(sortedNums,0,sortedNums.length-1,(target/2)+1)
    //length is the length of subset taken
    def loop(arr: Array[Int],length: Int, count: Int, pos: Int, posLimit : Int) : Int = {
      if(length>posLimit+1) count
      else if(pos > posLimit || pos+length > arr.length) loop(arr,length+1,count,0,posLimit)
      else if(isValid(arr,length,pos)) loop(arr,length,count+1,pos+1,posLimit)
      else loop(arr,length+1,count,0,posLimit)
    }
    //check if the subset is valid
    def isValid(arr: Array[Int],length: Int, pos: Int) = arr(pos) +arr(pos+length-1) < target
    posLimit map (loop(sortedNums,1,0,0,_))
  }

  def main(args: Array[String]): Unit = {
    println(binarySearch(Array(8,10,5,4,9,2).sorted,0,5,10))
  }
}
