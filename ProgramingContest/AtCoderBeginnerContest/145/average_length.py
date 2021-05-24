import math


N = int(input())

townList = [tuple(map(int, input().split())) for _ in range(N)]

distanceList = {}
for i in range(N):
    x1, y1 = townList[i]
    for j in range(N):
        if i == j:
            continue
        x2, y2 = townList[j]

        distance = math.sqrt(pow(x1 - x2,2) + pow(y1 - y2,2))
        distanceList[(i, j)] = distance

print(sum(distanceList.values()) / N)
