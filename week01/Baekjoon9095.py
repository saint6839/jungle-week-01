import sys

T = int(sys.stdin.readline())


target = 0
count = 0

def dfs(sum):
    global target
    global count

    if sum > target:
        return

    if sum == target:
        count += 1
        return

    for i in range(1,4):
        sum += i
        dfs(sum)
        sum -= i

for _ in range(T):
    count = 0
    target = int(sys.stdin.readline())
    dfs(0)
    print(count)

