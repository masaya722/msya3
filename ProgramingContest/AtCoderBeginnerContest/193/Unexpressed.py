from collections import defaultdict
N = int(input())
max_n = N
if N>10**5:
    max_n =10**5

dict = defaultdict(int)
for i in range(2,max_n+1):
    pow_num = 2
    while i**pow_num<=N:
        dict[i**pow_num]+=1
        pow_num+=1
can_cnt = 0
for i,j in dict.items():
    if j >0:
        can_cnt+=1
print(N-can_cnt)