# # 순열
# input_list = [1,2,3,4,5]
# used = [0] * len(input_list)

# print(used)

# def perm(arr, n):
#     if n == len(input_list):
#         print(arr)
#         return
#     for i in range(len(input_list)):
#         if not used[i]:
#             used[i] = 1
#             arr.append(input_list[i])
#             perm(arr, n+1)
#             arr.pop()
#             used[i] = 0
# perm([], 0)

# # 조합
# nums = [1,2,3,4,5]
# answer_list = []
# # anc
# def combi(n, ans):
#     if n == len(nums):
#         temp = [i for i in ans]
#         answer_list.append(temp)
#         return
#     ans.append(nums[n])
#     combi(n + 1, ans)
#     ans.pop()
#     combi(n + 1, ans)

# combi(0, [])
# print(answer_list)

# # nCr
# ums = [1,2,3,4,5]
# answer_list = []
# def nCr(n, ans, r):
#     if n == len(nums):
#         if len(ans) == r:
#             temp = [i for i in ans]
#             answer_list.append(temp)
#         return
#     ans.append(nums[n])
#     nCr(n + 1, ans, r)
#     ans.pop()
#     nCr(n + 1, ans, r)
# nCr(0, [], 3)
# print(answer_list)

from itertools import permutations
import sys
input = sys.stdin.readline

n, k = map(int, input())
cards = [input().rstrip() for _ in range(n)]
res = set()
for per in permutations(cards, k):
    res.add(''.join(per))

print(len(res))

# 순열
import itertools

arr = ['A', 'B', 'C']
nPr = itertools.permutataions(arr, 2)
print(list(nPr))

# 조합
import itertools

arr = ['A', 'B', 'C']
nCr = itertools.combinations(arr, 2)
print(list(nCr))

# 3번 풀이
from itertools import permutataions
n, k = int(input()), int(input())
cards = [input().rstrip() for _ in range(n)]
res = set()
for per in permutataions(cards, k):
    res.add(''.join(per))




# from itertools import permutations

# n = int(input())
# k = int(input())
# array = []

# for _ in range(n):
#     array.append(int(input()))

# perm = permutations(array, k)
# set_array = set(array)
# array = list(array)
# print(len(array))