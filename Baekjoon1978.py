# 소수 찾기
n = int(input())
numbers = map(int, input().split())
sosu = 0
for num in numbers:
    error = 0
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                error += 1
        if error == 0:
            sosu += 1
print(sosu)

# 김정희님 코드 #
# import sys
# import math
# n = int(sys.stdin.readline().rstrip())
# ls = [int(x) for x in sys.stdin.readline().split()]
# print(ls)
# maxi = max(ls)
# print(maxi)
# ch = [0] * (maxi+1)
# ch[0], ch[1] = 1, 1
# for i in range(2, math.ceil(math.sqrt(maxi))): #여기서 int(math.sart(maxi)+1) 하니까 문제 해결 됨.
#     if ch[i] == 0:
#         for j in range(i*i, maxi+1, i):
#             ch[j] = 1
# cnt = 0
# for x in ls:
#     if ch[x] == 0:
#         cnt += 1
# print(cnt)