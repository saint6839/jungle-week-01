import sys

results = set()
numbers = list()

n = int(sys.stdin.readline())
k = int(sys.stdin.readline())

isVisits = [False for i in range(n)]

for _ in range(n):
    numbers.append(int(sys.stdin.readline()))

def add_number(k, value):
    if k == 0:
        results.add(value)
        return

    for i in range(n):
        if not isVisits[i]:
            isVisits[i] = True
            size = len(str(numbers[i]))
            value += str(numbers[i])
            add_number(k - 1, value)
            isVisits[i] = False
            value = value[:-size]

add_number(k, '')
print(len(results))
