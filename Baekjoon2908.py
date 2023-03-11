# A, B = input().split()
# reverse_A = int(A[::-1])
# reverse_B = int(B[::-1])
# if reverse_A > reverse_B:
#     print(reverse_A)
# else:
#     print(reverse_B)

a, b = map(int, input().split())
reverse_a = int(str(a)[::-1])
reverse_b = int(str(b)[::-1])
if reverse_a > reverse_b:
    print(reverse_a)
else:
    print(reverse_b)