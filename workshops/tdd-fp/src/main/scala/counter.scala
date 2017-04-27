
class Counter {
  private var n = 0

  def inc = n += 1
  def dec = if(n > 3) n -= 2 else n -= 1
  def get = n
  def reset = n = 0
}

