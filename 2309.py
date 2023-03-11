# from itertools import combinations

# tall_lst = []
# for _ in range(9):
#     tall_lst.append(int(input()))
# tall_sum = sum(tall_lst)
# combi = combinations(tall_lst, 7)
# # print(list(combi))
# for i in combi:
#     if sum(i) == 100:
#         # print(list(i).sort())
#         i = list(i)
#         i.sort()
#         for j in i:
#             print(j)
#         break

# for i in combi:
#     if (tall_sum - sum(i)) == 100:
        
# if (tall_sum - )
from itertools import combinations

n_men = []
for _ in range(9):
    n_men.append(int(input()))
combi = combinations(n_men, 2)
n_sum = sum(n_men)

for i in combi:
    if n_sum - sum(i) == 100:
        n_men.remove(i[0])
        n_men.remove(i[1])
        break
n_men.sort()
for i in n_men:
    print(i)

