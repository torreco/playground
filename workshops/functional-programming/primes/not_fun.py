
def is_prime(number):
    divisible = False

    i = 2
    while i < number:
        if number % i == 0:
            divisible = True
            break
        i += 1

    return number > 1 and not divisible


if __name__ == "__main__":
    def primes():
        return list(i for i in range(1, 10000) if is_prime(i))

    primes()
