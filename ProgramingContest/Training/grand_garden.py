N = int(input())
h = list(map(int,input().split()))
active = 0
ans = 0
for i in h:
    if active<i:
        ans +=i-active
        active = i
    else:
        active = i
print(ans)
