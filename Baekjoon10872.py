def recursive(n):
    result = 1
    if n > 0:
        result = n * recursive(n - 1)
    return result

print(recursive(int(input())))