import sys

N = int(sys.stdin.readline())

words = []
for _ in range(N):
    words.append(sys.stdin.readline().strip())

words = list(set(words))
words.sort(key=lambda x: (len(x), x))

for i in range(len(words)):
    print(words[i])

