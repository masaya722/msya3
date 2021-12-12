N, L = map(int, input().split())
S = []
for i in range(L):
    S.append(input())
S.reverse()
last = input()
goal = 0
for i in range(len(last)):
    if last[i] == 'o':
        goal = i
        break
for s in S:
    if goal != 2*N-1 and len(s)>=goal+2:
        if s[goal+1] == '-':
            goal += 2
            continue
    if goal != 0:
        if s[goal-1] == '-':
            goal -= 2
if goal == 0:
    print(1)
else:
    print(goal//2+1)
