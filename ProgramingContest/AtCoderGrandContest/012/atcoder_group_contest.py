N = int(input())
a = list(map(int,input().split()))
a.sort(reverse=True)
edited_a = a[:2*N]
ans = 0
for i in range(len(edited_a)):
    if i%2 ==1:
        ans+=edited_a[i]
print(ans)