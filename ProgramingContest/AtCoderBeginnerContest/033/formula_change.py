from collections import defaultdict
S = input()
dict = defaultdict(int)
cnt = 0
for s in S:
    if dict[cnt] ==0:
        dict[cnt] =0
    if s =='0':
        dict[cnt]+=1
    if s =="+":
        cnt+=1
ans = 0
for i,j in dict.items():
    if j ==0:
        ans+=1
print(ans)

