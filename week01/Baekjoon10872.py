def recursive(result, number):
    if number == 0:
        return result
    result *= number
    return recursive(result, number - 1)


print(recursive(1, int(input())))
