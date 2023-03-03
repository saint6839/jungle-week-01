import sys

N = int(sys.stdin.readline())
result = 0


for n in range(1, N+1):
    if n < 10:
        result += 1
    else :
        temp = str(n)

        diff = int(temp[1]) - int(temp[0])
        isDegreeDiff = False
        for i in range(1, len(temp)-1):
            next_diff = int(temp[i+1]) - int(temp[i])
            if diff != next_diff:
                isDegreeDiff = False
                break
            isDegreeDiff = True

        if isDegreeDiff or len(temp) == 2:
            result += 1

print(result)

