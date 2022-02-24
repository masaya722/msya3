from collections import defaultdict,deque
N = int(input())
S = input()
ans = deque()
for s in S:
    ans.append(s)
cnt =defaultdict(int)
tmp = []
for i in range(N):
    if S[i] =='(':
        cnt['l']+=1
    else:
        cnt['r']+=1
    if cnt['l']<cnt['r']:
        ans.appendleft('(')
        cnt['l']+=1
while cnt['l']>cnt['r']:
    ans.append(')')
    cnt['r']+=1
s2 = ''
for a in ans:
    s2+=a
print(s2)

