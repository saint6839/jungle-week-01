import math
a, b, v = map(int, input().split())
day = 0
day = math.ceil((v-a)/(a-b)+1)

