import itertools

N = int(input())
S = set()
for i in range(N):
    S.add(tuple(map(int, input().split())))

ans = 0
for s1, s2 in itertools.combinations(S, 2):
    x1, y1 = s1
    x2, y2 = s2
    s3 = (x1 - y2 + y1, y1 + x2 - x1)
    s4 = (x2 - y2 + y1, y2 + x2 - x1)
    if s3 in S and s4 in S:
        ans = max(ans, ((s4[0] - s1[0]) ** 2 + (s4[1] - s1[1]) ** 2) / 2)


print(int(ans))
