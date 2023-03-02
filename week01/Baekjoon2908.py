A, B = input().split()

newA = int(A[::-1])
newB = int(B[::-1])
print(max(newA, newB))