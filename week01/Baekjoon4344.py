C = int(input())

for _ in range(C):
    inputs = input().split()
    sum = 0
    for i in range(1, len(inputs)):
        sum += int(inputs[i])

    avg = sum / int(inputs[0])

    count = 0
    for i in range(1, len(inputs)):
        if avg < int(inputs[i]):
            count += 1

    print("{:.3f}".format(count / int(inputs[0]) * 100), end='%\n')
