total = 1
for i in range(3):
    i = int(input())
    total *= i
str_total = str(total)
for num in range(10):
    cnt = str_total.count(str(num))
    print(cnt)