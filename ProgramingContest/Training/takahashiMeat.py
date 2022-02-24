n = int(input())
t = []
for _ in range(n):
    t.append(int(input()))

ans = 10 ** 18


def dfs(i, t1, t2):
    global ans
    if i == n:
        ans = min(ans, max(t1, t2))
        return
    dfs(i + 1, t1 + t[i], t2)
    dfs(i + 1, t1, t2 + t[i])


dfs(0, 0, 0)
print(ans)
