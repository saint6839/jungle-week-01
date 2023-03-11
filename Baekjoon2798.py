### 정답 코드 ###
n, m = list(map(int, input().split(' ')))
data = list(map(int, input().split(' ')))

result = 0
length = len(data)

count = 0
for i in range(0, length):
    for j in range(i+1,length):
        for k in range(j+1, length):
            sum_value = data[i] + data[j] + data[k]
            if sum_value <= m:
                result = max(result, sum_value)
print(result)

# from itertools import combinations
# import sys
# input = sys.stdin.readline
# # input 받기 (n, m, n개의 카드 수)
# n, m = map(int, input().split(' '))
# arr = list(map(int, input().split(' ')))
# # print(arr)

# # 조합으로 5C3 뽑아서 새로운 리스트에 넣기
# new_arr = list(combinations(arr, 3))
# # print(new_arr)
# # 새로운 리스트 for문 돌려서 리스트 합이 m 보다 작거나 같은 거
# # temp_list에 저장
# temp_list = []
# for i in new_arr:
#     if sum(i) <= m:
#         temp_list.append(i)
# # temp_list에서 합이 가장 큰 값을 출력하기
# # max_sum = 0
# # for i in range(len(temp_list)):
# #     # print(i)
# #     max_sum = sum(temp_list[i])
# #     for j in range(len(temp_list[i+1: len(temp_list)])):
# #         if max_sum < sum(temp_list[j]):
# #             max_sum = sum(temp_list[j])
# # print(max_sum)
# max_index = 0
# for i in range(len(temp_list)):
#     max_index = i
#     for j in range(i+1, len(temp_list)):
#         if sum(temp_list[max_index]) < sum(temp_list[j]):
#             max_index = j
#         temp_list[i], temp_list[max_index] = temp_list[max_index], temp_list[j]
# print(sum(temp_list[max_index]))