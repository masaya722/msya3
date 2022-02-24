N = int(input())
X = []
for _ in range(N):
    X.append([])

for _ in range(N):
    a, b = list(map(int, input().split()))
    X[a - 1].append(b)

cnt = [0] * 101

ans = 0
for i in range(N):
    for d in X[i]:
        cnt[d] += 1

    for i in range(100, 0, -1):
        if cnt[i] > 0:
            ans += i
            cnt[i] -=1
            break

    print(ans)