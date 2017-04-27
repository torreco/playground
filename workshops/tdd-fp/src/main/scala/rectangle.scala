 
case class Rectangle (width: Double, height: Double) {  
  val area = (width * height)
  val perimeter = (2*width) + (2*height)

  def biggerThan (r:Rectangle) = (area > r.area)  
}

