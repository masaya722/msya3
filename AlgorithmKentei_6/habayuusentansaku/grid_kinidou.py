n, x, y = list(map(int, input().split()))
visit = set([])
visit.add((0, 0))
for _ in range(n):
    visit.add(tuple(map(int, input().split())))

from collections import deque

q = deque()
q.append([(0, 0), 0])
while q:
    (X, Y), level = q.popleft()

    # 斜め移動を優先して探索
    for dx, dy in [(1, 1), (-1, 1), (0, 1), (1, 0), (-1, 0), (0, -1)]:
        xx = X + dx
        yy = Y + dy
        if (xx, yy) == (x, y):
            print(level + 1)
            exit()
            break
        # 範囲チェック
        if -201 <= xx <= 201 and -201 <= yy <= 201:
            pass
        else:
            continue

        if (xx, yy) not in visit:
            q.append([(xx, yy), level + 1])
            visit.add((xx, yy))

print(-1)
