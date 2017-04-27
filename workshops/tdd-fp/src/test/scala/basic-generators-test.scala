import org.scalacheck.Prop._
import org.scalacheck.{Arbitrary, Properties, Gen}

object RectangleGenerator {
  val rectangleGen: Gen[Rectangle] = for {
    height <- Gen.choose(0, 9999)
    width <- Gen.choose(height * 2, 99999)
  } yield (Rectangle (width, height))

 implicit val arbRectangle: Arbitrary[Rectangle] = Arbitrary(rectangleGen)
}

object basicGeneratorsTest extends Properties("Basic Generators") {
  import RectangleGenerator._

  property("Failing area logic") = forAll { (r: Rectangle) =>
    collect((r.height, r.width)) {
      r.perimeter == (r.width + r.height)
    }
  }

  property("Valid area logic") = forAll { (r: Rectangle) =>
    classify(r.height < 4999, "small", "large") {
      r.area == (r.width * r.height)
    }
  }

  property("Test biggerThan") = forAll { (r1:Rectangle, r2:Rectangle) =>
    (r1 biggerThan r2) == (r1.area > r2.area)
  }

}

