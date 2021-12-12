from typing import DefaultDict


from collections import defaultdict
n,m = map(int,input().split())
name = input()
kit = input()
name_dict= defaultdict(int)
kit_dict = defaultdict(int)
for k in kit:
    kit_dict[k]+=1
for n in name:
    name_dict[n]+=1
for n in name:
    if kit_dict[n]==0:
        print(-1)
        exit()
ans = 0
while not all([x== 0 for x in name_dict.values()]):
    for i,j in name_dict.items():
        if kit_dict[i]<=j:
            name_dict[i]-=kit_dict[i]
        else:
            name_dict[i]=0
    ans+=1
print(ans)
