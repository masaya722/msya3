from collections import defaultdict


N = int(input())
cnt = defaultdict(int)
for i in range(1,N+1):
    if i<10:
        cnt[(i,i)]+=1
    else:
        first = int(str(i)[0])
        last = int(str(i)[-1])
        cnt[(first,last)]+=1
        cnt[(last,first)]

ans =0
for k,v in cnt.items():
    f,l = k
    ans+=v*cnt[(l,f)]
print(ans)
