R,G,B,N = map(int,input().split())
count =0
for r in range(N+1):
    if r *R>N:
        break
    for g in range(N+1):
        if N-(r*R+g*G)<0:
            break
        if N-(r*R+g*G) == 0:
            count +=1
            break
        if (N-(r*R+g*G))%B == 0:
            count +=1
print(count)
