import java.nio.CharBuffer
import java.nio.charset.Charset

import org.scalacheck._
import org.scalacheck.Prop._

import scala.io.Codec
import scala.collection.JavaConverters._

object basicSymmetryTest extends Properties("Basic Symmetry") {

  property("charset") = forAll { (s: String, c: Codec) =>
    new String(s.getBytes(c.charSet), c.charSet) == s
  }

  property("codec") = forAll { (s: String, c: Codec) =>
    c.decoder.decode(c.encoder.encode(CharBuffer.wrap(s))).toString == s
  }

  implicit def CodecArbitrary: Arbitrary[Codec] =
    Arbitrary(Gen.oneOf(Charset.availableCharsets.values.asScala.map(new Codec(_)).toSeq))
}

