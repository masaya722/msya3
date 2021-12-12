N = int(input())
h = list(map(int, input().split()))
ans = 0
active = 0
for i in range(N):
    if active >=h[i]:
        active =h[i]
    else:
        ans +=h[i]-active
        active = h[i]
print(ans)