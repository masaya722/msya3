N,M =map(int,input().split())
INF = 10**6
disk = [INF]*(N+1)
out = [0]
for i in range(M):
    cd = int(input())
    k = out.pop()
    if cd ==k:
        out.append(k)
        continue
    if cd !=0 and disk[cd] ==INF:
        disk[cd] = k
    else:
        disk[disk.index(cd)] = k
    out.append(cd)

for i in range(1,N+1):
    if disk[i] ==INF:
        print(i)
    else:
        print(disk[i])


    


