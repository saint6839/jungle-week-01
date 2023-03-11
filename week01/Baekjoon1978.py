import math

N = int(input())

numbers = list(map(int, input().split()))

result = 0
for number in numbers:
    if number == 1:
        continue

    if number == 2:
        result += 1
        continue

    isPrime = True
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            isPrime = False
            break
    if isPrime:
        result+=1

print(result)