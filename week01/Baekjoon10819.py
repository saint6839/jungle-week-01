import sys

N = int(sys.stdin.readline())

numbers = list(map(int, sys.stdin.readline().split()))

isVisits = [False for i in range(len(numbers))]

max = 0
temps = []
def dfs(count, index):
    global max
    if count == len(numbers):
        sum = 0
        for i in range(0, len(temps)-1):
            sum += abs(temps[i] - temps[i+1])
        if max < sum:
            max = sum
        return

    for i in range(len(numbers)):
        if not isVisits[i]:
            isVisits[i] = True
            temps.append(numbers[i])
            dfs(count + 1, i + 1)
            temps.pop()
            isVisits[i] = False

dfs(0, 0)
print(max)