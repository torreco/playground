
def is_prime(number):
    return number > 1 \
        and none_match(lambda i: number % i == 0, range(2, number))


def none_match(predicate, iterator):
    return not any(filter(predicate, iterator))


if __name__ == "__main__":
    def primes():
        return list(i for i in range(1, 10000) if is_prime(i))

    primes()
