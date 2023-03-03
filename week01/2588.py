"""
곱셈
"""
import sys

a_str = sys.stdin.readline().rstrip()
n = len(a_str)
a = int(a_str)
b = int(sys.stdin.readline())

tot = 0
for i in range(n):
    tmp = b%10
    b = b//10 
    print(a * tmp)
    tot += (a * tmp) * (10 ** i)
    
print(tot) 



