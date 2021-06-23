from collections import deque

k = int(input())
Q = deque([1, 2, 3, 4, 5, 6, 7, 8, 9])
count = 0
while True:
    a = Q.popleft()
    count += 1
    if count == k:
        print(a)
        break
    if a % 10 != 0:
        Q.append(a * 10 + a % 10 - 1)
    Q.append(a * 10 + a % 10)
    if a % 10 != 9:
        Q.append(a * 10 + a % 10 + 1)
