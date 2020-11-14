N = 10


def is_prime(n: int) -> bool:
    return all(n % i for i in range(2, n))


if N < 0 or N % 1 != 0:
    raise ValueError("N should be natural number.")

primes = []

i = 2

while len(primes) != N:
    if is_prime(i):
        primes.append(i)

    i += 1

print(primes)
