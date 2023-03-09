from itertools import permutations
n = int(input())
arr = list(map(int, input().split()))
new_arr = []
total = 0

perm = permutations(arr)
for i in perm:
    total = 0
    for j in range(n-1):
        total += abs(i[j] - i[j+1])
    new_arr.append(total)
    # print(new_arr)
print(max(new_arr))
