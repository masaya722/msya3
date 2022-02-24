n,d = map(int,input().split())
wall = []
for i in range(n):
    l,r = map(int,input().split())
    wall.append((r,l))
wall.sort()
panch = 0
cnt = 0
for r1,l1 in wall:
    if l1>panch:
        panch=r1+d-1
        cnt +=1
print(cnt)

