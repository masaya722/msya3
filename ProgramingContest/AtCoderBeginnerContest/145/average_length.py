import math


N = int(input())

town_list = [tuple(map(int, input().split())) for _ in range(N)]

distance_list = {}
for i in range(N):
    x1, y1 = town_list[i]
    for j in range(N):
        if i == j:
            continue
        x2, y2 = town_list[j]

        distance = math.sqrt(pow(x1 - x2,2) + pow(y1 - y2,2))
        distance_list[(i, j)] = distance

print(sum(distance_list.values()) / N)
