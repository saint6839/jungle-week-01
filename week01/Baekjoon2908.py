A, B = input().split()

a_list = list(A)
b_list = list(B)
temp = ''
for a in reversed(A):
    temp += a
newA = int(temp)

temp = ''
for b in reversed(B):
    temp += b
newB = int(temp)

print(max(newA, newB))