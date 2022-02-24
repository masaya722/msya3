from collections import deque

k = int(input())
Q = deque([1, 2, 3, 4, 5, 6, 7, 8, 9])
count = 0
while True:
    i = Q.popleft()
    count += 1
    if count == k:
        print(i)
        break
    if i % 10 == 0:
        Q.append(i * 10)
        Q.append(i * 10 + 1)
    if i % 10 != 0 and i % 10 != 9:
        Q.append(i * 10 + i % 10 - 1)
        Q.append(i * 10 + i % 10)
        Q.append(i * 10 + i % 10 + 1)
    if i % 10 == 9:
        Q.append(i * 10 + i % 10 - 1)
        Q.append(i * 10 + i % 10)
