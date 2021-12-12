from collections import defaultdict
N = int(input())
W = []
for i in range(N):
    W.append(input())
count = defaultdict(int)
ans1 = 0    
for i in range(N):
    count[W[i]]+=1
    if count[W[i]] ==2:
        ans1= i
        break
ans2 = 0
for i in range(N-1):
    if W[i][len(W[i])-1] != W[i+1][0]:
        ans2 = i+1
        break
if ans1>0 and ans2>0:
    ans = min(ans1,ans2)
else:
    ans =max(ans1,ans2)
if ans==0:
    print("DRAW")
elif ans%2==0:
    print("LOSE")
else:
    print("WIN")