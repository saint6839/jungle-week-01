# # 인풋받기 #
# u_list = list(map(int, input().split()))
# # u_list = [int(x) for x in input().split()]

# # 2) 쪼개진 부분 리스트의 길이가 1이 될때까지 분할 #
# def merge_sort(u_list):
#     # 크기가 1이하면 반환
#     if len(u_list) <= 1:
#         return u_list

#     # 리스트를 2분할
#     mid = len(u_list)//2
#     left = u_list[:mid]
#     right = u_list[mid:]

#     # 리스트를 각각 merge sort 진행
#     left_ = merge_sort(left)
#     right_ = merge_sort(right)
#     return merge(left_, right_)

# # 3) 길이가 1로 쪼개진 리스트를 순서대로 병합하여 정렬 리스트에 저장
# def merge(left, right):
#     l, r = 0, 0
#     s_list = []

#     while l < len(left) and r < len(right):
#         if left[l] < right[r]:
#             s_list.append(left[l])
#             l += 1
#         else:
#             s_list.append(right[r])
#             r += 1
    
#     while l < len(left):
#         s_list.append(left[l])
#         l += 1
    
#     while r < len(right):
#         s_list.append(right[r])
#         r += 1
#     return s_list

# # 4) 정렬결과 확인
# print(merge_sort(u_list))

import sys
input = sys.stdin.readline

# 1) 인풋받기
n = int(input())
u_list = []

for _ in range(n):
	u_list.append(int(input()))

# 2) 쪼개진 부분 리스트의 길이가 1이 될때까지 분할
def merge_sort(u_list):
    # 크기가 1이하면 반환
    if len(u_list) <= 1:
        return u_list

    # 리스트를 2분할
    mid = len(u_list)//2
    left = u_list[:mid]
    right = u_list[mid:]

    # 리스트를 각각 merge sort 진행
    left_ = merge_sort(left)
    right_ = merge_sort(right)
    return merge(left_, right_)

# 3) 길이가 1로 쪼개진 리스트를 순서대로 병합하여 정렬 리스트에 저장
def merge(left, right):
    l, r = 0, 0
    s_list = []

    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            s_list.append(left[l])
            l += 1
        else:
            s_list.append(right[r])
            r += 1
    
    while l < len(left):
        s_list.append(left[l])
        l += 1
    
    while r < len(right):
        s_list.append(right[r])
        r += 1
    return s_list

# 4) 정렬결과 확인
for i in merge_sort(u_list):
	print(i)