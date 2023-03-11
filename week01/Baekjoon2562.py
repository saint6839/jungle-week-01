max_index = 0
max = 0
for i in range(1, 10):
    number = int(input())

    if max < number:
        max = number
        max_index = i

print(max)
print(max_index)

