S = list(input())
S.append("R")

flag = False
lasts = []
goal = []
for i in range(1,len(S)):
    if S[i-1] =="R" and S[i] == "L":
        flag = True
        goal.append(i)
    if flag:
        if S[i] == "R":
            lasts.append(i)
            flag = False

start = 0

ans = [0]*(len(S)-1)
for i,j in enumerate(lasts):
    count1 =0
    count2 =0
    for k in range(start,j):
        if abs(goal[i] -k)%2 ==0:
            count1 +=1
        else:
            count2 +=1
    ans[goal[i]] =count1
    ans[goal[i]-1] = count2
    start = j

for a in ans:
    print(a ,end=" ")
