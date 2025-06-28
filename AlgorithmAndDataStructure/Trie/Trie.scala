class Trie {
  class Node(
      var hashValue: Boolean,
      val children: collection.mutable.Map[Char, Node] =
        collection.mutable.Map()
  )
  val root = new Node(false)
}
