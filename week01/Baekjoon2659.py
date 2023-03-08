import sys

a, b, c, d = map(int, sys.stdin.readline().split())

num1 = a * 1000 + b * 100 + c * 10 + d
num2 = b * 1000 + c * 100 + d * 10 + a
num3 = c * 1000 + d * 100 + a * 10 + b
num4 = d * 1000 + a * 100 + b * 10 + c

min_num = min(num1, num2, num3, num4)

result = 0

count = 0
run = True

isVisits = [False for i in range(10000)]

while run:
    for i in range(1, 10):
        for j in range(1, 10):
            for k in range(1, 10):
                for l in range(1, 10):
                    first = i * 1000 + j * 100 + k * 10 + l
                    second = j * 1000 + k * 100 + l * 10 + i
                    third = k * 1000 + l * 100 + i * 10 + j
                    fourth = l * 1000 + i * 100 + j * 10 + k

                    result = min(first, second, third, fourth)
                    if min_num > result and not isVisits[result]:
                        # print(result)
                        isVisits[result] = True
                        count += 1
                    else:
                        run = False

print(count + 1)