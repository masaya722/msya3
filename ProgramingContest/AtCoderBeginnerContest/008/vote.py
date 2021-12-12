from collections import Counter
N =int(input())
S = []
for i in range(N):
    S.append(input())
count = Counter(S)
ans = count.most_common()[0][0]
print(ans)