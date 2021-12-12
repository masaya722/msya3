import sys
sys.setrecursionlimit(10**8)
N,M =map(int,input().split())
friends = [[]for _ in range(N)]
S = []
for _ in range(M):
    a,b =map(int,input().split())
    a-=1
    b-=1
    if a<b:
        S.append((a,b))
    else:
        S.append((b,a))
not_duplicate = set(S)
for i,j in not_duplicate:
    friends[i].append(j)
    friends[j].append(i)

checked = [False for _ in range(N)]
temp_ans = 1
def dfs(i):
    global temp_ans
    if checked[i]:
        return
    checked[i] = True
    for j in friends[i]:
        if not checked[j]:
            temp_ans =max(temp_ans,temp_ans+1)
        dfs(j)
    return
ans = 0
for i in range(N):
    dfs(i)
    ans = max(temp_ans,ans)
    temp_ans = 1
print(ans)