import sys

N = int(sys.stdin.readline())

numbers = list(map(int, sys.stdin.readline().split()))
operators = list(map(int, sys.stdin.readline().split()))

min = sys.maxsize
max = -sys.maxsize

def dfs(value, index):
    global min
    global max

    if not any(operators):
        if min > value:
            min = value
        if max < value:
            max = value
        return

    for i in range(4):
        if operators[i]:
            operators[i] -= 1
            if i == 0:
                dfs(value + numbers[index], index + 1)
            if i == 1:
                dfs(value - numbers[index], index + 1)
            if i == 2:
                dfs(value * numbers[index], index + 1)
            if i == 3:
                dfs(int(value / numbers[index]), index + 1)
            operators[i] += 1

dfs(numbers[0], 1)
print(max)
print(min)
