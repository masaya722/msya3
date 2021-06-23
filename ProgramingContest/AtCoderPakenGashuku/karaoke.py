N, M = list(map(int, input().split()))

songList = []
for _ in range(N):
    songList.append(list(map(int, input().split())))

ans = 0


def sum_max(firstsong, secondsong):
    summax = 0
    for i in range(N):
        summax += max(firstsong[i], secondsong[i])
    return summax


for i in range(M - 1):
    for j in range(i + 1, M):
        firstsong = [x[i] for x in songList]
        secondsong = [x[j] for x in songList]
        ans = max(ans, sum_max(firstsong, secondsong))

print(ans)
