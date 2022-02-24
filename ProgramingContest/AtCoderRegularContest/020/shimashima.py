from collections import defaultdict
n,c = map(int,input().split())
first = defaultdict(int)
second = defaultdict(int)

for i in range(n):
    if i%2 ==0:
        first[int(input())]+=1
    else:
        second[int(input())]+=1

first_rank =[]
second_rank = []
for key,val in first.items():
    first_rank.append((val,key))
for key,val in second.items():
    second_rank.append((val,key))    

first_rank.sort(reverse=True)
second_rank.sort(reverse=True)

f_val,f_key = first_rank[0]
s_val,s_key = second_rank[0]
f_use = 0
s_use = 0
if f_key ==s_key:
    if f_val>s_val:
        f_use = f_val
        if len(second_rank)>1:
            s_val,s_key = second_rank[1]
            s_use = s_val
        else:
            s_use = 0
    else:
        s_use = s_val
        if len(first_rank)>1:
            f_val,f_key = first_rank[1]
            f_use = f_val
        else:
            f_use = 0
else:
    f_use = f_val
    s_use = s_val
if n%2 ==0:
    print(((n//2-f_use)+(n//2-s_use))*c)
else:
    print(((n//2-f_use+1)+(n//2-s_use))*c)