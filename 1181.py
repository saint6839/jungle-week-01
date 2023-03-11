# n = int(input())
# array = []
# for i in range(n):
#     array.append(input())
# set_array = set(array)
# array = list(set_array)
# array.sort()
# array.sort(key = len)

# for i in array:
#     print(i)

# import sys

# n = int(sys.stdin.readline())
# lst = []

# for i in range(n):
#     lst.append(sys.stdin.readline())
# print(lst)

# set_list = set(lst)
# lst = list(set_list)
# lst.sort()
# lst.sort(key = len)

# for i in lst:
#     print(i)

n = int(input())
word_list = []

for _ in range(n):
    word_list.append(input())
word_list.sort()
set_word_list = set(word_list)
word_list.sort(key = len)
for i in word_list:
    print(i)