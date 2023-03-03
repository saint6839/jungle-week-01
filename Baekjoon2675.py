num = int(input())
for _ in range(num):
  ret = ''
  a = list(input().split())
  for i in a[1]:
      ret += i * int(a[0])
  print(ret)