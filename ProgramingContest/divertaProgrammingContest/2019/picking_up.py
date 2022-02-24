from collections import defaultdict
N = int(input())
S = []
for i in range(N):
    x,y = map(int,input().split())
    S.append((x,y))

cnt = defaultdict(int)
for i in range(N):
    for j in range(N):
        if i ==j:
            continue
        x1,y1 =S[i]
        x2,y2 = S[j]
        cnt[(x1-x2,y1-y2)]+=1

max_cnt = 0
for i in cnt.values():
    max_cnt = max(max_cnt,i)
print(N-max_cnt)