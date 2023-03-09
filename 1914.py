n = int(input())

def hanoi(n, _from, _to, _other):
    if n == 1:
        print(_from, _to)
        return
    hanoi(n-1, _from, _other, _to)
    print(_from, _to)
    hanoi(n-1, _other, _to, _from)
print(2**n - 1)
if (n <= 20):
   hanoi(n, 1, 3, 2)