MOD = 998244353
n = int(input())
a = list(map(int, input().split()))
a.sort()
t = 0
ans = a[0] * a[0]
for i in range(1, n):
    t += a[i - 1]
    ans += a[i] * t + a[i] * a[i]
    t = t * 2%MOD
print(ans%MOD)