N = int(input())
ans = []
for i in range(N):
    s = list(input())
    a = "".join(s)
    s.reverse()
    b = "".join(s)
    ans.append((b,a))

ans.sort()

for a,b in ans:
    print(b)