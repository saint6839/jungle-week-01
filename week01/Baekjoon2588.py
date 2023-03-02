first = int(input())
second = list(input())

count = 1
result = 0
for i in range(len(second)-1, -1, -1):
    mul = first * int(second[i])
    temp = mul * count
    print(mul)
    result += temp

    count *= 10

print(result)

