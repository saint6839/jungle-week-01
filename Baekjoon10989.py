import sys

n = int(sys.stdin.readline())
array = [0] * 10001

for i in range(n):
    data = int(sys.stdin.readline())
    array[data] += 1

for i in range(10001):
    if array[i] != 0:
        for j in range(array[i]):
            print(i)

### 계수정렬 ###
import sys
input = sys.stdin.readline
num = int(input())
arr = [0]*10000

for i in range(num):
    a = int(input())
    arr[a-1] += 1

for i in range(10000):
    if arr[i] != 0:
        for j in range(arr[i]):
            print(i + 1)