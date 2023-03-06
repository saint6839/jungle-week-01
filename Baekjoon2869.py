# A, B, V = map(int, input().split())
# day, ret = 0, 0
# for _ in range(V-A//A-B+1):
#     if (A-B) * day < (V-A):
#         ret += (A-B)
#         day += 1
#     else:
#         print(day + 1)
#         break

import math
a, b, v = map(int, input().split())
day = 0
day = math.ceil((v-a)/(a-b)+1)

