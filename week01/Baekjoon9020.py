import math
import sys

T = int(sys.stdin.readline())

prime_numbers = list()


def isPrime(i):
    for j in range(2, int(math.sqrt(i)) + 1):
        if i % j == 0:
            return False
    return True


for i in range(2, 10000):
    if i == 2:
        prime_numbers.append(i)
        continue

    if isPrime(i):
        prime_numbers.append(i)

for _ in range(T):
    number = int(sys.stdin.readline())
    min_diff = 10000
    a = 0
    b = 0

    for prime_number in prime_numbers:
        diff = number - prime_number
        if prime_number > diff:
            break
        if isPrime(diff):
            if min_diff > diff:
                min_diff = diff

                a = prime_number
                b = diff
    print(a, b)
