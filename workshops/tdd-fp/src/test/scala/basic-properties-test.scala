import org.scalacheck._
import org.scalacheck.Prop._
import java.lang.Math

object PropertiesTest extends Properties("Properties") {

  property("List reverse") = forAll { l: List[String] =>
    l.reverse.reverse == l
  }

  property("Lists size") = forAll { (a: List[String], b: List[String]) =>
    a.size + b.size == (a ::: b).size
  }

  property("Lists reverse") = forAll { (a: List[String], b: List[String]) =>
    (b ::: a).reverse == (a.reverse ::: b.reverse)
  }

  val failingProperty = forAll { (n: Int) =>
    val square = Math.pow(n, 2)
    ("value:" + square) |: Math.sqrt(square) == n
  }
  property("Failing Sqrt logic") = failingProperty

  val workingPropery = forAll { (n: Int) =>
    (n > 0) ==> (Math.sqrt(Math.pow(n, 2)) == n)
  }
  property("Valid Sqrt logic") = workingPropery

  property("Combined Property AND") = failingProperty && workingPropery
  property("Combined Property OR") = atLeastOne(failingProperty, workingPropery)

}

