L, X, Y, S, D = map(int, input().split())
dist = D-S
rev = Y-X
ans =0
if dist==0:
    print(ans)
    exit()
elif dist<0:
    if rev>0:
        ans = min(abs(dist)/rev,(L+dist)/(X+Y))
    else:
        ans = (L+dist)/(X+Y)
else:
    if rev>0:
        ans = min(dist/(X+Y),(L-dist)/rev)
    else:
        ans = dist/(X+Y)
print(ans)

