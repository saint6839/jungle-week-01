from itertools import permutations

n = int(input())
a = list(map(int, input().split()))
anc = []

perm = permutations(a)
total = 0

for i in perm:
    total = 0
    for j in range(len(i)-1):
        total += abs(i[j] - i[j+1])
        # for k in range(j+1, len(i)-1):
        #     total += abs(i[j] - i[k])
    anc.append(total)
    # total = 0
# print(anc)
print(max(anc))