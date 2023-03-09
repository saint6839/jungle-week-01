import time
start = time.time()

time.sleep(1)

n = int(input())
u_list = []
s_list = []
for _ in range(n):
    u_list.append(int(input()))
u_list.sort()
s_list = u_list
print(s_list)
# for i in s_list:
#     print(i)

print(f"{time.time()-start:.4f} sec")
