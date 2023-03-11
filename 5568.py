# from itertools import permutations

# n = int(input())
# k = int(input())
# array = []

# for _ in range(n):
#     array.append(input())

# result = set()

# for i in permutations(array, k):
#     result.add(''.join(i))
# print(len(result))

# perm = permutations(array, k)
# set_array = set(perm) 
# array = list(set_array)
# array.sort()
# print(len(array))
from itertools import permutations

n = int(input())
k = int(input())
arr = []

for _ in range(n):
    arr.append(input())
perm = permutations(arr, k)
# set_perm = set(perm)
# perm = list(set_perm)
# print(len(perm))
result = set()

for i in perm:
    result.add(''.join(i))
print(len(result))