from collections import defaultdict
N,C = map(int,input().split())

dict = defaultdict(int)
for i in range(N):
    a,b,c = map(int,input().split())
    dict[a]+=c
    dict[b+1]-=c

sorted_dict = sorted(dict.items())
s = 0
term = []
cost = []
for i,j in sorted_dict:
    s+=j
    term.append(i)
    cost.append(s)
ans = 0
for i in range(len(term)-1):
    if cost[i]>C:
        ans+=C*(term[i+1]-term[i])
    else:
        ans+=cost[i]*(term[i+1]-term[i])
print(ans)
