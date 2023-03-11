# n = int(input())
# temp = 0
# n_list = []
# for _ in range(n):
#     n_list.append(int(input()))
# for _ in range(n-1):
#     for i in range(n):
#         print(i)
#         if (i != (n-1)) and (n_list[i] > n_list[i+1]):
#             temp = n_list[i]
#             n_list[i] = n_list[i + 1]
#             n_list[i + 1] = temp
# for i in range(len(n_list)):
#     print(n_list[i])


### 정답 코드 ###
n = int(input())
array = list()

for _ in range(n):
    array.append(int(input()))

for i in range(n):
    min_index = i
    for j in range(i+1, n):
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i]

for i in range(len(array)):
    print(array[i])
