from collections import Counter

N = int(input())
A = []
for _ in range(N):
    A.append(int(input()))
count = Counter(A)
ans = 0
for i ,j in count.items():
    if j >1:
        ans+=j-1
print(ans)