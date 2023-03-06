### 백트래킹 이용한 풀이 ###
import sys

N = int(input())
travel_cost = [list(map(int, input().split())) for _ in range(N)]
min_value = sys.maxsize

def dfs_backtracking(start, next, value, visited):
    global min_value

    if len(visited) == N:
        if travel_cost[next][start] != 0:
            min_value = min(min_value, value + travel_cost[next][start])
        return
    for i in range(N):
        if travel_cost[next][i] != 0 and i not in visited and value < min_value:
            visited.append(i)
            dfs_backtracking(start, i, value + travel_cost[next][i], visited)
            visited.pop()

for i in range(N):
    dfs_backtracking(i, i, 0, [i])

print(min_value)

### dfs 이용한 풀이 ####
import sys

def dfs(start, next, value, visited):
    global min_value

    if len(visited) == N:
        if travel[next][start] != 0:
            min_value = min(min_value, value + travel[next][start])
        return
    
    for i in range(N):
        if travel[next][i] != 0 and i != start and i not in visited:
            visited.append(i)
            dfs(start, i, value + travel[next][i], visited)
            visited.pop()

if __name__ == "__main__":
    N = int(input())
    travel = [list(map(int, input().split())) for _ in range(N)]

    min_value = sys.maxsize

    for i in range(N):
        dfs(i, i, 0, [i])
    
    print(min_value)

### 순열 직접 구현 ###
def permutation(arr, r):
    result = []

    def permute(p, index):
        if len(p) == r:
            result.append(p)
            return
        
        for idx, data in enumerate(arr):
            if idx not in index:
                permute(p + [data], index + [idx])
    permute([], [])

    return result

for r in permutation(['A', 'B', 'C', 'D'], 2):
    print(r)


### 순열 라이브러리 이용 ####
from itertools import permutations

data = 'ABCD'
result = permutations(data, 2)

for r in result:
    print(r)


### 재귀적으로 조합 구현 ###
def combination(arr, r):
    result = []

    def combinate(c, index):
        if len(c) == r:
            result.append(c)
            return
        
        for idx, data in enumerate(arr):
            if idx > index:
                combinate(c + [data], idx)
    combinate([], -1)
    return result

for r in combination(['A', 'B', 'C', 'D'], 2):
    print(r)


### 조합 라이브러리로 구현 ###
from itertools import combinations
data = "ABCD"
result = combinations(data, 2)

for r in result:
    print(r)


### 병합정렬 ####
def merge_sort(arr):
    if len(arr) < 2:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    merged_arr = []
    l = r = 0
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            merged_arr.append(left[l])
            l += 1
        else:
            merged_arr.append(right[r])
            r += 1
    merged_arr += left[l:]
    merged_arr += right[r:]
    return merged_arr

import sys

def dfs(start, next, value, visited):
    global min_value

    if len(visited) == N:
        if travel[next][start] != 0:
            min_value = min(min_value, value + travel[next][start])
        return
    
    for i in range(N):
        if travel[next][i] != 0 and i != start and i not in visited:
            visited.append(i)
            dfs(start, i, value + travel[next][i], visited)
            visited.pop()

if __name__ == "__main__":

    N = int(input())
    travel = [list(map(int, input().split())) for _ in range(N)]

    min_value = sys.maxsize

    for i in range(N):
        dfs(i, i, 0, [i])
    
    print(min_value)

import sys

def dfs(start, cur, cost):
    global matrix, visit, minCost

    if start == cur and visit.count(False) == 0:
        minCost = min(minCost, cost)

    for i in range(n):
        if not matrix[cur][i] == 0 and not visit[i]:
            visit[i] = True
            dfs(start, i, cost + matrix[cur][i])
            visit[i] = False

n = int(input())

matrix = []
for _ in range(n):
    matrix.append([int(x) for x in sys.stdin.readline().split()])

minCost = float('inf')
float = [False for _ in range(n)]
dfs(0,0,0)

print(minCost)