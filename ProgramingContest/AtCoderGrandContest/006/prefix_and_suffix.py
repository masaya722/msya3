N = int(input())
s = input()
t = input()

ans = 0
for i in range(N):
    if s[i:N] == t[0:N-i]:
        ans = N+i
if s == t:
    ans = N
elif ans == 0:
    ans = 2*N
print(ans)
