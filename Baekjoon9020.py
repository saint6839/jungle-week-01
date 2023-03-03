# 소수 찾기
def is_prime(n):
    error = 0
    if n > 1:
        for i in range(2, n):
            if (n % i) == 0:
                return False
        return True
n = int(input())
for _ in range(n):
    num = int(input())
    a, b = num//2, num//2
    while a > 0:
        if (is_prime(a)) and (is_prime(b)):
            print(a, b)
            break
        else:
            a -= 1
            b += 1