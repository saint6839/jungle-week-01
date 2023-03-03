#윤년 4의 배수 and not 100배수 or 400의 배수
Y_year = int(input())
result = Y_year % 4
result2 = Y_year % 100
result3 = Y_year % 400
if result == 0 and result2 != 0 or result3 == 0:
    print(1)
else:
    print(0)

