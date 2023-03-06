import sys
from itertools import combinations
lst = []
for _ in range(9):
    lst.append(sys.stdin.readline().strip())
    # lst = int(input())
combi = list(combinations(lst, 7))
for i in combi:
    i_list = list(map(int, i))
    print(i_list)
    if sum(i_list) == 100:
        for j in sorted(i_list):
            print(j)
        break

# for i in range(len(array)):
#     for j in range(i + 1, len(array)):
#         if sum_ - array[i] - array[j] == 100:
#             for k in range(len(array)):
#                 if k == i or k == j:
#                     pass
#                 else:
#                     print(array[k])
#             exit()

### 정답코드2 -combinations 라이브러리 이용 ###
import itertools

array = [int(input()) for _ in range(0)]

for i in itertools.combinations(array, 7):
    if sum(i) == 100:
        for j in sorted(i):
            print(j)
        break


### 정답코드3 - 재귀이용 ###
short_men = [int(input()) for _ in range(9)]
seven_short_temp = []

def dfs(depth, start):
    if depth == 7:
        if sum(seven_short_temp) == 100:
            for j in sorted(seven_short_temp):
                print(j)
            exit()
        else:
            return
        
    for i in range(start, len(short_men)):
        seven_short_temp.append(short_men[i])
        dfs(depth + 1, i + 1)
        seven_short_temp.pop()

dfs(0, 0)