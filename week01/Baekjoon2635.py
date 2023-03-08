import sys

N = int(sys.stdin.readline())


max_len = -sys.maxsize
max_results = []
for i in range(N//2,N):
    results = []
    cN = N
    results.append(cN)
    if i==0:
        results.append(1)
    else :
        results.append(i)

    index = 1
    while True:
        diff = results[index-1] - results[index]
        if diff < 0:
            if max_len < len(results):
                max_len = len(results)
                max_results = results
            break
        results.append(diff)
        index += 1

print(max_len)
print(*max_results, sep=' ')


