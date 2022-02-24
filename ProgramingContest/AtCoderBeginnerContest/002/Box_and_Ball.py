from collections import defaultdict
n,m = map(int,input().split())

red_pass= [False for _ in range(n+1)]
red_pass[1] = True
box_cnt = defaultdict(int)
for i in range(1,n+1):
    box_cnt[i]+=1
for i in range(m):
    x,y = map(int,input().split())
    if red_pass[x]:
        red_pass[y] = True
    box_cnt[x]-=1
    if box_cnt[x] ==0:
        red_pass[x] = False
    box_cnt[y]+=1

ans = 0
for box_num,cnt in box_cnt.items():
    if red_pass[box_num] and cnt>0:
        ans+=1
print(ans)

