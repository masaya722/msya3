from collections import defaultdict
dict = defaultdict(int)
N,C = map(int,input().split())
for _ in range(N):
    a,b,c = map(int,input().split())
    dict[a]+=c
    dict[b+1]-=c
sorted_dict = sorted(dict.items())
total = 0
ans = 0
for i in range(len(sorted_dict)-1):
    total+=sorted_dict[i][1]
    ans +=min(C,total)*(sorted_dict[i+1][0]-sorted_dict[i][0])
print(ans)
