from collections import Counter

N =int(input())
S = []
for _ in range(N):
    s = list(input())
    s.sort()
    S.append("".join(s))

count = Counter(S)
ans = 0
for i in count.values():
    if i ==1:
        continue
    else:
        ans += i*(i-1)//2
print(ans)

    
    