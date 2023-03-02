N = int(input())


results = list()
for i in range(N):
    value = list(input())

    sum = 0
    score = 0
    for v in value:
        if v == 'O':
            score += 1
            sum += score
        if v == 'X':
            score = 0
    results.append(sum)

for result in results:
    print(result)