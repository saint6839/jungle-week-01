num = int(input())
for _ in range(num):
    ox_list = list(input())
    score = 0
    sum_score = 0
    for ox in ox_list:
        if ox == 'O':
            score += 1
            sum_score += score
        else:
            score = 0
    print(sum_score)
# num = int(input())
# str_list = []
# count = 0
# sum_count = 0
# for i in range(num):
#     str_list.append(input())
#     for j in str_list:
#         count = 0
#         sum_count = 0
#         for k in j:
#             if k == 'O':
#                 count += 1
#                 sum_count += count
#             else:
#                 count = 0
#     print(sum_count)
