num = int(input())
for _ in range(num):
    s_list=[]
    s_sum = 0
    count = 0
    s_list = list(map(int, input().split()))
    s_sum = sum(s_list[1:])
    s_avg = s_sum/s_list[0]
    for score in s_list[1:]:
        if score > s_avg:
            count += 1
    rate = count/s_list[0] * 100
    print(f'{rate:.3f}%')
