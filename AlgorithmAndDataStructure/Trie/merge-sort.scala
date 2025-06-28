object Algorithm extends App {
  def mergeSort[T: Ordering](items: IndexedSeq[T]): IndexedSeq[T] = {
    if (items.length <= 1) {
      return items
    } else {
      val (left, right) = items.splitAt(items.length / 2)
      val (sortedLeft, sortedRight) = (mergeSort(left), mergeSort(right))
      var (leftIdx, rightIdx) = (0, 0)
      val output = IndexedSeq.newBuilder[T]
      while (leftIdx < sortedLeft.length || rightIdx < sortedRight.length) {
        val takeLeft =
          (leftIdx < sortedLeft.length, rightIdx < sortedRight.length) match {
            case (true, false) => true
            case (false, true) => false
            case (true, true) =>
              Ordering[T].lt(sortedLeft(leftIdx), sortedRight(rightIdx))
            case (false, false) => false
          }
        if (takeLeft) {
          output += sortedLeft(leftIdx)
          leftIdx += 1
        } else {
          output += sortedRight(rightIdx)
          rightIdx += 1
        }
      }
      return output.result()
    }
  }

//   val testArray = Array(64, 34, 25, 12, 22, 11, 90)
  val testArray = Array("b", "a", "aa", "c", "db", "ac")
  println("元の配列: " + testArray.mkString(", "))
  val sortedArray = mergeSort(testArray)
  println("ソート後: " + sortedArray.mkString(", "))
}
