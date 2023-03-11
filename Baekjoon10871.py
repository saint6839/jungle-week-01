num, X = map(int, input().split())
result_list = []

num_list = list(map(int, input().split()))
for i in range(num):
    if (num_list[i] < X):
        print(num_list[i], end=" ")

