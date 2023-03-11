x, y = map(int, input().split())
x_list = [0, x] # 가로 각각 길이
y_list = [0, y] # 세로 각각 길이
for _ in range(int(input())):
    xy, length = map(int, input().split())
    if xy == 0:
        y_list.append(length)
    else:
        x_list.append(length)

x_list.sort()
y_list.sort()

max_square = 0
for i in range(1, len(x_list)):
    for j in range(1, len(y_list)):
        width = x_list[i] - x_list[i-1]
        height = y_list[j] - y_list[j-1]
        max_square = max(max_square, width * height) # 가장 큰 범위
print(max_square)
    