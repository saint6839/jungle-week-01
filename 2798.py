# from itertools import combinations
# import sys
# input = sys.stdin.readline

# n, m = map(int, input().split())
# array = []
# new_array =[]
# max_i = 0

# array = list(map(int, input().split()))
# combi = combinations(array, 3)

# for i in combi:
#     if sum(i) <= m:
#         new_array.append(i)
# # print(new_array)
# for i in range(len(new_array)):
#     max_i = sum(new_array[i])
#     # print(max_i)
#     for j in range(i+1, len(new_array)):
#         if max_i < sum(new_array[j]):
#             max_i = sum(new_array[j])
#     print(max_i)
#     break

n, m = list(map(int, input().split()))
data = list(map(int, input().split()))

length = len(data)
result = 0

for i in range(length):
    for j in range(i+1, length):
        for k in range(j+1, length):
            sum_value = data[i] + data[j] + data[k]
            if sum_value <= m:
                result = max(result, sum_value)
print(result)

from itertools import combinations

n, m = map(int, input().split())
cards = list(map(int, input().split()))
card_list = []
combi = combinations(cards, 3)
for card in combi:
    if sum(card) <= m:
        card_list.append(sum(card))
print(max(card_list))
